thisFruits = {'apple', 'banana', 'cherry'}
#thisFruits.add('orange')
#thisFruits.add('orange')
#thisFruits.add('orange')
#print(thisFruits)

#Sets cannot be duplicated values
#hash set

#thisFruits.update(['orange', 'mango', 'grapes'])
#print(thisFruits)

#Database -> list -> set -> tuples

#remove an item in a set, either remove() or discard() method
#thisFruits.remove("banana")
#print(thisFruits)

#thisFruits.discard("banana")
#print(thisFruits)

#NOTE: If the item to remove does not exist, remove() will raise an error. Or you can use discard(), which will not raise an error.

#pop to remove an item in a set if no specific item is specified it will pop the last value.
#thisFruits.pop()
#print(thisFruits)

#union() method returns a new set with all items from both sets
#output: random order
#set1 = {"a", "b", "c"}
#set2 = {1, 2, 3}
#set3 = set1.union(set2)
#print(set3)

# can change value and key in a dictionary switch the value and key in a dictionary
#fruits = {"apple": 1, "banana": 2, "cherry": 3}
#for value, key in fruits.items():
#    print(key, value)

# loops 1, 2 ,3 and prints it using loop
#my_list = [1,2,3]
#new_list = [x*2 for x in my_list]
#print(new_list)

#my_list = [1,2,3,4,5]
#new_list = [x for x in my_list if x % 2==0]
#print(new_list)

#fruits = {"apple,": 1, "banana": 2, "cherry": 3}
#new_fruits = {key: value*2 for key, value in fruits.items()}
#print(new_fruits)

#Deconstruction of tuples
#my_tuple = (1,2,3)
#a,b,c = my_tuple
#print(c,b,a)
