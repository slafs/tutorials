"""
OR pattern (|) for creating pattern alternatives
"""


def or_match(data):
    match data:
        case 0 | 1:
            print("Got zero or one")
        case _:
            print("Got something else")


or_match(0)
or_match(1)
or_match(2)

# `|` has a special meaning inside the case block
# i.e. `x | y` doesn't mean `x.__or__(y)`
# as it normally would in Python.
