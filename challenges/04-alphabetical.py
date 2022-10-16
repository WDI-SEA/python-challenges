# You'll need to use a couple of built in functions to alphabetize a string.
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


def orderWord():
    wordArr = []
    letterIndex = ""

    word = input("Give me a word to alphabetize:\n")

    for k in range(len(word)):
        wordArr.append(word[k])

    for index in range(len(wordArr)):
        for subIndex in range(len(wordArr)):
            if wordArr[index] <= wordArr[subIndex] and index < len(wordArr):
                letterIndex = wordArr[index]
                wordArr[index] = wordArr[subIndex]
                wordArr[subIndex] = letterIndex
            else:
                letterIndex = wordArr[index]
                wordArr[index] = letterIndex

    word = ""
    print(f"Alphabetized: {word.join(wordArr)}")


orderWord()
