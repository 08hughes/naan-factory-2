from naan_factory_func import *
# Test 1 - make_dough() input - wheat and water - expected output dough
print("Test 1 - testing func make_dough() with input - wheat and water - expected output dough")
print(make_dough("wheat", "water") == "dough")

# Test 2 make_dough - input = x and y - expected output = "none"
print("Test 2 - testing func make_dough() with input = x and y - expected output = none")
print(make_dough("x", "y") == "none")

# Test 3 - bake_dough() input = dough expected output = "naan"
print("Test 3 - testing func bake_dough() with input = dough expected output = naan")
print(bake_dough("dough") == "naan")

# Test 4 - bake_dough() input = x - expected output = "none"
print("Test 4 - testing func bake_dough() with input = x - expected output = none")
print(bake_dough("x") == "none")

# Test 5 - package_naan() input = naan expected output = "Ready to sell"
print("Test 5 - testing func package_naan() with input = naan expected output = ready to sell")
print(package_naan("naan") == "Ready to sell")

# Test 6 - package_naan() input = x, expected output = none
print("Test 6 - testing func package_naan() with input = x, expected output = none")
print(package_naan("x") == "none")
