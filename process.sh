#!/bin/bash
cd "${0%/*}"

TRAIN_IMG=train_img
TRAIN_LBL=train_lbl
TEST_IMG=test_img
TEST_LBL=test_lbl

ODIR=data

mkdir $ODIR 2>/dev/null

echo 'Fetching files'
curl http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz -o $ODIR/$TRAIN_IMG.ubyte.gz
curl http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz -o $ODIR/$TRAIN_LBL.ubyte.gz
curl http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz -o $ODIR/$TEST_IMG.ubyte.gz
curl http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz -o $ODIR/$TEST_LBL.ubyte.gz

echo 'Deflating files'
gunzip data/*

python3 convert_to_json.py

echo 'Compressing JSON files'
gzip -k *.json
