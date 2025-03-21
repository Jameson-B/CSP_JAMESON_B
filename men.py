# Men Python

import random


# Assignment Instructions:
# 
# Build a game! With your team (of 4 people) you need to build a game that will be run completely out of the console. Your game must include:
# 
# 1 variable 
# 2 Functions
# 1 conditional
# 1 loop
print("Welcome to Hang Men!")
# Robert N: Art.
print("_______")
print(" |    |")
print("      |")
print("      |")
print("      |")
print("      |")
print("      |")
# David Garcia 
import random  
  
word_list = ["ABACK", "ABASE", "ABATE", "ABBEY", "ABIDE", "ABOUT", "ABOVE", "ABYSS", "ACORN", "ACRID", "ACTOR", "ACUTE", "ADAGE", "ADAPT", "ADMIT", "ADOBE", "ADOPT", "ADORE", "ADULT", "AFFIX", "AFTER", "AGAIN", "AGAPE", "AGATE", "AGENT", "AGILE", "AGING", "AGLOW", "AGONY", "AGREE", "AHEAD", "AISLE", "ALBUM", "ALERT", "ALIEN", "ALIKE", "ALIVE", "ALLOW", "ALOFT", "ALONE", "ALOOF", "ALOUD", "ALPHA", "ALTAR", "ALTER", "AMASS", "AMBER", "AMISS", "AMPLE", "ANGEL", "ANGER", "ANGRY", "ANGST", "ANODE", "ANTIC", "ANVIL", "AORTA", "APART", "APHID", "APPLE", "APPLY", "APRON", "APTLY", "ARBOR", "ARDOR", "ARGUE", "AROMA", "ASCOT", "ASIDE", "ASKEW", "ASSET", "ATLAS", "ATOLL", "ATONE", "AUDIO", "AUDIT", "AVAIL", "AVERT", "AWAIT", "AWAKE", "AWARD", "AWASH", "AWFUL", "AXIOM", "AZURE", "BACON", "BADGE", "BADLY", "BAGEL", "BAKER", "BALSA", "BANAL", "BARGE", "BASIC", "BASIN", "BASTE", "BATHE", "BATON", "BATTY", "BAWDY", "BAYOU", "BEACH", "BEADY", "BEAST", "BEAUT", "BEEFY", "BEGET", "BEGIN", "BEING", "BELCH", "BELIE", "BELLY", "BELOW", "BENCH", "BERET", "BERTH", "BESET", "BEVEL", "BINGE", "BIOME", "BIRCH", "BIRTH", "BLACK", "BLADE", "BLAME", "BLAND", "BLARE", "BLAZE", "BLEAK", "BLEED", "BLEEP", "BLIMP", "BLOCK", "BLOKE", "BLOND", "BLOWN", "BLUFF", "BLURB", "BLURT", "BLUSH", "BOAST"] 
hang = random.choice(word_list)  
guessed_letters = []  
attempts = 6  
  
while attempts > 0:  
 
    a = ''.join([letter if letter in guessed_letters else '_' for letter in hang])  
    print(a)  
  
    guess = input("Guess a letter: ").upper()  
    
    

    if guess in hang:  
        guessed_letters.append(guess)  
        print("Good guess!")  
    else:  
        attempts -= 1  
        print("Wrong guess! Attempts left:", attempts)  
      
    if all(letter in guessed_letters for letter in hang):  
        print("Congratulations! You've guessed the word:", hang)  
        break  
else:  
    print("Sorry! The word was:", hang)  

# Robert N: Art.

#print(________)
#print(" |    |")
#print("🙁   |")
#print("      |")
#print("      |")
#print("      |")

#print(________)
#print(" |    |")
#print("🙁   |")
#print(" |    |")
#print("      |")
#print("      |")

#print(________)
#print(" |    |")
#print("🙁   |")
#print(" |    |")
#print("  \   |")
#print("      |")

#print(________)
#print(" |    |")
#print("🙁   |")
#print(" |    |")
#print("/\    |")
#print("      |")

#print(________)
#print(" |    |")
#print("🙁   |")
#print(" |\    |")
#print("/\    |")
#print("      |")

#print(________)
#print(" |    |")
#print("💀   |")
#print("/|\   |")
#print("/\    |")
#print("      |")


#print(""Here Lies your guess"")
#print(f"{correct_word} 🪦 2025-2025")



# Jameson B: Handle user inputs.
    #1. Define variables and functions.
        # Word list (str, list)
        # Correct word (str)
correct_word = random.choice(word_list)
print(correct_word)
        # Correct word length (int)
        # Letter guess (str)
        # Word guess (str)
        # Word guess length (int)
         
    #2. Print user instructions.

guess = input("Guess one letter:\n")
    #3. Computations.
    #4. Output.
    #5. Repeat.
# David G: Compiling word list, random word selector.

nap_time = "now"
me = "tired"
urmom= "funnt"

# Jasper Holt: outputs letter check, 

# find if the letter is in the word, find tcharecter(s) it is, change the charecter in the hang man.make if statments for if the letter is corect. put the letter in the word if the letter if true if flase tell the image to add a body part. 
#if letter = (any of the letters in the word)
print(len(hang))