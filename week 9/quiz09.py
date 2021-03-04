my_list =(1,-2,2,3,4,5,8,1000)

smallest = 0

for value in my_list:

    if value <= smallest:

        smallest = value

print(f"The smallest is {smallest}")