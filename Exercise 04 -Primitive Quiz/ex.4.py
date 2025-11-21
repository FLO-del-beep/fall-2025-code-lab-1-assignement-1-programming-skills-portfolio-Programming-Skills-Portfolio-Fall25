Dictionary = {
    'France':'Paris',
    'Germany':'Berlin',
    'Italy':'Rome',
    'Spain':'Madrid',
    'Portugal':'Lisbon',
    'Greece':'Athens',
    'Netherlands':'Amsterdam',
    'Belgium':'Brussels',
    'Philippines':'Manila',
    'China' : 'Beijing'
} #    dictionary of countries and their capitals

for country, capital in Dictionary.items(): #stating what to put on the start 
    answer = input(f"What is the capital of {country}? ") #stating the question

    if answer.strip().lower() == capital.lower(): #Checks if the user answered the correct capital, ignoring capitalization and extra spaces. If they match, the user got the answer right.
        print("Correct!") #runs if the users answer matches the correct capital.
    else: #runs when the answer doesn't match.
        print(f"Wrong! The correct answer is {capital}.") #tells the user their answer was wrong and shows the correct capital.