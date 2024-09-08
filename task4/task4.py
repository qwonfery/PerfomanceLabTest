import argparse
from statistics import median


def find_min_moves(array: list) -> int:
    array_median = median(array)
    moves = sum(abs(num - array_median) for num in array)
    return moves


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("nums_filepath")

    file = parser.parse_args().nums_filepath

    with open(file) as f:
        raw_nums = f.read()
    nums = [int(i) for i in raw_nums.split('\n')]

    print(find_min_moves(nums))
