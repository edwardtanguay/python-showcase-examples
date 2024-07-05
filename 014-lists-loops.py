from tools import separator, section

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

section('iterate through items like foreach')
for planet in planets:
	print(planet)

section('iterate through items using index')
for i in range(len(planets)):
	print(f"{i+1}. {planets[i]}")