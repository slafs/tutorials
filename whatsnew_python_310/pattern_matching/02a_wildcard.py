"""
Wildcard pattern (case _)
to capture "everything else"
"""


def wildcard_match(data):
    match data:
        case 0:
            print("Got zero")
        case 1:
            print("Got one")
        case _:
            print("Got something else")


wildcard_match(0)
wildcard_match(1)
wildcard_match(2)

# if `case _:` wouldn't be the last case block
# we'd get:
#
#   SyntaxError:
#     wildcard makes remaining patterns unreachable

# `_` has a special meaning inside the case block

# `case _` is an "Irrefutable Case Block"
# and `_` is an "Irrefutable Pattern"
# i.e. a "match-all" block/pattern,
# that will always succeed.
#
# There are more of those :).
