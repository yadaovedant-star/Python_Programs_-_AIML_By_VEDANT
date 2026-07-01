# Q6. Random Module

import random

# Generate and print 5 random integers between 1 and 100
print("Five random integers between 1 and 100:")
for i in range(5):
    print(random.randint(1, 100))   # randint → integer between 1 and 100

# Generate and print one random integer between 50 and 150
print("\nOne random integer between 50 and 150:")
print(random.randint(50, 150))      

# Print a random floating point number between 0 and 1
print("\nRandom floating point number between 0 and 1:")
print(random.random())              # random() → float between 0 and 1
