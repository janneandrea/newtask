my_list =(1,-2,2,3,-1000,4,5,8,100000)

largest = 0

for value in my_list:

    if value > largest:

        largest = value

print(f"The largest is {largest}")