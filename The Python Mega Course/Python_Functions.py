def minutes_to_hours(minutes):
    try:
        hours = minutes / 60
        return hours
    except Exception as e:
        return e.args


print(minutes_to_hours(12))


def walberth_hours(minutes, seconds):
    try:
        hours = minutes / 60 + seconds / 3600
        return print(hours)
    except Exception as e:
        return print(e.args)


walberth_hours(50, 2)


def walberth_predefine_hours(seconds, minutes=70):  # Function with default arguments
    try:
        hours = minutes / 60 + seconds / 3600
        return print(hours)
    except Exception as e:
        return print(e.args)


walberth_predefine_hours(50, 25000)


def request_age():
    try:
        age = input("Enter your age: ")
        new_age = int(age) + 50
        return print("Your age in 50 years {} ".format(new_age))
    except Exception as e:
        return print(e.args)


request_age()


#  Function to convert celsius to Fahrenheit
def celsius_fahrenheit(grades):
    try:
        return (grades * 9 / 5) + 32
    except Exception as e:
        return e.args


print(celsius_fahrenheit(10))


#  Function that count the length of one string
def string_length(string):
    try:
        return len(str(string))
    except Exception as e:
        return e.args


print(string_length("Walberth"))