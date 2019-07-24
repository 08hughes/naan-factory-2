def make_dough(ingredient1, ingredient2):
    if ingredient1 == "wheat" and ingredient2 == "water" or ingredient2 == "wheat" and ingredient1 == "water":
        return "dough"
    else:
        return "none"
