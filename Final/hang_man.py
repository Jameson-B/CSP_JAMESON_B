# Hang Man Python

import random

# Assignment Instructions:
# 
# Build a game! With your team (of 4 people) you need to build a game that will be run completely out of the console. Your game must include:
# 
# 1 variable 
# 2 Functions
# 1 conditional
# 1 loop
print('Welcome to our Hang Man game, we hope you enjoy it')
# Robert N: Art.
def print_image():
    if attempts == 6:
        print("_______")
        print(" |    |")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
    elif attempts == 5:
        print("_______")
        print(" |    |")
        print("🙁   |")
        print("      |")
        print("      |")
        print("      |")
    elif attempts == 4:
        print("_______")
        print(" |    |")
        print("🙁   |")
        print(" |    |")
        print("      |")
        print("      |")
    elif attempts == 3:   
        print("_______")
        print(" |    |")
        print("🙁   |")
        print(" |    |")
        print("  \   |")
        print("      |")
    elif attempts == 2:
        print("_______")
        print(" |    |")
        print("🙁   |")
        print(" |    |")
        print("/\    |")
        print("      |")
    elif attempts == 1:
        print("_______")
        print(" |    |")
        print("🙁   |")
        print(" |\   |")
        print("/\    |")
        print("      |")
    else:
        print("_______")
        print(" |    |")
        print("💀   |")
        print("/|\   |")
        print("/\    |")
        print("      |")      

        print("Here Lies your guess.")
        print(f"{correct_word} 🪦 2025-2025")
  
#David G: Compiling word list, random word selector.
word_list = ["ABACK", "ABASE", "ABATE", "ABBEY", "ABIDE", "ABOUT", "ABOVE", "ABYSS", "ACORN", "ACRID", "ACTOR", "ACUTE", "ADAGE", "ADAPT", "ADMIT", "ADOBE", "ADOPT", "ADORE", "ADULT", "AFFIX", "AFTER", "AGAIN", "AGAPE", "AGATE", "AGENT", "AGILE", "AGING", "AGLOW", "AGONY", "AGREE", "AHEAD", "AISLE", "ALBUM", "ALERT", "ALIEN", "ALIKE", "ALIVE", "ALLOW", "ALOFT", "ALONE", "ALOOF", "ALOUD", "ALPHA", "ALTAR", "ALTER", "AMASS", "AMBER", "AMISS", "AMPLE", "ANGEL", "ANGER", "ANGRY", "ANGST", "ANODE", "ANTIC", "ANVIL", "AORTA", "APART", "APHID", "APPLE", "APPLY", "APRON", "APTLY", "ARBOR", "ARDOR", "ARGUE", "AROMA", "ASCOT", "ASIDE", "ASKEW", "ASSET", "ATLAS", "ATOLL", "ATONE", "AUDIO", "AUDIT", "AVAIL", "AVERT", "AWAIT", "AWAKE", "AWARD", "AWASH", "AWFUL", "AXIOM", "AZURE", "BACON", "BADGE", "BADLY", "BAGEL", "BAKER", "BALSA", "BANAL", "BARGE", "BASIC", "BASIN", "BASTE", "BATHE", "BATON", "BATTY", "BAWDY", "BAYOU", "BEACH", "BEADY", "BEAST", "BEAUT", "BEEFY", "BEGET", "BEGIN", "BEING", "BELCH", "BELIE", "BELLY", "BELOW", "BENCH", "BERET", "BERTH", "BESET", "BEVEL", "BINGE", "BIOME", "BIRCH", "BIRTH", "BLACK", "BLADE", "BLAME", "BLAND", "BLARE", "BLAZE", "BLEAK", "BLEED", "BLEEP", "BLIMP", "BLOCK", "BLOKE", "BLOND", "BLOWN", "BLUFF", "BLURB", "BLURT", "BLUSH", "BOAST"] 
correct_word = random.choice(word_list)  
guessed_letters = []  
attempts = 6  
  
while attempts > 0:  
 
    a = ''.join([letter if letter in guessed_letters else '_' for letter in correct_word])  
    print(a)  
  
    guess = input("Guess a letter: ").upper()  
    
    #jasper Holt outputs
    if guess in correct_word:  
        guessed_letters.append(guess)  
        print("Good guess!")
        print_image()  
    else:  
        attempts -= 1 
        print_image()
        print("Wrong guess! Attempts left:", attempts)  
        
    if all(letter in guessed_letters for letter in correct_word):  
        print("Congratulations! You've guessed the word:", correct_word)  
        
    
else:  
    print("Sorry! The word was:", correct_word) 

if attempts == 0:
    break
     
print("Welcome to Hang Man!")
print_image()

# Jameson B: Handle user inputs.
correct_word = random.choice(word_list)
         
    #2. Print user instructions.

guess = input("Guess one letter:\n")
    #3. Computations.
    #4. Output.
    #5. Repeat.




