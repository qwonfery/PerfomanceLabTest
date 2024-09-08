import argparse
from math import dist


def find_locations(circle_radius: int, circle_center: list, points_data: list) -> list:
    point_locations = []
    for point in points_data:
        distance = dist(point, circle_center)
        if distance > circle_radius:
            point_location = '2'
        elif distance == circle_radius:
            point_location = '0'
        else:
            point_location = '1'
        point_locations.append(point_location)
    return point_locations


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("circle_filepath")
    parser.add_argument("points_filepath")

    args = parser.parse_args()

    with open(args.circle_filepath) as f:
        center = [int(i) for i in f.readline().split()]
        radius = int(f.readline())

    with open(args.points_filepath) as f:
        points_data_raw = f.read()

    points = []
    for point_data in points_data_raw.split('\n'):
        points.append([int(i) for i in point_data.split()])

    raw_answer = find_locations(radius, center, points)
    locations = "\n".join(raw_answer)
    with open("task2/point_locations", "w") as f:
        f.write(locations)
