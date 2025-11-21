---
# Demographic Data Collection Program

##  Overview

This Python program interactively collects demographic information for **10 individuals**. For each person, the user is prompted to enter their **name**, **age**, and **gender**. The program validates the age input, assigns an **age group category**, and stores all the information in a structured dictionary.

The program is useful for small surveys, classroom exercises, beginner Python projects, and demonstrations of loops, validation, and conditional logic.

---

##  Features

* Repeatedly prompts for user input up to 10 times
* Validates age input to ensure it is a whole number
* Automatically assigns an age group:

  * **Child:** 3–12
  * **Teenager:** 13–19
  * **Young Adult:** 20–39
  * **Middle Aged:** 40–64
  * **Senior:** 65+
* Stores each individual’s data in a dictionary using their name as the key
* Gracefully handles invalid age input with `continue`
* Organized and beginner-friendly control-flow logic

---

##  How It Works

1. A loop runs until 10 valid entries are collected.
2. For each iteration:

   * Name is formatted using `.title()`
   * Age is validated using `.isdigit()`
   * Age is converted to an integer
   * An age group is assigned using `if/elif` conditions
   * Gender is collected and formatted
3. Each entry is stored like this:

```python
demographics = {
    "John": [23, "Young Adult", "Male"],
    "Mary": [12, "Child", "Female"],
    ...
}
```

4. The loop stops when 10 valid individuals have been processed.

---

##  Example Output Structure

```python
{
  'Alice': [34, 'Young Adult', 'Female'],
  'David': [10, 'Child', 'Male'],
  'Joy': [67, 'Senior', 'Female']
}
```

---

##  Running the Program

Simply run the Python script in any environment:

```bash
python3 bio_data.py
```

You will then be prompted to enter information for each individual.

---

##  Requirements

* Python 3.x
* No external libraries required

---

##  Educational Concepts Demonstrated

This program helps beginners understand:

* `while` loops
* Counters
* `continue` statements
* Input validation
* Dictionaries
* Lists
* Nested data structures
* Conditional logic
* Title-casing and string handling

---CSV
Just let me know!
