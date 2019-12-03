from typing import List, Tuple


def calculate_distance(x, y) -> int:
    return abs(0 - x) + abs(0 - y)


def calculate_manhattan_distance(wire_1: str, wire_2: str) -> int:
    points_wire_1 = get_wire_points(wire_1.split(','))
    points_wire_2 = get_wire_points(wire_2.split(','))

    intersections = find_intersections(points_wire_1, points_wire_2)

    closest_intersection_dist = calculate_distance(*intersections[0])

    for i, intersection in enumerate(intersections):
        if i == 0:
            continue

        intersection_dist = calculate_distance(*intersections[i])

        if intersection_dist < closest_intersection_dist:
            closest_intersection_dist = intersection_dist

    return closest_intersection_dist


def get_wire_points(steps_wire_1):
    x, y = 0, 0

    points = []

    for step in steps_wire_1:
        direction = step[0]
        distance = int(step[1:])

        points += get_path_points(x, y, direction, distance)

        x, y = points[-1]

    return points


def get_path_points(x, y, direction: str, distance: int) -> List[Tuple[int, int]]:
    path_points = []

    for i in range(distance):
        if direction == 'L':
            x, y = x - 1, y
        if direction == 'R':
            x, y = x + 1, y
        if direction == 'D':
            x, y = x, y - 1
        if direction == 'U':
            x, y = x, y + 1

        path_points.append((x, y))

    return path_points


def find_intersections(
        points_wire_1: List[Tuple[int,int]], points_wire_2: List[Tuple[int,int]]) -> List[Tuple[int,int]]:
    return list(set(points_wire_1) & set(points_wire_2))


with open('input.txt') as f:
    wire_1 = f.readline()
    wire_2 = f.readline()
    day_1_solution = calculate_manhattan_distance(wire_1, wire_2)
    print(f'Day 03. Part 1: \n{day_1_solution}')
