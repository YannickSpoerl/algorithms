def alarm_problem(integers: list[int]) -> (int, list[int]):
    pick = [integers[0]]
    skip = [0]
    pick_pred = [[0]]
    skip_pred = [[]]
    for i in range(1, len(integers)):
        pick.append(skip[i - 1] + integers[i])
        new_list = skip_pred[i - 1].copy()
        new_list.append(i)
        pick_pred.append(new_list)

        if pick[i - 1] > skip[i - 1]:
            skip.append(pick[i - 1])
            new_list = pick_pred[i - 1].copy()
            skip_pred.append(new_list)
        else:
            skip.append(skip[i - 1])
            new_list = skip_pred[i - 1].copy()
            skip_pred.append(new_list)

    if pick[-1] > skip[-1]:
        return pick[-1], pick_pred[-1]
    else:
        return skip[-1], skip_pred[-1]
