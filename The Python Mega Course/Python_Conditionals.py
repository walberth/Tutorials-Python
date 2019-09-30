#  Conditionals
a = 5 #input("Insert a number please: ")

if int(a) < 5:
    print("The value is less than 5")
elif int(a) == 5:
    print("The value is equal to 5")
else:
    print("The value is greater than 5")


#  Function that count the length of one string version two
def string_length_v2(string):
    try:
        if type(string) == int:
            return "Sorry integers don't have length"
        elif type(string) == float:
            return "Sorry float don't have length too"
        else:
            return len(str(string))
    except Exception as e:
        return e.args

print(string_length_v2(1.0))


#  Function to convert celsius to Fahrenheit version two
def celsius_fahrenheit_v2(grades):
    try:
        if(float(grades) < -273.15):
            return "That temperature is impossible"
        else:
            return (grades * 9 / 5) + 32
    except Exception as e:
        return e.args


print(celsius_fahrenheit_v2(-30))