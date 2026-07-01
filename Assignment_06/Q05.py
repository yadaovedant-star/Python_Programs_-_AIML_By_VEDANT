# Program: append() and insert()

# Start with an empty list
cities = []

# Take user input for 2 cities
city1 = input("Enter first city: ")
city2 = input("Enter second city: ")

# Add them using append()
cities.append(city1)
cities.append(city2)

# Add 3 more cities directly
cities.append("Mumbai")
cities.append("Delhi")
cities.append("Pune")

# Insert one more city at position 2 (index 1)
cities.insert(1, "Nagpur")

# Print final list
print("Final list of cities:", cities)
