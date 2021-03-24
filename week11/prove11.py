with open ("life_expectancy.csv") as life_expectancy: #opens and closes the text file
     for line in life_expectancy:
        parts = line.split(",") # divides it into parts
        
        entity = parts[0] #entity
        code = parts[1] #code
        year = parts[2] #year
        life_expec = parts[3] #year
        
        print(f"{entity},{code},{year},{life_expec.strip()}") 

        