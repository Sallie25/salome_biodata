flag = True                     # Controls the loop; stays True until manually turned off
count = 10                      # Number of iterations allowed (10 people)
demographics = {}               # Dictionary to store all collected data

while flag:                     # Loop continues while flag is True
  count -= 1                    # Reduce count at the start of each loop

  if count < 1:                 # If count goes below 1, stop the loop
    flag = False


  name = input("Enter your name: ").title()      # Get and format name

  age = input("Enter your age: ")                # Age received as string
  if not age.isdigit():                          # Check if age is a valid whole number
        print("Please enter a whole number")
        continue                                 # Skip to next loop iteration if invalid input

  age = int(age)                                 # Convert age to integer

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

