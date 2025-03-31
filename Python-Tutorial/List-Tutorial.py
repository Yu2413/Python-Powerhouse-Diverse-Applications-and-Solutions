# Tutorial For Lists

# TestList = ["element1","element","element"]

# Testlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Scores = [40.45, 80.6, 90.8, 72.9, 80]
# Numbers 1, 2, 3, 4, 5


print(Scores[-1]) # Last Number

print(Scores[-2]) # Second Last Number

print(Scores[-3]) # Third Last Number

print(Scores[-4]) # Fourth Last Number

print(Scores[-4]) # Fifth Last Number


print(Scores[0])  # First Number

print(Scores[1])  # Second Number

print(Scores[2])  # Third Number

print(Scores[3])  # Fourth Number

print(Scores[4])  # Fifth Number


print(Scores[0:5]) # Numbers 1 to 5

print(Scores[0:4]) # Numbers 1 to 4

print(Scores[0:3]) # Numbers 1 to 3

print(Scores[0:2]) # Numbers 1 to 2

print(Scores[0:1]) # Numbers 1


print(Scores[1:5]) # Numbers 2 to 5

print(Scores[3:5]) # Numbers 4 to 5

print(Scores[2:4]) # Numbers 3 to 4


Scores[0] = 78 # Changed Number 1 to 78

print(Scores)  # Prints list with the above change of 40.45 -> 78.

Scores[0:1] = [] # Deletes the first 2 on the list for the next action.

print(Scores) # Prints list with the above change of no numbers 1, and 2 or 1-2.

Scores[0] = ["Hello", "World"] # Adds words to the beginning of the list

print(Scores) # Prints list with the above change of adding ["Hello", "World"] to the list.

print(Scores[0]) # Prints list with just ["Hello", "World"] in the list.

print(Scores[0][1]) # Prints list with just "World".

print(Scores[0][0]) # Prints list with just "Hello".

Scores.append(95)   # Append Score with 95 to add to it.

print(Scores) # Prints the final score





