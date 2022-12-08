from typing import Optional


def find_marker_of_length(input: str, n: int) -> Optional[int]:
    for ngram in zip(*[input[i:] for i in range(n)]):
        chunk = "".join(ngram)
        if len(set(chunk)) == n:
            return input.index(chunk) + n

    return None


if __name__ == "__main__":
    with open("day6.txt") as infile:
        signal = infile.read()

    print(find_marker_of_length(signal, n=4))
    print(find_marker_of_length(signal, n=14))
