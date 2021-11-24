class IntervalSchedulingInterval:
    """interval to schedule in interval scheduling"""

    def __init__(self, name: str, start_time: int, end_time: int):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self) -> str:
        return f"{self.name}({self.start_time}, {self.end_time})"


def interval_scheduling(intervals: list[IntervalSchedulingInterval]) -> list[IntervalSchedulingInterval]:
    """computes biggest set of compatible intervals
    :param intervals: all available intervals
    :return: the biggest set of compatible intervals
    """
    sorted_intervals = intervals.copy()
    sorted_intervals.sort(key=lambda i: i.start_time)
    selected_intervals = []
    while sorted_intervals:
        new_interval = sorted_intervals.pop(0)
        selected_intervals.append(new_interval)
        for interval in sorted_intervals:
            if new_interval.start_time <= interval.start_time < new_interval.end_time:
                sorted_intervals.remove(interval)
                continue
            if new_interval.start_time < interval.end_time <= new_interval.end_time:
                sorted_intervals.remove(interval)
                continue
            if interval.start_time < new_interval.start_time and new_interval.end_time < interval.end_time:
                sorted_intervals.remove(interval)

    return selected_intervals
