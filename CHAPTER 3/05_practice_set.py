# Question 1
name = input("Enter your name: ")
print("Good Afternoon", name)

# Question 2
letter = '''
Dear <|Name|>,

You are selected!

Date: <|Date|>
'''

print(letter.replace("<|Name|>", "Abbad").replace("<|Date|>", "14 July 2026"))

# Question 3
name = "Abbad  Aiser"
print(name.find("  "))   # Finds double spaces

# Question 4
name = "Abbad  Aiser"
print(name.replace("  ", " "))

# Question 5
letter = "Dear Abbad,\n\tThis Python course is nice.\nThanks!"
print(letter)
