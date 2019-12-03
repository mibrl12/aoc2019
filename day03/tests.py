from day03.run import calculate_manhattan_distance, calculate_closest_intersection

assert calculate_manhattan_distance(
    wire_1='R8,U5,L5,D3',
    wire_2='U7,R6,D4,L4') == 6

test_1_wire_1_str = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
test_1_wire_2_str = 'U62,R66,U55,R34,D71,R55,D58,R83'

test_2_wire_1_str = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
test_2_wire_2_str = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'

assert calculate_manhattan_distance(wire_1=test_1_wire_1_str, wire_2=test_1_wire_2_str) == 159


assert calculate_manhattan_distance(wire_1=test_2_wire_1_str, wire_2=test_2_wire_2_str) == 135


assert calculate_closest_intersection(wire_1=test_1_wire_1_str, wire_2=test_1_wire_2_str) == 610


assert calculate_closest_intersection(wire_1=test_2_wire_1_str, wire_2=test_2_wire_2_str) == 410
