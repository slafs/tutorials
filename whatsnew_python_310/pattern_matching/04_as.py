"""
AS pattern (P as NAME) assign subject to a var.
"""


def as_match(data):
    match data:
        case 0 | 1 as zero_or_one:
            print(f"Got {zero_or_one=}")
        case _:
            print("Got something else")


as_match(0)
as_match(1)
as_match(2)
