"""
Class patterns.


Using `Class()` and `Class(x=y, ...)` contructs
to match a type and attributes.
"""

from dataclasses import dataclass


class Foo:
    ...


@dataclass
class Bar:
    x: int = 1


def class_match(data):
    match data:
        case Foo():
            print("A. Got Foo object")
        case Bar(x=2):
            print("B. Got Bar with x=2")
        case Bar():
            print("C. Got Bar object")
        case str():
            print("D: Got a string")
        case int():
            print("E: Got an int")
        case _:
            print("Got something else")


class_match(Foo())
class_match(Bar(x=2))
class_match(Bar(x=1))
class_match("string")
class_match(5)

# Note that `case Class()` bits
# are not instantiating anything.

# `case Class()` checks if a subject
# is an instance of `Class`

# `case Class(x=y)` additionally checks
# if a subject has attribute `x`
# and its value is `y`.
