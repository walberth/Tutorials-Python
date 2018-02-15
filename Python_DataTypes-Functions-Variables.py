# Variables
#_greeting = "Hello"
#print(_greeting)

#_greetingTWo = input("Hello wabe.. Please write a name: ")
#print(_greetingTWo)

# Data Types
#print("The type of _greetingTwo is: " + str(type(_greetingTWo)))

# Converting types
#age = input("Enter your age: ")
#new_age = int(age) + 50
#print(new_age)

# String
c = "Walberth"
print(c.replace("a", "i", 1))  # Replace the first occurrence of thr letter selected in one particular string
print(c.upper())  # Upper all letter in word

# Get help
help("".replace)  # Get help for the replace build function

# Indexing
variable = "Hi There wal!"
print(variable[0])
print(variable[-1])
print(variable[0:2])
print(variable[:3])
print(variable[3:])
print(variable[-3:-1])

# Lists
listValues = ["Walberth", 24, "Hello"]
print(listValues[0] + " " + listValues[2])
print(type(listValues[1]))
listValues.append(5)
print(listValues)
listValues.remove(24)

# Tuples: Are inmutables
tupl = ("Hello", "Walberth", 3, 4)
print(tupl)

# Dictionaries
listDictionaries = {"Name":"Walberth", "SurName":"Felipe", "FatherLastname":"Gutierrez", "MotherLastname":"Telles"}
print(listDictionaries["SurName"])
print(listDictionaries)
listDict = {"Name":"Walberth", "Cities":("Lima", "HUancayo", "Loreto")}
print(listDictionaries["Name"] + " live in " + listDict["Cities"][0])

s = "Python is fun"
print(s[7:9])

# Syntax Error
