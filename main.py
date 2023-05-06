# Hangman

from time import sleep
import os
from random import randint

listPrompts = [ # List of all the Dynamic Prompts
    "Welcome to Hangman",
    "Are you Excited! ",
    "Great Lets start!",
    "The concept is that we will give you a list of possible outcomes and you need to guess it before the hangman is drawn.",
    "So let's start "
]

for i in listPrompts: # Iterating Over the Prompts
    os.system('cls')
    print(i)
    sleep(3)


# List of all the words
words = [ "abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes", "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle", "bookworm", "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buxom", "buzzard", "buzzing", "buzzwords", "caliph", "cobweb", "cockiness", "croquet", "crypt", "curacao", "cycle", "daiquiri", "dirndl", "disavow", "dizzying", "duplex", "dwarves", "embezzle", "equip", "espionage", "euouae", "exodus", "faking", "fishhook", "fixable", "fjord", "flapjack", "flopping", "fluffiness", "flyby", "foxglove", "frazzled", "frizzled", "fuchsia", "funny", "gabby", "galaxy", "galvanize", "gazebo", "giaour", "gizmo", "glowworm", "glyph", "gnarly", "gnostic", "gossip", "grogginess", "haiku", "haphazard", "hyphen", "iatrogenic", "icebox", "injury", "ivory", "ivy", "jackpot", "jaundice", "jawbreaker", "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging", "joking", "jovial", "joyful", "juicy", "jukebox", "jumbo", "kayak", "kazoo", "keyhole", "khaki", "kilobyte", "kiosk", "kitsch", "kiwifruit", "klutz", "knapsack", "larynx", "lengths", "lucky", "luxury", "lymph", "marquis", "matrix", "megahertz", "microwave", "mnemonic", "mystify", "naphtha", "nightclub", "nowadays", "numbskull", "nymph", "onyx", "ovary", "oxidize", "oxygen", "pajama", "peekaboo", "phlegm", "pixel", "pizazz", "pneumonia", "polka", "pshaw", "psyche", "puppy", "puzzling", "quartz", "queue", "quips", "quixotic", "quiz", "quizzes", "quorum", "razzmatazz", "rhubarb", "rhythm", "rickshaw", "schnapps", "scratch", "shiv", "snazzy", "sphinx", "spritz", "squawk", "staff", "strength", "strengths", "stretch", "stronghold", "stymied", "subway", "swivel", "syndrome", "thriftless", "thumbscrew", "topaz", "transcript", "transgress", "transplant", "triphthong", "twelfth", "twelfths", "unknown", "unworthy", "unzip", "uptown", "vaporize", "vixen", "vodka", "voodoo", "vortex", "voyeurism", "walkway", "waltz", "wave", "wavy", "waxy", "wellspring", "wheezy", "whiskey", "whizzing", "whomever", "wimpy", "witchcraft", "wizard", "woozy", "wristwatch", "wyvern", "xylophone", "yachtsman", "yippee", "yoked", "youthful", "yummy", "zephyr", "zigzag", "zigzagging", "zilch", "zipper", "zodiac", "zombie"]

while(True):

    chosenWord = list(words[randint(0, len(words)-2)])  # This will be the word Chosen from the whole list
    tries = randint(3, len(chosenWord)-1) # Allocating a random number of Tries to the player
    inputWord = [] # This list will be the COllection of all the correct user inputs
    while (True):
        if tries == 0: # If all the tries run out 
            print("OOPS! You ran out of Tries")
            break
        elif sorted(set(inputWord)) == sorted(set(chosenWord)): # In case of a win 
            os.system('cls')
            print("Congrats You got that right! ")
            break
        for i in range(len(chosenWord)):
            print(chosenWord[i] if chosenWord[i] in inputWord else "_", end=" ") # For printing the actual letters in place of dashes for already guessed letters
        print("")
        inputLetter = input("\nEnter a Letter to Start Guess: ")
        posWord = {} # To keep Track of the indexes
        if inputLetter in chosenWord and len(inputLetter) == 1: # To Check if the input is correct.
            inputWord.append(inputLetter)
            posWord[inputLetter] = chosenWord.index(inputLetter)
        else: # If it is not just lessen the tries
            tries -= 1
            os.system('cls')
            print("Sorry Wrong input\n")
    choice = int(input("Do you want to play again, enter 0 or 1 : "))
    if choice == 0:
        break
