class KnapsackItem:
    """Item with id, weight and value for use in knapsack"""

    def __init__(self, item_id, weight, value):
        self.item_id = item_id
        self.weight = weight
        self.value = value

    def __repr__(self):
        return f"({self.item_id}, {self.weight}, {self.value})"


def knapsack(list_of_items: list[KnapsackItem], max_capacity: int) -> (list[KnapsackItem], int):
    """Returns subset, total-value of list_items with highest accumulative value with total_capacity =< max_capacity"""
    val_table = []
    list_table = []
    for i in range(0, len(list_of_items) + 1):
        val_table.append([])
        list_table.append([])
        for w in range(0, max_capacity + 1):
            if i == 0 or w == 0:
                val_table[i].append(0)
                list_table[i].append([])
                continue

            item = list_of_items[i - 1]
            val_excluded = val_table[i - 1][w]
            val_included = 0

            if item.weight <= w:
                val_included = item.value + val_table[i - 1][w - item.weight]

            if val_included > val_excluded:
                val_table[i].append(val_included)
                new_list = list_table[i - 1][w - item.weight].copy()
                new_list.append(item)
                list_table[i].append(new_list)
            else:
                val_table[i].append(val_table[i - 1][w])
                list_table[i].append(list_table[i - 1][w])

    return list_table[len(list_of_items)][max_capacity], val_table[len(list_of_items)][max_capacity]
