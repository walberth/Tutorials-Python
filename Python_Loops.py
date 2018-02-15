#  Loops: for
emails = ['w.felipe.gutierrez@gmail.com', 'walberth.gutierrez@gmail.com', 'walberth_gutierrez@outlook.com']

for email in emails:
    if 'gmail' in email:
        print(email)

name = "Walberth"

for letter in name[0:]:
    print(letter)

mylist = [1, 2, 3, 4, 5]

for number in mylist:
    if number > 2:
        print(number)

names = ['walberth', 'felipe', 'pepe', 'juancho']
email_test = ['w.felipe.gutierrez@gmail.com', 'walberth.gutierrez@gmail.com', 'walberth_gutierrez@outlook.com']

for i, j in zip(names, email_test):  # Iterate in multiple list
    print(i, j)

#  Loops: while
password = ''
while password != '1234':
    password = input("Please enter the password: ")
    if password == '1234':
        print("Hi, you are logged in!")
    else:
        print("Invalid credentials")


#  Exercises
def celsius_fahrenheit_v3(grades):
    try:
        if (float(grades) < -273.15):
            return "That temperature is impossible"
        else:
            return (grades * 9 / 5) + 32
    except Exception as e:
        return e.args


def evaluating(temperatureLis1t):
    for grades in listValues:
        print(celsius_fahrenheit_v3(grades))


listValues = [10, -20, -280, 100]

evaluating(listValues)
