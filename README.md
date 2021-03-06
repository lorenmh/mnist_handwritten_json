# MNIST Handwritten Digits as JSON
All data is from http://yann.lecun.com/exdb/mnist/.

There are **70,000** examples in total in the datasets:

* **60,000** training examples in `mnist_handwritten_train.json`
* **10,000** test examples in `mnist_handwritten_test.json`

The data is in a JSON format. Each JSON file contains an array of objects,
where each object has two fields:

* `image`: a 784-element array of numbers [0,255], representing pixel values
  for each 28x28 handwritten image. `0` means background (white) and `255` means
  foreground (black).
* `label`: the label for this character

There are two JSON files; one is training data and the other is test data.
These two sets were provided from the original MNIST dataset.

## File sizes

    2.8M  mnist_handwritten_test.json.gz
    17M   mnist_handwritten_train.json.gz

**I strongly suggest you download the gzipped files, as the non-gzipped files
are very large**

## Download / Decompress

To download the files, something like this should work:

    curl -LO https://github.com/lorenmh/mnist_handwritten_json/raw/master/mnist_handwritten_test.json.gz
    curl -LO https://github.com/lorenmh/mnist_handwritten_json/raw/master/mnist_handwritten_train.json.gz

To decompress:

    gunzip *.gz

If you clone you will need [git-lfs](https://git-lfs.github.com/).

## To run
You'll need the `process.sh` and `convert_to_json.py` files in some directory. The `process.sh` script will create a directory `data/` in the same directory as the script, and will call `convert_to_json.py` to convert the data from the IDX format to JSON.

I just removed the non-gzipped JSON files as Github has been notifying me that I am going over my data limits, my guess is it's the 420MB uncompressed JSON file I had in here :)
