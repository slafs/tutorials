"""
__match_args__ property.

For matching with `Class(x, y, ...)`
"""

from dataclasses import dataclass


@dataclass
class Point:
    __match_args__ = ("x", "y")
    x: int = 0
    y: int = 0


def class_match2(data):
    match data:
        case Point(x=x, y=y) if x == y:
            print("A. X=Y: {x}")
        case Point(x, y=0):
            print(f"B. Y=0, {x=}")
        case Point(0):
            print("C. X=0")
        case Point(x, y):
            print(f"D. Got a Point object {x=} {y=}")
        case _:
            print("E. Got something else")


class_match2(Point(2, 2))
class_match2(Point(2, 0))
class_match2(Point(0, 2))
class_match2(Point(3, 4))
