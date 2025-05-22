#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<EOF
Usage: $(basename "$0") <DEST_ROOT>
Download and unpack the FSD50K dataset into the given root directory.

Arguments:
  DEST_ROOT   Path to the folder where FSD50K will be created.
EOF
  exit 1
}

# Check for required argument
if [ $# -ne 1 ]; then
  usage
fi

# Where to download and unpack
DEST_ROOT="$1"
DEST_DIR="${DST_ROOT%/}"    # Ensure no trailing slash, then append
BASE_URL="https://zenodo.org/records/4060432/files"

# Files to fetch
FILES=(
  "FSD50K.dev_audio.z01"
  "FSD50K.dev_audio.z02"
  "FSD50K.dev_audio.z03"
  "FSD50K.dev_audio.z04"
  "FSD50K.dev_audio.z05"
  "FSD50K.dev_audio.zip"
  "FSD50K.eval_audio.z01"
  "FSD50K.eval_audio.zip"
  "FSD50K.ground_truth.zip"
  "FSD50K.metadata.zip"
  "FSD50K.doc.zip"
)

echo "Creating destination directory: ${DEST_DIR}"
mkdir -p "${DEST_DIR}"
cd "${DEST_DIR}"

echo "Starting download of FSD50K components…"
for f in "${FILES[@]}"; do
  echo " → Downloading ${f}"
  wget -c "${BASE_URL}/${f}?download=1" -O "${f}"
done

echo
echo "Merging and extracting development audio…"
zip -s 0 FSD50K.dev_audio.zip --out dev_unsplit.zip
unzip -q dev_unsplit.zip -d dev_audio

echo "Merging and extracting evaluation audio…"
zip -s 0 FSD50K.eval_audio.zip --out eval_unsplit.zip
unzip -q eval_unsplit.zip -d eval_audio

echo "Extracting metadata, ground truth, and documentation…"
unzip -q FSD50K.metadata.zip   -d metadata
unzip -q FSD50K.ground_truth.zip -d ground_truth
unzip -q FSD50K.doc.zip         -d doc

echo
echo "All done! Your FSD50K dataset is in ${DEST_DIR}"
