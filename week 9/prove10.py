 #welcome to the user
print("Welcome to the Shopping cart Program!")

#Set lists
cart =[]
prices = []
i=0

#Menu
while action is !="5":
    print("Please choose one of the following options:"/n)
    print("1.Add a new item")
    print("2.Display the contents of the shopping cart")
    print("3.Remove an item")
    print("4.Compute the total")
    print("5.Quit")

action = input("Please enter an action: 1,2,3,4,5 "/n)

# Add several items
    if action =="1"
       add_items = input("What item would you like to add? ")
       items.append(add_items)
       print(f"{add_items}has been added to the cart."/n)

# Display items
    elif action =="2"
       print(f"{display_items}The contents of the shopping cart are: ")
       for i in range (len(cart)):
       cart =[]
       prices = []
       print(f"-{i+1},{item}, ${price}.2f") #Python starts counting at zero. Number of item, item, price.

#Remove items
    elif action =="3"
       remove_items = input("What item would you like to remove? ")
       items.pop(remove_items)
       print(f"{remove_items} has been removed.")

# Show total
    elif action =="4"
       for item in price:
       total = total + price  
       print(total)

#quit
     elif action =="5"
        print("Thank you. Goodbye.")