# Robert Gemma
# November 17, 2017

#              Programming Project Skeleton - The Game of Set

''' Program Description ------------------------------------------------'''

# The program I am writing for the Programming Project will run the
# game of SET. It will create the 81 card deck that SET uses, and deal 12 of
# them at a time. The user will input three cards that he/she thinks form a
# set and the program will return whether or not the cards are one.

# In order to accomplish this, I will need a function that creates the deck
# of cards, randomly pulls a 12 card deal from the deck, and one that both
# asks the user to input 3 cards and checks if they are a set. I will also
# use a seperate function to run the menu.

# The program will find out if the user inputed a set by testing each of the
# 4 features one at a time, using if statements to determine if they are
# the same in all 3 cards, or different in all three (the criteria for
# creating a set). It will assume that the inputed cards are a set, and
# use an else statement to change the set boolean to False if the listed
# criteria fail for any of the four card features.

''' Main Function Pseudocode -------------------------------------------'''

# deck = generateDeck
# deal = dealCards(deck)
# playing = True

# While playing:
#   If menuOption is F:
#       testSet()
#       menu()
#   If menuOption is D
#      deal = dealCards
#   If menuOption is Q,
#       playing = False

# print the end screen

''' Function Design ----------------------------------------------------'''

    ''' Exception Handling -----------------------------------------'''

def menuExceptions:
    options = ['F', 'D', 'Q']
    # Input must be in options
    
    return menu

def setExceptions:
    # Card must be in the deal
    # Can't pick the same card twice to test if they're a set
    
    return setChoice


    ''' Functions --------------------------------------------------'''

def generateDeck:
    deck = []
    # Quad nested for loop
    # End with an array with 81 objects
    
    return deck


def dealCards(deck):
    deal[]
    # Randomly pick 12 numbers (0-80) to index deck
    # Pull the card at the index numbers into deal
    # Print the deal (3X3)
    # Set menuOPtion to F
    
    return deal, menuOption

def testSet(deal):
    # Get user input of a possible set, with exception handling (card1)
    # Get user input of a possible set, with exception handling (card2)
    # Get user input of a possible set, with exception handling (card3)

    # Initialize testing to True
    # Initialize set to True
    # Initialize index (i) to 0
    
    # Test to see if the inputs are a set (loop through string)
    # While Testing and i < (card1.length-1):
    #   If card1[i], card2[i] and card3[i] are the same
    #       i += 1
    #   Elif card1[i], card2[i] and card3[i] are different
    #       i += 1
    #   Else
    #       set = False
    #       testing = False

    # If set:
    #   print(card1, card2, "and", card3 "are a set")
    # Else:
    #   print(card1, card2, "and", card3 "are not a set")

    return

def menu:
    # Print out the menu options
    # Get input for the option selected, use exception handling
    
    return menuOption




