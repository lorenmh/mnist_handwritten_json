# MNIST Handwritten Digits as JSON
All data is from http://yann.lecun.com/exdb/mnist/.

The data is in a JSON format. Each JSON file contains an array of objects,
where each object has two fields:

* `image`: a 784-element array of numbers [0,255], representing pixel values
  for each 28x28 handwritten image. 0 means background (white) and 255 means
  foreground (black).
* `label`: the label for this character

There are two JSON files; one is training data and the other is test data.
These two sets were provided from the original MNIST dataset.
