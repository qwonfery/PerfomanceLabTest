import argparse


def circle_array(n: int):
    while True:
        cnt = 1
        while not cnt > n:
            yield cnt
            cnt += 1


def get_path(length: int, step: int) -> list:
    array_generator = circle_array(length)
    first = next(array_generator)
    interval_end = 0
    path = [first]

    while True:
        for i in range(step - 1):
            interval_end = next(array_generator)
        if interval_end == first:
            break
        path.append(interval_end)
    return path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("length")
    parser.add_argument("step")

    args = parser.parse_args()
    answer = get_path(int(args.length), int(args.step))

    print("".join([str(i) for i in answer]))
