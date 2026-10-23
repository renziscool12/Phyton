message = "  The secret ingredients in programming is practice  "

# Prints the letter i in index 11
print(message[11])

# Prints every letters into numbers which is 49
print(len(message))

# Prints true if it has the word on the variable
print("secret" in message)

# Slicing if no starting pos it automatically prints where it ends
print(message[3:21])

# Negative index slice string from end always start at the left sentences
print(message[-45:22])

print(message.strip())
print(message.lower())
print(message.upper())

print(message.replace("e", "*"))
print(message.split())

message1 = "Phyton"

# Loop through each letter in the message and print it
for x in str(message1):
    print(x)

# loop through each letter in the message phyton and adds space through it
for y in str(message1):
    print(y, end = " ")
