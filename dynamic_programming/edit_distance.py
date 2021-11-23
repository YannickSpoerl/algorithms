from typing import Callable


def default_cost_func(char1: str, char2: str) -> int:
    if char1 == char2:
        return 0
    return 1


def edit_distance(string1: str, string2: str, delta_cost_func: Callable[[str, str], int] = default_cost_func) -> int:
    """Given two string, and an optional cost-function for two chars, computes the minimum-distance
    :param string1: first string to compare
    :param string2: second string to compare
    :param delta_cost_func: a function that takes two characters (including empty) and returns the cost of alignment
    :return: the minimal cost of aligning both strings
    """
    alignment_table = []
    for i in range(0, len(string1) + 1):
        alignment_table.append([])
        for j in range(0, len(string2) + 1):
            if i == 0 and j == 0:
                alignment_table[i].append(0)
                continue
            elif i == 0 and j != 0:
                alignment_table[i].append(alignment_table[i][j - 1] + delta_cost_func("", string2[j - 1]))
                continue
            elif i != 0 and j == 0:
                alignment_table[i].append(alignment_table[i - 1][j] + delta_cost_func(string1[i - 1], ""))
                continue

            cost_delete1 = alignment_table[i - 1][j] + delta_cost_func("", string2[j - 1])
            cost_delete2 = alignment_table[i][j - 1] + delta_cost_func(string1[i - 1], "")
            cost_change_chars = alignment_table[i - 1][j - 1] + delta_cost_func(string1[i - 1], string2[j - 1])

            alignment_table[i].append(min(cost_delete1, cost_delete2, cost_change_chars))

    return alignment_table[len(string1)][len(string2)]
