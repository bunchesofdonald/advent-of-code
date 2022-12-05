import copy
import re

Crate = str
Stack = list[Crate]
Procedure = tuple[int, int, int]

def _read_crates(lines: list[str]) -> list[Stack]:
    num_crates = 0

    # Find out how many stacks of crates we're dealing with
    for line in lines:
        if '1' in line:
            num_crates = int(line.strip()[-1])
            break

    # Initialize our stacks
    crates = []
    for _ in range(num_crates):
        crates.append(list())

    # Add the crates
    for line in lines:
        if '[' not in line:
            break

        for n in range(1, len(line), 4):
            crate = line[n]
            if crate == ' ':
                continue

            stack_number = int(((n - 1) / 4))
            crates[stack_number].append(crate)

    return crates


def _read_procedures(lines: list[str]) -> list[Procedure]:
    procedures = []
    for line in lines:
        line = line.strip()

        if 'move' not in line:
            continue

        match = re.match(r'move (\d+) from (\d+) to (\d+)', line)
        number = int(match.group(1))
        move_from = int(match.group(2)) - 1
        move_to = int(match.group(3)) - 1
        procedures.append((number, move_from, move_to))

    return procedures

def read_crates_and_procedures(lines: list[str]) -> tuple[list[Stack], list[Procedure]]:
    crates = _read_crates(lines)
    procedures = _read_procedures(lines)

    return crates, procedures


def do_procedures(crates: list[Stack], procedures: list[Procedure], mode=9000):
    crates = copy.deepcopy(crates)

    for number, move_from, move_to in procedures:
        if mode == 9000:
            for _ in range(number):
                crate = crates[move_from].pop(0)
                crates[move_to].insert(0, crate)
        elif mode == 9001:
            to_move = crates[move_from][:number]
            del crates[move_from][:number]
            for crate in to_move[::-1]:
                crates[move_to].insert(0, crate)

    return crates


if __name__ == "__main__":
    with open("day5.txt") as infile:
        crates, procedures = read_crates_and_procedures(infile.readlines())

    new_crates = do_procedures(crates, procedures)
    print(''.join([stack[0] for stack in new_crates if stack]))

    new_crates = do_procedures(crates, procedures, mode=9001)
    print(''.join([stack[0] for stack in new_crates if stack]))
