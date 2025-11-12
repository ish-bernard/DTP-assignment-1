a = float(input("Enter the first number: "))  # Get first number from user
b = float(input("Enter the second number: ")) # Get second number from user

if a > b:
    print(f"{a} is greater than {b}")
elif b>a:
    print(f"{b} is greater than {a}")
else:
    print("The numbers are equal")