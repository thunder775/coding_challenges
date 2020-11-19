def diceGame(rolls):
    sum = 0;
    for [dice1, dice2] in rolls:
        if dice2 == dice1:
            sum = 0
        else:
            sum += dice2 + dice1
    return sum


print(diceGame([[1, 2], [3, 4], [5, 6]]))
# // should
# return 21

print(diceGame([[5, 6], [6, 4], [1, 1]]))
# // should
# return 0

print(diceGame([[4, 5], [4, 5], [4, 5]]))
# // should
# return 27


vovels = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1, }


def countVowels(word):
    vowelCount = 0
    for char in word.lower():
        vowelCount += vovels.get(char, 0)
    print(vowelCount)
    return vowelCount


countVowels("Celebration")
# // should return 5

countVowels("Palm")
# // should return 1

countVowels("Prediction")
# // should return 4
