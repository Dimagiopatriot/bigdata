#!/usr/bin/env python

import sys


def read_input(file):
    for line in file:
        # split the line into words
        yield line.split()


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        f = open("file1.txt", "w+")
        for word in words:
            f.write(word + separator + "1" + "\n")
        f.close()


if __name__ == "__main__":
    main()
