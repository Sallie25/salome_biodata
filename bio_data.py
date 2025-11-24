flag = True                     # Controls the loop; stays True until manually turned off
count = 10                      # Number of iterations allowed (10 people)
demographics = {}               # Dictionary to store all collected data

while flag:                     # Loop continues while flag is True
  count -= 1                    # Reduce count at the start of each loop

  if count < 1:                 # If count goes below 1, stop the loop
    flag = False


  name = input("Enter your name: ").title()      # Receives and format name

  age = input("Enter your age: ")                # Age received as string
  if not age.isdigit():                          # Check if age is a valid whole number. #This helps us deal with situations where user enters age as a float
        print("Please enter a whole number")
        continue                                 # Skip to next loop iteration if true.

  age = int(age)                                 # Convert age to integer

  # Determine age group based on numeric age value
  if 3 <= age <= 12:
      grouped_age_range = "Child"
  elif 13 <= age <= 19:
      grouped_age_range = "Teenager"
  elif 20 <= age <= 39:
      grouped_age_range = "Young Adult"
  elif 40 <= age <= 64:
      grouped_age_range = "Middle Aged"
  elif age >= 65:
      grouped_age_range = "Senior"
  else:
      grouped_age_range = "Invalid age range"    # Handles ages below 3

  gender =  input("Enter your gender: ").title() # Captures and format gender
 
  individual_info = [age,grouped_age_range,gender]           # Store person's info in a list
  demographics[name] = individual_info           # Save to dictionary using name as the key

