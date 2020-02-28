def longestWord(wordList):
    longest = []
    for word in wordList:
        longest.append((len(word), word))
        longest.sort()
    return longest[-1][1]


longestWord(["PHP", "Exercises", "Backend"])
