from tools import separator, section

drinks = [
    "Margarita",
    "Mojito",
    "Old Fashioned",
    "Cosmopolitan",
    "Martini"
]

section("copy list by reference")
drinks2 = drinks
print(drinks)
print(drinks2)
separator()
drinks[2] = "(NONE)"
print(drinks)
print(drinks2)

section("copy list by reference")
drinks3 = drinks.copy()
print(drinks)
print(drinks3)
separator()
drinks[2] = "---"
print(drinks)
print(drinks3)