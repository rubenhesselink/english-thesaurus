import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def definition(w):
    w = w.lower()
    if w in data:
        return data[w]

    elif w.title() in data:
        return data[w.title()]

    elif w.upper() in data:
        return data[w.upper()]

    elif len(get_close_matches(w, data.keys())) > 0:

        yn = input("Did you mean %s instead? Enter Y if this is correct, or N if this is incorrect: " % get_close_matches(w, data.keys())[0])
        if yn == "Y" or "y":
            return data[get_close_matches(w, data.keys())[0]]
            
        elif yn == "N" or "n":
            return "The word does not exist!"

        else:
            return "Invalid input, please enter Y or N!"

    else:
        return "The word does not exist!"

word = input("Enter a word: ")

output = definition(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)