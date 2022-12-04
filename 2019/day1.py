def naieve_fuel_cost(mass):
    result = int(mass) // 3 - 2
    if result > 0:
        return result
    return 0


def full_fuel_cost(mass):
    results = [naieve_fuel_cost(mass)]
    curr_result = results[0]
    while curr_result > 0:
        curr_result = naieve_fuel_cost(curr_result)
        results.append(curr_result)

    return sum(results)


if __name__ == "__main__":
    with open("day1.txt") as input:
        print(sum([naieve_fuel_cost(mass) for mass in input.readlines()]))

    with open("day1.txt") as input:
        print(sum([full_fuel_cost(mass) for mass in input.readlines()]))
