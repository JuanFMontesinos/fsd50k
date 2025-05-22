# What's this repo for  
Surf throughout the mess of metadata files without spending hours of your life.  

1-click download of the [FSD50K dataset](https://annotator.freesound.org/fsd/release/FSD50K/).  
Easy function to create a dataframe with all the metadata of the dataset.

## How to use  
1. Download the dataset by `bash fsd50k.sh path_to_destination` (linux only)
2. Install polars: `pip install polars`
3. Export the environment variable `FSD50K_DIR` by doing `export FSD50K_DIR=path_to_destination`
4. Run `python3 fsd50k.py`   
If you see
```
shape: (51_197, 15)
┌────────┬───────────────┬───────────────┬──────────┬───┬───────────────┬───────────────┬───────────────┬──────────────┐
│ fname  ┆ labels        ┆ mids          ┆ filename ┆ … ┆ description   ┆ tags          ┆ license       ┆ uploader     │
│ ---    ┆ ---           ┆ ---           ┆ ---      ┆   ┆ ---           ┆ ---           ┆ ---           ┆ ---          │
│ i64    ┆ list[str]     ┆ list[str]     ┆ str      ┆   ┆ str           ┆ list[str]     ┆ str           ┆ str          │
╞════════╪═══════════════╪═══════════════╪══════════╪═══╪═══════════════╪═══════════════╪═══════════════╪══════════════╡
│ 37199  ┆ ["electric_gu ┆ ["/m/02sgy",  ┆ eval     ┆ … ┆ Electric      ┆ ["electric",  ┆ http://creati ┆ UncleSigmund │
│        ┆ itar",        ┆ "/m/0342h", … ┆          ┆   ┆ guitar.       ┆ "guitar"]     ┆ vecommons.org ┆              │
│        ┆ "guitar", …   ┆ "/m…          ┆          ┆   ┆               ┆               ┆ /pub…         ┆              │
│ 175151 ┆ ["electric_gu ┆ ["/m/02sgy",  ┆ eval     ┆ … ┆ Another       ┆ ["electric",  ┆ http://creati ┆ MinigunFiend │
│        ┆ itar",        ┆ "/m/0342h", … ┆          ┆   ┆ single,       ┆ "cowboy", …   ┆ vecommons.org ┆              │
│        ┆ "guitar", …   ┆ "/m…          ┆          ┆   ┆ urgent,       ┆ "dese…        ┆ /pub…         ┆              │
│        ┆               ┆               ┆          ┆   ┆ danger…       ┆               ┆               ┆              │
│ 253463 ┆ ["electric_gu ┆ ["/m/02sgy",  ┆ eval     ┆ … ┆ Electric lead ┆ ["electric",  ┆ http://creati ┆ GW7fold      │
│        ┆ itar",        ┆ "/m/0342h", … ┆          ┆   ┆ guitar lick   ┆ "distortion", ┆ vecommons.org ┆              │
│        ┆ "guitar", …   ┆ "/m…          ┆          ┆   ┆ in k…         ┆ … "…          ┆ /lic…         ┆              │
│ 329838 ┆ ["electric_gu ┆ ["/m/02sgy",  ┆ eval     ┆ … ┆ Old epiphone  ┆ ["guitar",    ┆ http://creati ┆ deerstalking │
│        ┆ itar",        ┆ "/m/0342h", … ┆          ┆   ┆ through an    ┆ "electric",   ┆ vecommons.org ┆              │
│        ┆ "guitar", …   ┆ "/m…          ┆          ┆   ┆ Edirol…       ┆ "loop"]       ┆ /lic…         ┆              │
│ 1277   ┆ ["electric_gu ┆ ["/m/02sgy",  ┆ eval     ┆ … ┆ looped guitar ┆ ["arpeggio",  ┆ http://creati ┆ plagasul     │
│        ┆ itar",        ┆ "/m/0342h", … ┆          ┆   ┆ arpeggio,     ┆ "dreamy", …   ┆ vecommons.org ┆              │
│        ┆ "guitar", …   ┆ "/m…          ┆          ┆   ┆ mellow…       ┆ "mell…        ┆ /lic…         ┆              │
│ …      ┆ …             ┆ …             ┆ …        ┆ … ┆ …             ┆ …             ┆ …             ┆ …            │
│ 102863 ┆ ["fowl", "liv ┆ ["/m/025rv6n" ┆ dev      ┆ … ┆ Barnacle      ┆ ["barnacle",  ┆ http://creati ┆ dobroide     │
│        ┆ estock_and_fa ┆ , "/m/0ch8v", ┆          ┆   ┆ Geese calling ┆ "field-record ┆ vecommons.org ┆              │
│        ┆ rm_a…         ┆ "/m…          ┆          ┆   ┆ at a St…      ┆ ing"…         ┆ /lic…         ┆              │
│ 389607 ┆ ["fowl", "liv ┆ ["/m/025rv6n" ┆ dev      ┆ … ┆ An H4N        ┆ ["birds", "fi ┆ http://creati ┆ 16coreyn     │
│        ┆ estock_and_fa ┆ , "/m/0ch8v", ┆          ┆   ┆ recording of  ┆ eld-recording ┆ vecommons.org ┆              │
│        ┆ rm_a…         ┆ "/m…          ┆          ┆   ┆ geese on t…   ┆ ", ……         ┆ /pub…         ┆              │
│ 90091  ┆ ["fowl", "liv ┆ ["/m/025rv6n" ┆ dev      ┆ … ┆ these are the ┆ ["ducks",     ┆ http://creati ┆ Justin.Mckin │
│        ┆ estock_and_fa ┆ , "/m/0ch8v", ┆          ┆   ┆ sounds of     ┆ "pong",       ┆ vecommons.org ┆ sey          │
│        ┆ rm_a…         ┆ "/m…          ┆          ┆   ┆ backgr…       ┆ "splashing"]  ┆ /pub…         ┆              │
│ 244718 ┆ ["fowl", "liv ┆ ["/m/025rv6n" ┆ dev      ┆ … ┆ Recording of  ┆ ["bucharest", ┆ http://creati ┆ jlseagull    │
│        ┆ estock_and_fa ┆ , "/m/0ch8v", ┆          ┆   ┆ ducks and     ┆ "romania", …  ┆ vecommons.org ┆              │
│        ┆ rm_a…         ┆ "/m…          ┆          ┆   ┆ water f…      ┆ "wa…          ┆ /pub…         ┆              │
│ 24061  ┆ ["fowl", "liv ┆ ["/m/025rv6n" ┆ dev      ┆ … ┆ Series of     ┆ ["ambiance",  ┆ http://creati ┆ LG           │
│        ┆ estock_and_fa ┆ , "/m/0ch8v", ┆          ┆   ┆ small-sized   ┆ "birds", …    ┆ vecommons.org ┆              │
│        ┆ rm_a…         ┆ "/m…          ┆          ┆   ┆ recordin…     ┆ "voice…       ┆ /lic…         ┆              │
└────────┴───────────────┴───────────────┴──────────┴───┴───────────────┴───────────────┴───────────────┴──────────────┘
```
Congrats, it works. Copy the file in your repo and be happy. 