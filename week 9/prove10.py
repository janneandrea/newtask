 #welcome to the user
print("Welcome to the Shopping cart Program!")

#Set lists
action =""
cart =[]
prices = []

#Menu
while action is != "5":
Print("Please choose one of the following options:"/n)
print("1.Add a new item")
print("2.Display the contents of the shopping cart")
print("3.Remove an item")
print("4.Compute the total")
print("5.Quit")

action =("Please enter an action: ")

# Add several items
    if action =="1"
       add_items = input("What item would you like to add? ")
       items.append(add_items)
       print(f"{add_items}has been added to the cart.")

# Display items
    if action =="2"
       print(f"{display_items}The contents of the shopping cart are: ")
       display_items = input("The contents of the shopping cart are: ")
       for i in range (len(cart)):
       cart =[]
       prices = []
       print("f{i+1} ") #Python starts counting at zero

#Remove items
    if action =="3"
       remove_items = input("What item would you like to remove? ")
       items.pop(remove_items)
       print(f"{remove_items} has been removed.")

# Show total
    if action =="4"



#quit
    if action =="5"
    print("Thank you. Goodbye.")