"""
Group pattern - using "(" and ")"

Add parentheses around patterns
to emphasize the intended grouping.
"""


def group_pattern(data):
    match data:
        case [(0 | 1), *_, (0 | 1)] as x:
            print(f"Seq that starts and ends with either 0 or 1: {x=}")
        case _:
            print("something else")


group_pattern([0, 1, 2, 3, 2, 1])
group_pattern([0, 1, 2, 3, 2, 1, 0])
group_pattern([1, 2, 3, 4, 3, 2, 1])
group_pattern([1, 2, 3, 2, 1, 0])

group_pattern([1, 2, 3, 2])
group_pattern([2, 3, 2, 1, 0])
group_pattern([2, 3, 2, 1, 0])
