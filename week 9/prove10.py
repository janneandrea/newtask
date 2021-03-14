 #welcome to the user
print("\nWelcome to the Shopping cart Program!")

#Set lists
cart =[]
prices = []
action= ""
price= ""
item=""
i=0

#Menu
while action !="5":
    print("\nPlease choose one of the following options:")
    print("\n1.Add a new item")
    print("2.Display the contents of the shopping cart")
    print("3.Remove an item")
    print("4.Compute the total")
    print("5.Quit")
    print("6.Clear cart")
    action = input("Please enter an action: ")

# Add several items
    if action =="1":
       add_items = input("What item would you like to add?")
       price_items=input(f"What is the price of {add_items}?")
       cart.append(add_items)
       print(f"{add_items} has been added to the cart.")

# Display items
    elif action =="2":
        for item in cart (len(item)):
            print(f"{i+1},{add_items}, ${price_items}") #Python starts counting at zero. Number of item, item, price.

#Remove items
    elif action =="3":
       remove_items=input("What item would you like to remove?")
       cart.pop(remove_items)
       print(f"{remove_items} has been removed.")

# Show total
    elif action =="4":
        for item in prices:
            total += item  
            print(total)

#quit
    elif action =="5":
        print("Thank you. Goodbye.")

#clear entire cart
    elif action =="6":
	    cart.clear( add_items,price_items)
	    print("Your cart has been emptied")