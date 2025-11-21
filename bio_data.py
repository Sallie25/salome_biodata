# Controls the loop; stays True until manually turned off
flag = True 

# Number of iterations allowed (10 people)                    
count = 10    

 # Dictionary to store all collected data                  
demographics = {}              

# Loop continues while flag is True
while flag:  
  
# Reduce count at the start of each loop                  
  count -= 1                    

# If count goes below 1, stop the loop
  if count < 1:                 
    flag = False

# Get and format name
  name = input("Enter your name: ").title()      

# Age received as string
  age = input("Enter your age: ")    

 # Check if age is a valid whole number              
  if not age.isdigit():                         
        print("Please enter a whole number")

        # Skip to next loop iteration if invalid input
        continue    
                               
    # Convert age to integer
  age = int(age)                                 

  # Determine age group based on numeric range
  if 3 <= age <= 12:
      group = "Child"
  elif 13 <= age <= 19:
      group = "Teenager"
  elif 20 <= age <= 39:
      group = "Young Adult"
  elif 40 <= age <= 64:
      group = "Middle Aged"
  elif age >= 65:
      group = "Senior"
  else:
      group = "Invalid age range (too young)"    # Handles ages below 3

  gender =  input("Enter your gender: ").title() # Capture and format gender
 
  individual_info = [age,group,gender]           # Store person's info in a list
  demographics[name] = individual_info           # Save to dictionary using name as the key

