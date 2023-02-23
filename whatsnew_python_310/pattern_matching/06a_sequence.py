"""
Sequence patterns (case [...] or case (...)).

For matching sequences
e.g. lists or tuples
but not strings, bytes or bytearrays.
"""


def sequence_match(data):
    match data:
        case [0, 1] as x:
            print(f"A. Got {x=}")

        case (0, 1) as y:
            # this will never succeed
            # because the first pattern is the same
            print(f"B. Got {y=}")

        case [0, 1, _] as t:
            print(f"C. Got a 3 element sequence {t=}")

        case [0, 1, a, b] as t:
            print(f"D. 3rd is {a=} and 4th is {b=}")

        case [0, 1, _, _, *rest]:
            print(f"E. Got at least 4 elements {rest=}")

        case [0, *middle, 4]:
            print(f"F. Start: 0 End: 4 and {middle=}")

        case [*start, 4]:
            print(f"G. End: 4 and {start=}")

        case _:
            print("Got something else")


sequence_match([0, 1])
sequence_match((0, 1))

sequence_match([0, 1, 2])
sequence_match([0, 1, 2, 3])
sequence_match([0, 1, 2, 3, 4])

sequence_match([0, 2, 2, 2, 4])
sequence_match([2, 2, 2, 2, 4])


# There is no difference
# if parentheses or square brackets are used
# for sequence patterns (i.e. (...) vs [...] ).
