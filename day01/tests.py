from day01.run import calculate_fuel_requirement, calculate_fuel_requirement_total

assert calculate_fuel_requirement(12) == 2
assert calculate_fuel_requirement(14) == 2
assert calculate_fuel_requirement(1969) == 654
assert calculate_fuel_requirement(100756) == 33583


assert calculate_fuel_requirement_total(14) == 2
assert calculate_fuel_requirement_total(1969) == 966
assert calculate_fuel_requirement_total(100756) == 50346
