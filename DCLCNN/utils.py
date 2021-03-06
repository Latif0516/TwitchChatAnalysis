import numpy as np
import tensorflow as tf

ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789-,;.!?:\'\"/\\|_@#$%^&*~`+ =<>()[]{}"  # len: 69
FEATURE_LEN = 512


def get_char_dict():
    cdict = {}
    for i, c in enumerate(ALPHABET):
        cdict[c] = i + 2

    return cdict


def get_vectorized_comment(text, max_length=FEATURE_LEN):
    array = np.ones(max_length)
    count = 0
    cdict = get_char_dict()

    for ch in text:
        if ch in cdict:
            array[count] = cdict[ch]
            count += 1

        if count >= FEATURE_LEN - 1:
            return array

    return array


def to_categorical(y, nb_classes=None):
    y = np.asarray(y, dtype='int32')

    if not nb_classes:
        nb_classes = np.max(y) + 1

    Y = np.zeros((len(y), nb_classes))
    for i in range(len(y)):
        Y[i, y[i]] = 1.

    return Y
