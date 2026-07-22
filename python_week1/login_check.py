username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "python123":
    print("Login successful")
elif username == "admin":
    print("incorrect password")
else: 
    print("Unknown username")