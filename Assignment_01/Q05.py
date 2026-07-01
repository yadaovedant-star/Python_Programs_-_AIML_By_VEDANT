Your_Name=input("Please enter your name: ")
Your_Birth_Year=int(input("Please enter your birth year: "))
#I converted the input to int because input() gives string, and calculations require numbers
Current_Year=2026
Your_Age=Current_Year-Your_Birth_Year
print("Your current age is:", Your_Age)
print(Your_Name,"Your current age is:", Your_Age)