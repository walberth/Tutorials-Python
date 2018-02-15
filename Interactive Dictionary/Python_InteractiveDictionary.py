import json
import difflib

"""First real time project for interactive dictionary reading a json"""

data = json.load(open("/home/walberth/Documents/Python/Interactive Dictionary/data.json"))


def translate(word):
    value = word.lower()

    try:
        if value in data:
            return data[value]
        elif value.title() in data:
            return data[value.title()]
        elif value.upper() in data:
            return data[value.upper()]
        else:
            correct_key = difflib.get_close_matches(value, data.keys())[0]
            correct_value = data[correct_key]

            if len(correct_key) > 0:
                evaluation = input("Did you mean %s instead? Enter Y if yes, or N if no: " % correct_key)
                if evaluation.upper() == "Y":
                    return correct_value
                else:
                    return "The word doesn't exists. Please double check it."
    except Exception as ex:
        return ex.args


word = input("Please enter a word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
