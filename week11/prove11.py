with open ("life_expectancy.csv") as life_expectancy: #opens and closes the text file
    for line in life_expectancy:
        parts = line.split(",") # divides it into parts
        
        entity = parts[0] #entity
        code = parts[1] #code
        year = parts[2] #year
        life_expec = parts[3] #year
        
        print(f"{entity},{code},{year},{life_expec.strip()}") 
        
user_choice = input("Enter the year of interest: ")

max_expect= -1

        if life_expec > max_expect:
            max_expect = life_expec

        print(f"The overall max life expectancy is: {max_expect} from {entity} in {year}")
    
    
min_expect=100000

        if life_expec < min_expect
            min_expect = life_expec

        print(f"The overall min life expectancy is: {min_expect} from {entity} in {year}")

print(f"For the year {user_choice}")
    
    avg= mean(life_expec)
    print("The average life expectancy across all countries was", round(avg,2))

    print(f"The max life expectancy was in {entity}with {life_expec}")
    print(f"The min life expectancy was in {entity} with {life_expec}")
