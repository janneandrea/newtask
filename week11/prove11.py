with open ("life_expectancy.csv") as life_expectancy: #opens and closes the text file
     for line in life_expectancy:
        parts = line.split(",") # divides it into parts
        
        entity = parts[0] #entity
        code = parts[1] #code
        year = parts[2] #year
        life_expec = parts[3] #year
        
        print(f"{entity},{code},{year},{life_expec.strip()}") 
        
user_choice = input("Enter the year of interest: ")

print(f"The overall max life expectancy is: max{life_expec} from {entity} in {year}")
print(f"The overall min life expectancy is: min{life_expec} from {entity} in {year}")

print(f"For the year {user_choice}")
print(f"The average life expectancy across all countries was {}")
print(f"The max life expectancy was in {entity}with {life_expec}")
print(f"The min life expectancy was in {entity} with {life_expec}")
