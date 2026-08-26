# Olivia Vesper wheelhouse + splitter contract

python scripts/split_zip.py split SRC --out DIR [--max-bytes 10485760]
python scripts/split_zip.py join DIR --out RESTORED [--from-b64]
python scripts/split_zip.py proof SRC --out DIR

Each .partNNNN.zip is <= 10 MiB. SPLIT_MANIFEST.json carries SHA-256.
.zip.b64 sidecars are Colab/Spark text transport.
Skill 0.2.0. Absolute Liv HUB.
