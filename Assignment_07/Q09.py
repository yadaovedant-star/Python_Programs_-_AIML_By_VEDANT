# Tuple of coordinates
coordinates = (10, 20)

# Trying to change the first element
#coordinates[0] = 99   #ERROR: 'tuple' object does not support item assignment

# Trying to add a new element using append()
#coordinates.append(30)  #ERROR: 'tuple' object has no attribute 'append'

# Correct way: Convert tuple to list, modify, then convert back to tuple
temp_list = list(coordinates)   # Convert tuple → list
temp_list[0] = 99               # Modify first element
temp_list.append(30)            # Add new element
coordinates = tuple(temp_list)  # Convert list → tuple again

print("Modified Tuple:", coordinates)
