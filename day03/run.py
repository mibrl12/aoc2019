from typing import List, Tuple


def calculate_distance(x, y) -> int:
    return abs(0 - x) + abs(0 - y)


def find_intersections(
        points_wire_1: List[Tuple[int, int]], points_wire_2: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    return list(set(points_wire_1) & set(points_wire_2))


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


def calculate_steps_to_intersection(points: List[int], intersection: Tuple[int, int]) -> int:
    for i, point in enumerate(points):
        if point == intersection:
            return i + 1
    return -1


def calculate_closest_intersection(wire_1: str, wire_2: str) -> int:
    points_wire_1 = get_wire_points(wire_1.split(','))
    points_wire_2 = get_wire_points(wire_2.split(','))

    intersections = find_intersections(points_wire_1, points_wire_2)

    closest_distance_to_intersection = calculate_steps_to_intersection(points_wire_1, intersections[0]) + \
                                       calculate_steps_to_intersection(points_wire_2, intersections[0])

    for i, intersection in enumerate(intersections):
        if i == 0:
            continue

        distance_to_intersection = calculate_steps_to_intersection(points_wire_1, intersections[i]) + \
                                   calculate_steps_to_intersection(points_wire_2, intersections[i])

        if distance_to_intersection < closest_distance_to_intersection:
            closest_distance_to_intersection = distance_to_intersection

    return closest_distance_to_intersection


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


with open('input.txt') as f:
    wire_1 = f.readline()
    wire_2 = f.readline()
    day_1_solution = calculate_manhattan_distance(wire_1, wire_2)
    print(f'Day 03. Part 1: \n{day_1_solution}')
    day_2_solution = calculate_closest_intersection(wire_1, wire_2)
    print(f'Day 03. Part 2: \n{day_2_solution}')
