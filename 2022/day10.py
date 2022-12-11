from typing import Union

Instruction = tuple[str, Union[int, None]]


def run(instructions: list[str], x: int = 1) -> list[int]:
    run_log: list[int] = []

    for line in instructions:
        instruction: str = line.strip()
        if instruction.startswith("noop"):
            run_log.append(x)
        else:
            run_log.append(x)

            _, number = instruction.split(" ")

            run_log.append(x)
            x = x + int(number)

    return run_log


def signal_strengths(run_log: list[int]) -> list[int]:
    return [x * i for i, x in enumerate(run_log, start=1)]


def draw_crt(run_log: list[int]):
    out = []

    for i, x in enumerate(run_log, start=0):
        pixel = i % 40
        if pixel in [x - 1, x, x + 1]:
            out.append("#")
        else:
            out.append(".")

    for i in range(0, len(out), 40):
        print("".join(out[i : i + 40]))


if __name__ == "__main__":
    with open("day10.txt") as infile:
        run_log = run(infile.readlines())

    strengths = signal_strengths(run_log)
    print(sum(strengths[i] for i in range(19, len(strengths), 40)))

    draw_crt(run_log)
