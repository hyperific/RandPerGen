import random as r
def get():
    first = ["I", "E"]
    second = ["N", "S"]
    third = ["T", "F"]
    fourth = ["P", "J"]
    pers = r.choice(first) + r.choice(second) + r.choice(third) + r.choice(fourth)
    return pers
