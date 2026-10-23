
#n = int(input("Enter a number: "))

#sum = 0
#ctr = 1

#while ctr <= n:
#    sum = sum + ctr
#    ctr += 1
#print("The sum of the first", n, "numbers is:", sum)

#i = 1
#while i < 6:
#    print(i)
#    if i == 3:
#        break
#    i += 1

#i = 0
#while i < 6:
#    i += 1
#    if 1 == 3:
#        continue
#    print(i)

#i = 1
#while i == 6 :
#   print(i)
#   i += 1
#else:
#   print("i is no longer less than 6")

#numbers = [6,5,3,8,4,2,5,4,11]

#sum = 0
#for val in numbers:
#    sum = sum + val

#print("The sum", sum)

#digits = [0, 5, 10]

#for i in digits:
#    print(i)
#    i += 1
#else:
#    print("No more items")

#for val in "string":
#    if val == "i":
#        break
#    print(val)
#print("The end")

#for val in "string":
#   if val == "i":
#        continue
#    print(val)
#print("the end")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        if y == "cherry" and x == "big":
            print(y,x)
