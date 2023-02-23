"""
Literal pattern.
"""


def literal_match(data):
    match data:  # data is a SUBJECT
        case "a string":  # "a string" is a (literal) PATTERN
            print("Got a string")
        case True:
            print("Got True")
        case False:
            print("Got False")
        case None:
            print("Got None")
        case 0:
            print("Got zero")
        case 1:
            print("Got one")


literal_match("a string")
literal_match(True)
literal_match(False)
literal_match(None)
literal_match(0)
literal_match(1)
