names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave","John","Ken","Jonathan","Amy","Sasha"]

# Ask the user what name they want to search for
search_term = input("Enter a name to search for: ")

# Flag to track whether the name is found
found = False

# Loop through the list and compare each name
for name in names:
    if name.lower() == search_term.lower():  # ignore capitalization
        found = True
        break

# Print the result
if found:
    print(f"{search_term} was found in the list.")
else:
    print(f"{search_term} was not found in the list.")
