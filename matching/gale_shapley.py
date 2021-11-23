class ObjectA:
    """first type of object to be matched when running the gale-shapley algorithm"""

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name


class ObjectB:
    """second type of object to be matched when running the gale-shapley algorithm"""

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name


def gale_shapley(preferences_a: dict[ObjectA, list[ObjectB]], preferences_b: dict[ObjectB, list[ObjectA]]) -> \
        dict[ObjectA, ObjectB]:
    """computes a stable matching given a two lists of objects and the preferences
    :param preferences_a: dictionary with all objects_a and the list of their preferences
    :param preferences_b: dictionary with all objects_b and the list of their preferences
    :return: dictionary of the stable matching from objects_b to objects_a
    """
    matching_a = {}
    matching_b = {}
    unmatched_a = list(preferences_a.keys())

    while unmatched_a:
        new_a = unmatched_a[0]
        if not preferences_a[new_a]:
            unmatched_a.remove(new_a)
            continue
        potential_b = preferences_a[new_a].pop(0)
        if potential_b in matching_a.values():
            current_a = matching_b[potential_b]

            if preferences_b[potential_b].index(new_a) > preferences_b[potential_b].index(current_a):
                continue
            matching_a.pop(current_a)
            unmatched_a.append(current_a)

        matching_a[new_a] = potential_b
        matching_b[potential_b] = new_a
        unmatched_a.remove(new_a)
    return matching_a
