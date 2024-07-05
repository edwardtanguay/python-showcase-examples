from tools import separator, section

colors = ["red", "black", "blue", "green", "yellow"]

section('len')
print(f"There are {len(colors)} colors.")

section('various types')
items = ["abc", 34, True, 40, "male"]
print(f"The third item is of type: {type(items[2])}")
separator()
for item in items:
	print(f"Value {item} is of type: {type(item)}")

section('last item')
print(f"the last item is {colors[-1]}")

section('range')
print(f"items with index numbers 1-3: {colors[1:4]}") # last index number is not included
print(f"from second to end: {colors[1:]}")
print(f"first three: {colors[:3]}") # last index number is not included

section('if included')
searchColor = 'purple'
if searchColor in colors:
	print(f'{searchColor} is in list')
else:
	print(f'{searchColor} NOT in list')

section('replace items')
scores = [10,11,0,0,14]
print(scores)
scores[2:4] = [12,13]
print(scores)

section('insert')
ages = [34,35,36,38,39]
print(ages)
ages.insert(3, 37)
print(ages)