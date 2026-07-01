# Demonstrating different import methods with math module

# 1. Import the entire math module
import math
print("Using math.pow(2, 4):", math.pow(2, 4))

# 2. Import only sqrt from math
from math import sqrt
print("Using sqrt(16):", sqrt(16))

# 3. Import math with an alias
import math as m
print("Using m.factorial(5):", m.factorial(5))
