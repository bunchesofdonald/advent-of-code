def end_point(commands):
    position = depth = 0

    for command_string in commands:
        command, amount = command_string.split(' ')
        amount = int(amount)

        match command:
            case 'down':
                depth += amount
            case 'up':
                depth -= amount
            case 'forward':
                position += amount

    return position, depth


def better_end_point(commands):
    aim = position = depth = 0

    for command_string in commands:
        command, amount = command_string.split(' ')
        amount = int(amount)

        match command:
            case 'down':
                aim += amount
            case 'up':
                aim -= amount
            case 'forward':
                position += amount
                depth += amount * aim

    return position, depth


if __name__ == '__main__':
    with open('day2.txt') as infile:
        commands = [line.strip() for line in infile.readlines()]

    position, depth = end_point(commands)
    print(position * depth)

    position, depth = better_end_point(commands)
    print(position * depth)
