import contextlib
import json
import os
import wave
from pathlib import Path
from typing import Dict

import polars as pl

with contextlib.suppress(ImportError):
    from dotenv import load_dotenv

    load_dotenv()
    print("Loading environment variables from .env file")

fsd_dir = Path(os.getenv("FSD_50K_DIR")) 

def _labels_from_str_to_list(string:str):
    string = string.strip().lower()
    return string.split(',')
    
def wav_metadata(row):
    
    path = fsd_dir / f"{row['filename']}_audio" / F"FSD50K.{row['filename']}_audio" / (str(row['fname'])+".wav")
    with contextlib.closing(wave.open(path.as_posix(), 'rb')) as wf:
        n_channels   = wf.getnchannels()
        samp_width   = wf.getsampwidth()
        framerate    = wf.getframerate()
        n_frames     = wf.getnframes()
        duration_sec = n_frames / float(framerate)
    return {
        'channels':    n_channels,
        'sample_width': samp_width, # bytes
        'sr':   framerate, # Hz
        'n_frames':    n_frames,
        'duration': duration_sec # seconds
    }
    
    
def fsd50k(fsd_dir: Path)->Dict[str,pl.DataFrame]:
    metadata_dir = fsd_dir/ "ground_truth" / "FSD50K.ground_truth"
    
    # Load metadata from CSV files
    metadata = {}
    for name in ['dev', 'eval']:
        file = metadata_dir / (name +'.csv')
        df = pl.read_csv(file)
        df= df.with_columns(pl.lit(name).alias("filename"))
        if name == 'eval':
            df = df.with_columns(pl.lit('test').alias("split"))
        metadata[name] = df
    metadata = pl.concat([metadata['eval'],metadata['dev']], how='diagonal')

    # Convert labels from comma-separated strings to lists
    metadata = metadata.with_columns(pl.col('labels').map_elements(_labels_from_str_to_list,return_dtype=pl.List(pl.Utf8)).alias('labels'))
    metadata = metadata.with_columns(pl.col('mids').map_elements(_labels_from_str_to_list,return_dtype=pl.List(pl.Utf8)).alias('mids'))
    vocabulary = pl.read_csv(metadata_dir / 'vocabulary.csv',has_header=False,new_columns=('fname','labels','mids'))
    vocabulary=vocabulary.with_columns(pl.col('labels').str.to_lowercase().alias('labels')) 
    vocab_set =set(vocabulary['labels'].unique())
    metadata_labels_set = set(metadata.explode('labels')['labels'].unique())
    if not vocab_set == metadata_labels_set:
        print(vocab_set-metadata_labels_set)
        print(metadata_labels_set-vocab_set)
        raise ValueError("The vocabulary and metadata labels do not match.")
    
    # Add waveform metadata to the dataframe
    metadata = metadata.with_columns(pl.struct(["fname", "filename"]).map_elements(wav_metadata).alias('tmp')).unnest('tmp')
    
    # Add additional metadata
    metadata_dir = fsd_dir/ "metadata" / "FSD50K.metadata"
    with (metadata_dir/"dev_clips_info_FSD50K.json").open('r') as f:
        clips_info = json.load(f)
    with (metadata_dir/"eval_clips_info_FSD50K.json").open('r') as f:
        eval_clips_info = json.load(f)
    assert set(clips_info.keys()).intersection(set(eval_clips_info.keys())) == set(), "Overlap between dev clips info and metadata"

    clips_info.update(eval_clips_info)
    def mapping_fn(fname):
        return clips_info[fname]
    
    metadata = metadata.with_columns(pl.col("fname").cast(pl.Utf8).map_elements(mapping_fn).alias('tmp')).unnest('tmp')
    return {'metadata': metadata, 'vocabulary': vocabulary}

if __name__ == "__main__":
    metadata = fsd50k(fsd_dir)
    print(metadata['metadata'])
    print(metadata['vocabulary'])