#!/usr/bin/python
from logging import info


class FileFormatException(IOError):
    pass


def read(file_path):
    with open(file_path) as f:
        for line in f:
            yield line


def get_max_accessories(file_path):
    """
    Function, that finds product ID with the highest number of accessories.
    For example, if accessories.txt contains:
    1: 8,17
    12: 2,3,4,5,6,7
    13: 
    15: 1,11
    Returns (12, 6) 
    """
    try:
        product_id_max = None
        max_accessories = 0
        for line in read(file_path):
            line_splitted = line.split(":")
            if len(line_splitted) != 2:
                raise FileFormatException("Line cannot be split by ':'")
            product_id, accessories = line_splitted
            accessories = accessories.split(",")
            if len(accessories) >= max_accessories:
                max_accessories = len(accessories)
                product_id_max = int(product_id)
        return product_id_max, max_accessories
    except FileFormatException:
        info("Bad input file. Please check format of your file")
        raise
    except IOError:
        info("Some I/O Problems")
    return None


if __name__ == '__main__':
    file_path = input()
    print(get_max_accessories(file_path))
