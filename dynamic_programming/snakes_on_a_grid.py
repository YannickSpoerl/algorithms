def snakes_on_a_grid(grid: list[list[int]]) -> (list[int], int):
    dp_table = []
    dp_table_path = []
    for i in range(0, len(grid) + 1):
        dp_table.append([])
        dp_table_path.append([])
        for j in range(0, len(grid[0])):
            if i == 0:
                dp_table[i].append(0)
            elif j == 0:
                dp_table[i].append(max(dp_table[i - 1][j], dp_table[i - 1][j + 1]) + grid[i - 1][j])
                dp_table_path[i].append(dp_table[i - 1].index(dp_table[-1][-1] - grid[i - 1][j]))
            elif j == len(grid[0]) - 1:
                dp_table[i].append(max(dp_table[i - 1][j - 1], dp_table[i - 1][j]) + grid[i - 1][j])
                dp_table_path[i].append(dp_table[i - 1].index(dp_table[-1][-1] - grid[i - 1][j], j - 1))
            else:
                dp_table[i].append(
                    max(dp_table[i - 1][j - 1], dp_table[i - 1][j], dp_table[i - 1][j + 1]) + grid[i - 1][j])
                dp_table_path[i].append(dp_table[i - 1].index(dp_table[-1][-1] - grid[i - 1][j]))

    max_val = max(dp_table[-1])
    path = [dp_table[-1].index(max_val)]
    for i in range(1, len(dp_table) - 1):
        path.insert(0, dp_table_path[-i][path[0]])
    return max(dp_table[-1]), [grid[i][j] for i, j in enumerate(path)]
