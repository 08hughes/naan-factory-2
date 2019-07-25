def make_dough(ingredient1, ingredient2):
    if ingredient1 == "wheat" and ingredient2 == "water" or ingredient2 == "wheat" and ingredient1 == "water":
        return "dough"
    else:
        return "none"


def bake_dough(dough):
    if dough == "dough":
        return "naan"
    else:
        return "none"

def package_naan(naan):
    if naan == "naan":
        return "Ready to sell"
    else:
        return "none"