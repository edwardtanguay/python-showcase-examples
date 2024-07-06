from tools import separator, section

section('arguments')
def getFullName(first, last):
  return f"{first} {last}"

fullName = getFullName("Roger", "Gargoyle")
print(fullName)

section('arbitrary number of arguments')
def printInfos(*infos):
  print(f"The argument is a {type(infos)}.")
  print(infos)
  print(f"There are {len(infos)} infos.")
  for i,info in enumerate(infos):
    print(f"{i+1}. {info}")

printInfos('rock', 'tree')
