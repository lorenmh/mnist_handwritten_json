#!/usr/local/bin/python3
'''
Loren Howard - 1/13/2018

The file format is documented here:
    http://yann.lecun.com/exdb/mnist/

This script simply converts the files from http://yann.lecun.com/exdb/mnist/
into a simple JSON format;

The outputted JSON file is an array of objects with two fields:
    image: an array with 784 0-255 pixel values (28*28*1byte image)
    label: the corresponding label for this image
'''


import json
import struct

UNPACK = (('data/test_img.ubyte', 'data/test_lbl.ubyte', 'mnist_handwritten_test.json'),
          ('data/train_img.ubyte', 'data/train_lbl.ubyte', 'mnist_handwritten_train.json'))

IMG_HEADER_FMT = '>IIII'
IMG_HEADER_SZ = 16

LBL_HEADER_FMT = '>II'
LBL_HEADER_SZ = 8

LBL_FMT = 'B'
LBL_SZ = 1

JSON_INDENT = 2

def struct_unpack_file(struct_fmt, struct_sz, f):
    while True:
        bytes = f.read(struct_sz)
        if not bytes:
            break
        yield struct.unpack(struct_fmt, bytes)

def unpack(img_fname, lbl_fname, o_fname):
    print('Unpacking %s and %s and outputting as %s' % (img_fname, lbl_fname,
                                                        o_fname))
    img_file = open(img_fname, 'rb')
    lbl_file = open(lbl_fname, 'rb')

    img_header = img_file.read(IMG_HEADER_SZ)
    lbl_header = lbl_file.read(LBL_HEADER_SZ)

    _, num_img, num_row, num_col = struct.unpack(IMG_HEADER_FMT, img_header)
    _, num_lbl =                   struct.unpack(LBL_HEADER_FMT, lbl_header)

    if num_img != num_lbl:
        raise ValueError('number of labels != number of images')

    img_sz = num_row * num_col
    img_fmt = 'B' * img_sz

    img_gen = struct_unpack_file(img_fmt, img_sz, img_file)
    lbl_gen = struct_unpack_file(LBL_FMT, LBL_SZ, lbl_file)

    lst = [{'image': img, 'label': lbl} for img,[lbl] in zip(img_gen, lbl_gen)]

    o_file = open(o_fname, 'w')
    json.dump(lst, o_file, indent=JSON_INDENT)

    img_file.close()
    lbl_file.close()
    o_file.close()

for args in UNPACK:
    unpack(*args)
