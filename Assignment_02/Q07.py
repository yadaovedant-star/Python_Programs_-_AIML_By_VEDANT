# Q7. Program to give advice based on temperature and rain using nested if

# Take inputs from the user
temperature = int(input("Enter the temperature (in °C): "))
is_raining = input("Is it raining? (yes/no): ")

# Outer if for temperature condition
if temperature > 30:
    # Inner if for rain condition
    if is_raining == "no":
        print("Hot day, wear light clothes.")
    else:
        print("Hot and rainy, carry umbrella.")

elif temperature < 15:
    # Inner if for rain condition
    if is_raining == "yes":
        print("Cold and rainy, wear jacket and take umbrella.")
    else:
        print("Cold day, wear warm clothes.")

else:
    # Suitable message for other cases
    print("Weather is moderate, dress comfortably.")
