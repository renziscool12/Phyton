def mart():
    print("---Mini Mart---\n")
    print("1. Bread - $35")
    print("2. Milk - $25")
    print("3. Water - $10")
    print("4. Instant Noodles - $50")
    print("5. Love Ryo Yamada - $0")
    print("6. Exit\n")

def total_price(item, quantity):
    if item == 1:
        price = 35
    elif item == 2:
        price = 25
    elif item == 3:
        price = 10
    elif item == 4:
        price = 50
    elif item == 5:
        price = 0
    else:
        price = 0
    return price * quantity

def main():
    mart()
    while True:
       item = int(input("Enter the item number (1-6): "))
       if item == 6:
              print("Thank you for shopping with us!")
              break
       if item == 5:
           print("You'll think Ryo Yamada would love you back? She's jsut a fictional character, you know? What a Loser \n")
           break
       quantity = int(input("Enter the quantity: "))
       total = total_price(item, quantity)
       print("Total price: $" + str(total) + "\nQuantity: " + str(quantity) + "\nItem number: " + str(item) + "\n")

main()
