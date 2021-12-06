def depth_window_sums(depths, n):
    result = []
    for depths in zip(*[depths[i:] for i in range(n)]):
        result.append(sum(depths))
    return result


def depth_increase_rate(depths):
    count = 0
    last = depths[0]
    for depth in depths[1:]:
        if depth > last:
            count += 1
        last = depth

    return count


def depth_increase_rate_window(depths, window_size=3):
    count = 0
    depth_sums = depth_window_sums(depths, window_size)
    last = depth_sums[0]
    for sum in depth_sums[1:]:
        if sum > last:
            count += 1
        last = sum

    return count


if __name__ == '__main__':
    with open('day1.txt') as infile:
        depths = [
            int(depth.strip()) for depth in
            infile.readlines()
        ]

    print(depth_increase_rate(depths))
    print(depth_increase_rate_window(depths))
