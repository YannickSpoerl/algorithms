def subset_sum(integers: list[int], weight: int) -> bool:
    """check if there is a subset of a given list of numbers that sums up to exactly the given weight
    :param integers: a list of integers
    :param weight: the sum to check up on
    :return: True if a subset of the integers sums to the weight
    """
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
