import post
import req
import json
from collections import Counter
start = 0
start_data = req.get_data("03")
print(start_data)


letters = start_data["letters"]
letters = str(letters).lower()

buchstaben = Counter(letters)

search_word = start_data["searchPhrase"]
search_word = str(search_word).lower()

word = Counter(search_word)

possible = []

for letter in word:
    if letter in buchstaben:
        possible.append(buchstaben[letter] // word[letter])
    else:
        possible.append(0)

solution = min(possible)
print(solution)


solutionResult =  post.post_data("03", solution)
print(solutionResult)