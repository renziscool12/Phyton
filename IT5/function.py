#def message():
#    print('I love Python Programming')

#message()

#def message2(string):
#    print(string + 'I love Python Programming')

#message2('I need to study Python because ')
#message2('I need to Python Tutorial because ')   

# function should be only used once
#def person(name, gender):
#    name = input('Enter name: ')
#    gender = input('Enter gender: ')
#    print(name, gender)

#person(name = " ", gender = " ")

#def add(x, y):
#    print(f'arguments are {x} and {y}')
#    return x + y

#print(add(5, 6))
#print(add(10, 20))
#print(add(29, 30))

#def describe_pet(name, animal_type):
#   print(f"I have a {animal_type} and its name is {name}")

#describe_pet(name ="jal", animal_type = "dog")    

#args would become a tuple
#def print_numbers(*args):
#    for num in args:
#        print(num, end = " ")
#       print(args)

#print_numbers('orange', 'apple', 'grapes', 'kiwi')

#kwargs would become a dictionary

#def print_info(**kwargs):
#    for key, value in kwargs.items():
#        print(f"{key}: {value}")
               
#print_info(name='Jal', age=19, state='Bago Oshiro')

#def full_example(a,b, *args, **kwargs):
#    print("a:", a)
#    print("b:", b)
#    print("args:", args)
#    print("kwargs:", kwargs)

#full_example(1, 2, 3, 4, 5, name='Jal', job='Unemployed')    

#def example(a, b, c, d, *args, **kwargs):
#    print("1: ", a)
#    print("2: ", b)
#    print("3: ", c)
#    print("4: ", d)
#    print(args)
#    print(kwargs)

#example('Jal', 'Virchie', 'John Vicent', 'Casper', 6,5,4,4, petname='Scooby', dogtype='Italian Greyhound', birth='March')
