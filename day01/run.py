
def calculate_fuel_requirement(mass: int) -> int:
    return mass // 3 - 2


def calculate_fuel_requirement_total(mass: int) -> int:
    total_fuel_requirement = 0
    fuel = calculate_fuel_requirement(mass)

    while fuel > 0:
        total_fuel_requirement += fuel
        fuel = calculate_fuel_requirement(fuel)

    return total_fuel_requirement


with open('input.txt') as f:
    masses = [int(line.strip()) for line in f]
    sum_fuel_requirement = sum([calculate_fuel_requirement(mass) for mass in masses])
    print(f'Day 01. Part 1: {sum_fuel_requirement}')
    sum_fuel_requirement_total = sum([calculate_fuel_requirement_total(mass) for mass in masses])
    print(f'Day 01. Part 2: {sum_fuel_requirement_total}')
