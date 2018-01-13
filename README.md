# MNIST Handwritten Digits as JSON
All data is from http://yann.lecun.com/exdb/mnist/.

The data is in a JSON format. Each JSON file contains an array of objects,
where each object has two fields:

* `image`: a 784-element array of numbers [0,255], representing pixel values
  for each 28x28 handwritten image. `0` means background (white) and `255` means
  foreground (black).
* `label`: the label for this character

There are two JSON files; one is training data and the other is test data.
These two sets were provided from the original MNIST dataset.

## File sizes

    70M   mnist_handwritten_test.json
    421M  mnist_handwritten_train.json
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
