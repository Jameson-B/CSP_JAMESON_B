 #Hang Man Python Jameson, Robert, Jasper, David.

import random
  
# Robert N: Art
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


        
#David G: Compiling word list, random word selector.
word_list = ["ABACK", "ABASE", "ABATE", "ABBEY", "ABIDE", "ABOUT", "ABOVE", "ABYSS", "ACORN", "ACRID", "ACTOR", "ACUTE", "ADAGE", "ADAPT", "ADMIT", "ADOBE", "ADOPT", "ADORE", "ADULT", "AFFIX", "AFTER", "AGAIN", "AGAPE", "AGATE", "AGENT", "AGILE", "AGING", "AGLOW", "AGONY", "AGREE", "AHEAD", "AISLE", "ALBUM", "ALERT", "ALIEN", "ALIKE", "ALIVE", "ALLOW", "ALOFT", "ALONE", "ALOOF", "ALOUD", "ALPHA", "ALTAR", "ALTER", "AMASS", "AMBER", "AMISS", "AMPLE", "ANGEL", "ANGER", "ANGRY", "ANGST", "ANODE", "ANTIC", "ANVIL", "AORTA", "APART", "APHID", "APPLE", "APPLY", "APRON", "APTLY", "ARBOR", "ARDOR", "ARGUE", "AROMA", "ASCOT", "ASIDE", "ASKEW", "ASSET", "ATLAS", "ATOLL", "ATONE", "AUDIO", "AUDIT", "AVAIL", "AVERT", "AWAIT", "AWAKE", "AWARD", "AWASH", "AWFUL", "AXIOM", "AZURE", "BACON", "BADGE", "BADLY", "BAGEL", "BAKER", "BALSA", "BANAL", "BARGE", "BASIC", "BASIN", "BASTE", "BATHE", "BATON", "BATTY", "BAWDY", "BAYOU", "BEACH", "BEADY", "BEAST", "BEAUT", "BEEFY", "BEGET", "BEGIN", "BEING", "BELCH", "BELIE", "BELLY", "BELOW", "BENCH", "BERET", "BERTH", "BESET", "BEVEL", "BINGE", "BIOME", "BIRCH", "BIRTH", "BLACK", "BLADE", "BLAME", "BLAND", "BLARE", "BLAZE", "BLEAK", "BLEED", "BLEEP", "BLIMP", "BLOCK", "BLOKE", "BLOND", "BLOWN", "BLUFF", "BLURB", "BLURT", "BLUSH", "BOAST"] 
correct_word = random.choice(word_list)  
guessed_letters = []
wrong_letters = [] 
attempts = 6 

# Jameson B: Intro message, general supervision/ Helping others
print_image()
print("Welcome to Hang Men!")


while attempts > 0:  
 
    a = ''.join([letter if letter in guessed_letters else '_' for letter in correct_word])  
    print(a)  
  
    guess = input("Guess a letter: ").upper()
    guessed_letters.append(guess)
   
#Jasper Holt outputs
    if guess in correct_word:     
        print("Good guess!") 
    else:  
        attempts -= 1
        wrong_letters.append(guess) 
        print("Wrong guess! Attempts left:", attempts)
    print_image()
    print(wrong_letters) 
           
    if all(letter in guessed_letters for letter in correct_word):  
        print("Congratulations! You've guessed the word:", correct_word)  
def end_statement():

    print("Sorry! The word was:", correct_word)
    print("Here Lies your guess: 🪦 2025-2025")
end_statement()