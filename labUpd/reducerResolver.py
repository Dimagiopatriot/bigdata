#!/usr/bin/env python
import sys
from itertools import groupby
from operator import itemgetter


def read_mapper_output(file):
    for line in file:
        yield line.rstrip()


def reduce(fileNames, separator='\t'):
    for fileName in fileNames:
        with open(fileName) as f:
            lines = f.readlines()

        try:
            total_count = len(lines)
            line_to_print = lines[0].split("\t", 1)[0]
            print("%s%s%d" % (line_to_print, separator, total_count))
        except ValueError:
            # count was not a number, so silently discard this item
            print("idi nahuy")
            pass


if __name__ == "__main__":
    data = read_mapper_output(sys.stdin)
    fileNames = []
    for fileName in data:
        fileNames.append(fileName)

    reduce(fileNames[0:int(fileNames.__len__() / 2)])
    reduce(fileNames[int(fileNames.__len__() / 2 + 1):])
