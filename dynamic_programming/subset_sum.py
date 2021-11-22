def subset_sum(integers: list[int], weight: int) -> bool:
    dp_table = []
    for i in range(0, len(integers)):
        dp_table.append([])
        for j in range(0, weight + 1):
            if i == 0:
                dp_table[i].append(j == integers[0])
            elif j == 0:
                dp_table[i].append(True)
            elif j >= integers[i]:
                dp_table[i].append(dp_table[i - 1][j] or dp_table[i - 1][j - integers[i]])
            else:
                dp_table[i].append(dp_table[i - 1][j])
    return dp_table[-1][-1]
