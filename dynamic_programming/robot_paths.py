def robot_paths(x: int, y: int) -> int:
    """compute the number of paths from top-left to bottom-right cell in a x-y-grid
    :param x: width of grid
    :param y: length of grid
    :return: number of possible paths, when only walking right or down a cell
    """
    number_of_paths = []
    for i in range(0, x + 1):
        number_of_paths.append([])
        for j in range(0, y + 1):
            if i == 0 or j == 0:
                number_of_paths[i].append(0)
            elif i == 1 and j == 1:
                number_of_paths[i].append(1)
            else:
                number_of_paths[i].append(number_of_paths[i - 1][j] + number_of_paths[i][j - 1])
    return number_of_paths[x][y]
