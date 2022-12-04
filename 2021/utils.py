def adjacent_points(x, y, height=10, width=10, include_diagonals=True):
    points = []
    if x - 1 >= 0:
        points.append((x - 1, y))
    if x + 1 < width:
        points.append((x + 1, y))
    if y - 1 >= 0:
        points.append((x, y - 1))
    if y + 1 < height:
        points.append((x, y + 1))

    if include_diagonals:
        if x - 1 >= 0 and y - 1 >= 0:
            points.append((x - 1, y - 1))
        if x - 1 >= 0 and y + 1 < height:
            points.append((x - 1, y + 1))
        if x + 1 < width and y - 1 >= 0:
            points.append((x + 1, y - 1))
        if x + 1 < width and y + 1 < height:
            points.append((x + 1, y + 1))

    return points
