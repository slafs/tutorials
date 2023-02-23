"""
Value patterns (case ATTR.NAME).
"""

from enum import Enum


class E(int, Enum):
    zero = 0


class C:
    one = 1
    two = 2


c = C()


def value_match(data):
    match data:
        case E.zero:
            print("Got zero")
        case c.one:
            print("Got one")
        case C.two:
            print("Got two")
        case x:
            print(f"Got something else {x=}")


value_match(0)
value_match(1)
value_match(2)
value_match(3)

# When the same value pattern occurs multiple times
# in the same match statement,
# the interpreter may cache the first value found
# and reuse it,
# rather than repeat the same lookup.
#
# This cache is strictly tied to a given execution
# of a given match statement.
