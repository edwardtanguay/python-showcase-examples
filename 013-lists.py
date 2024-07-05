from tools import separator, section

section('len')
colors = ["red", "blue", "green"]
print(f"There are {len(colors)} colors.")

section('various types')
items = ["abc", 34, True, 40, "male"]
print(f"The third item is of type: {type(items[2])}")
separator()
for item in items:
	print(f"Value {item} is of type: {type(item)}")