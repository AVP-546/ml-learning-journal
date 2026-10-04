##Madlibs Game

def testingStrings(word):
    while not word or len(word.strip()) == 0:
        word = input("\nYou did not enter anything, please try again: ")

adjective = input("Enter an adjective (1)(description): ")
testingStrings(adjective)

adjective2 = input("Enter a second adjective: ")
testingStrings(adjective2)

noun1 = input("Enter a noun: ")
testingStrings(noun1)

verb = input("Enter a verb: ")
testingStrings(verb)

adjective3 = input("Enter a third adjective: ")
testingStrings(adjective3)
print("\n\n\n-----------------------------------")
print(f"Today I want to a {adjective} zoo.\nIn an exhibit, i saw a {noun1}\n{noun1} was {adjective2} and {verb}\nI was {adjective3}!")
print("-----------------------------------\n")