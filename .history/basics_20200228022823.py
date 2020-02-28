def longestWord(wordList):
    longest = []
    for word in wordList:
        longest.append((len(word), word))
        longest.sort()

    print(longest)


longestWord(["PHP", "Exercises", "Backend"])
