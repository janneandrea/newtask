 #welcome to the user
print("Welcome to the Shopping cart Program!")

#Set lists
cart =[]
prices = []
action= ""
i=0

#Menu
while action !="5":
    print("Please choose one of the following options:")
    print("1.Add a new item")
    print("2.Display the contents of the shopping cart")
    print("3.Remove an item")
    print("4.Compute the total")
    print("5.Quit")
    
    action = int(input("Please enter an action: "))

# Add several items
    if action =="1":
       add_items = input("What item would you like to add? ")
       items.append(add_items)
       print(f"{add_items}has been added to the cart.")

# Display items
    elif action =="2":
        cart =[]
        prices = []
        for i in range (len(cart)):
            print(f"{i+1},{item}, ${price}.2f") #Python starts counting at zero. Number of item, item, price.

#Remove items
    elif action =="3":
       remove_items = input("What item would you like to remove? ")
       items.pop(remove_items)
       print(f"{remove_items} has been removed.")

# Show total
    elif action =="4":
        for item in price:
            total += item  
            print(total)

#quit
    elif action =="5":
        print("Thank you. Goodbye.")