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
    second_part = word[n+1:]
    final_word = first_part + second_part
    return final_word


print(remove_char('Python', 3))

# WAF THAT COUNTS THE NUMBER OF OCCURENCES OF EACH WORD IN A SENTENCE
