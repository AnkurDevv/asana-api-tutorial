# functions takes a list of words and returns the longest one
def longestWord(wordList):
    longest = []
    for word in wordList:
        longest.append((len(word), word))
        longest.sort()
    return longest[-1][1]


print(longestWord(["PHP", "Exerci", "Backend"]))

# function that removes the nth character from the string


def remove_char(word, n):
    first_part = word[:n]
    print(first_part)


print(remove_char('Python', 3))
