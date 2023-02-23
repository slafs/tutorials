"""
Capture pattern (case NAME) to bind subject to a var
"""


def capture_match(data):
    match data:
        case 0:
            print("Got zero")
        case 1:
            print("Got one")
        case x:
            print(f"Got something else {x=}")


capture_match(0)
capture_match(1)
capture_match(2)


# capture patterns are irrefutable

# if `case x:` wouldn't be the last case block
# we'd get:
#
#   SyntaxError:
#     name capture 'x'
#     makes remaining patterns unreachable

# A single underscore `_` is not a capture pattern
# (which is a wildcard pattern)


def capture_match_gotcha(data):
    """
    Can't use a constant variable for matching
    (without `.` - see Value pattern)
    """
    x = 5

    match data:
        case 0:
            print("Got zero")
        case 1:
            print("Got one")
        case x:
            print(f"Got something else {x=}")

    print(f"{x=}")


capture_match_gotcha(0)
capture_match_gotcha(1)
capture_match_gotcha(2)
