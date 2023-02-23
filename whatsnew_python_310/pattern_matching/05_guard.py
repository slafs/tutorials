"""
Guard (case P if EXPRESSION).
"""

forbid_0 = True


def guard_match(data):
    match data:
        case 0 | 1 as x if not (x == 0 and forbid_0):
            print(f"Got {x=}")
        case _:
            print("Got something else")


guard_match(0)
guard_match(1)
guard_match(2)

# A guard must succeed
# for code inside the case BLOCK to execute.

# The PATTERN is executed _before_ the guard.

# Guard is NOT a pattern.
# Guards are "normal" Python expressions.
# Can have side-effects
# and exceptions from them will "bubble up".
