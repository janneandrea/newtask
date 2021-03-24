with open ("life_expectancy.csv") as life_expectancy: #opens and closes the text file
    for line in life_expectancy:
        parts = line.split(",") # divides it into parts
        
        entity = parts[0] #entity
        code = parts[1] #code
        year = parts[2] #year
        life_expec = float(parts[3]) #year
        
        print(f"{entity},{code},{year},{life_expec.strip()}") 
        
user_choice = input("Enter the year of interest: ")

max_expect = life_expec[3]

for life_expec in life_expec:
    if life_expec > max_expect:
        # This number is larger than the largest we had seen so far

        # So it is now the largest we've seen
        max_expect = life_expec

# Now, after the loop we can display it:
print(f"The largest is: {max_expect}")
