user_id = "user123"
user_password = "pass123"

id = input("Enter username:")
password = input("Enter password:")

if user_id == id and password == user_password:
    print("Login successful!")
else:
    print("Access denied.")