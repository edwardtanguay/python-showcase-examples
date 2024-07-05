from tools import separator, section

# set items are unchangable
# but you can remove and add items
# sets are unordered, you can't be guaranteed in which order they will appear

plants = {
    "Rose",
    "Lily",
    "Fern",
    "Sunflower",
    "Cactus",
	"Rose"
}

section('notice no duplicates')
print(plants) # second "Rose" not added
plants.add("Tulip") # will add
plants.add("Fern") # will not add
print(plants)

section('add another set')
newPlants = {"Peony", "Daisy"}
print(plants)
plants.update(newPlants)
print(plants)
