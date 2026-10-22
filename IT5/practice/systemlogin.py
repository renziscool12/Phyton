username = "jaladmin123"
password = "roxxane123"

print('---System Login---')

while True:
    attemptuser = input("Username: ")
    attemptpass = input("Password: ")

    if attemptuser == username and attemptpass:
        print("Welcome, ", attemptuser)
        break
    else:
        print("try again!")
