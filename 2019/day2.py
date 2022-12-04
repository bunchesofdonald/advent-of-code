import copy
import operator


def run_intcode(intcode, verb=None, noun=None):
    output = copy.copy(intcode)
    if verb and noun:
        output[1] = verb
        output[2] = noun

    for i in range(0, len(output), 4):
        opcode = output[i]
        if opcode == 99:
            break

        func = operator.add if opcode == 1 else operator.mul
        x = output[output[i + 1]]
        y = output[output[i + 2]]
        pos = output[i + 3]

        output[pos] = func(x, y)

    return output


def find_verb_noun(intcode, checksum):
    for x in range(100):
        for y in range(100):
            result = run_intcode(intcode, x, y)[0]
            if result == checksum:
                return x, y


if __name__ == "__main__":
    with open("day2.txt") as input:
        intcode = [int(code) for code in input.read().strip().split(",")]

    print(run_intcode(intcode, 12, 2)[0])
    print(find_verb_noun(intcode, 19690720))
