def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:  # Only for the ZeroDivisionError
        return "Zero division have not sense"


print(divide(2, 0))
