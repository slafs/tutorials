"""
Mapping pattern (case {...}).

For matching mappings
e.g. dicts or mappingproxy.
"""


def mapping_match(data):
    match data:
        case {"a": a, "b": b} as d:
            print(f"A. {a=}, {b=}, subject: {d}")

        case {"b": b, **rest} as d:
            print(f"B. {b=}, rest: {rest}")

        case {"c": c, **rest} if len(rest) == 0:
            print(f"C: got only {c=}")

        case _:
            print("D. Got something else")


mapping_match({"a": 1, "b": 2})
mapping_match({"a": 1, "b": 2, "c": 3})

mapping_match({"b": 1})

mapping_match({"c": 3})

mapping_match({"c": 3, "d": 4})


# Unlike with sequence patterns
# additional key-value items on the subject
# are ignored by default.

# Unless you put a guard with the **rest.

# Note that `**_` is not supported
# (and not needed if you think about it).
