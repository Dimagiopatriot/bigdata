#!/usr/bin/env python

def read_file(name):
    with open(name) as f:
        lines = f.readlines()
    return lines


def split_data(data):
    array = []
    buffItem = data[0]
    buffArray = []
    for item in data:
        if (buffItem == item):
            buffArray.append(item)
            if (item == data[-1]):
                array.append(buffArray)
        else:
            array.append(buffArray.copy())
            buffArray.clear()
            buffItem = item
            buffArray.append(item)
    return array


if __name__ == "__main__":
    data = read_file("file1.txt")
    data += read_file("file2.txt")
    data.sort()

    res = split_data(data)
    for item in res:
        filename = item[0][0:3]
        f = open(filename, "w+")
        print(filename)
        for jitem in item:
            f.write(jitem)
        f.close()
