 #welcome to the user
print("Welcome to the Shopping cart Program!")

#Set lists
cart =[]
prices = []
i=0

#Menu
while action is != "none":
Print("Please choose one of the following options:"/n)
print("1.Add a new item")
print("2.Display the contents of the shopping cart")
print("3.Remove an item")
print("4.Compute the total")
print("5.Quit")

action =("Please enter an action: "/n)

# Add several items
    elif action =="1"
       add_items = input("What item would you like to add? ")
       items.append(add_items)
       print(f"{add_items}has been added to the cart."/n)

# Display items
    elif action =="2"
       print(f"{display_items}The contents of the shopping cart are: ")
       for i in range (len(cart)):
       cart =[]
       prices = []
       print(f"{i+1},{item}, {price}") #Python starts counting at zero. Number of item, item, price.

#Remove items
    elif action =="3"
       remove_items = input("What item would you like to remove? ")
       items.pop(remove_items)
       print(f"{remove_items} has been removed.")

# Show total
    elsif action =="4"
    total = sum(price * item )
    print(f"The total price of the items in the shopping cart is: ${total}")

#quit
    else:
    print("Thank you. Goodbye.")