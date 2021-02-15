# Robert Gemma
# Due date of Progect

#                           The Game of Set


''' Program Description ------------------------------------------------'''

# Brief description of the program

# Pull card out of deck when getting deal
# Random number should be 1 less than the length of deck
# Card should be put back in the same place after it's been put in deal
    # Save indexes in an array - use that and deal to put them back in the
    #    right place

# In intro, ask if playing solo or with 2 players. If 2:
# Players take turns finding a SET
# If a set is found, add a point
# If not, or set already been found, switch turns
# Continue until all sets have been found
# Winner is the player with the most points


''' Globals ------------------------------------------------------------'''

import random

''' Exception Handling -------------------------------------------------'''

def menuExceptions():
    options = ['F', 'D', 'Q']

    noOption = True
    while noOption:
        # Print the menu options
        print('')
        print("F    Find another set")
        print("D    Deal another 12 cards")
        print("Q    Quit the game")
        print('')

        # Get user and input and test if it's a valid option
        option = str(input("Option: "))
        if option not in options:
            if option == 'f' or option == 'd' or option == 'q':
                # Option must be a capital letter
                print("Input must be a capital letter, please try again")
                
            elif "'" in option or '"' in option:
                # Option can't have quotes around it
                print("Do not include quotes in your letter, please try again")
            else:
                # Option must be in options
                print("Input must be F, D, or Q, please try again")
        else:
            # Option is valid, leave the loop
            print('')
            noOption = False
    
    return option


def cardTest(deal):
    noCard = True
    while noCard:
        # Get user input and test if it's a valid card
        card = str(input("Enter a card "))
        if card not in deal:
            if "'" in card or '"' in card:
                print("Do not include quotes in your card, please try again")
            else:
                print("Your card must be in the deal, please try again")
        else:
            # Option is valid, leave the loop
            noCard = False

    return card


def cardExceptions(deal):
    # Get the first and second cards and make sure they aren't the same
    card1 = cardTest(deal)
    card2 = cardTest(deal)
    
    testing = True
    while testing:
        if card1 == card2:
            print("Your first and second cards can't be the same")
            print('')
            print("Your cards:  ", card1)
            card2 = cardTest(deal)
        else:
            testing = False

    # Get the third card and make sure it isn't the same as card1 or card2
    card3 = cardTest(deal)

    testing = True
    while testing:
        if card1 == card3:
            print("Your first and third cards can't be the same")
            print('')
            print("Your cards:  ", card1, card2)
            card3 = cardTest(deal)
        elif card2 == card3:
            print("Your second and third cards can't be the same")
            print('')
            print("Your cards:  ", card1, card2)
            card3 = cardTest(deal)
        else:
            testing = False

    print('')

    return card1, card2, card3

''' Print Functions ----------------------------------------------------'''

def printIntroduction():
    print('                                 Welcome to SET')
    print('')
    print('Instructions:')
    print('')
    
    # Instruction 1
    print('A 12 card deal will be generated and displayed to you, your',
          'job is to select 3')
    print('     cards that create a set.')
    # Instruction 2
    print('A set occurs when all of the values of a feature are either',
          'all the same or all')
    print('     different.')
    # Instruction 3
    print('Each of the four features are indepent of one another - if 3',
          'of the feaures are')
    print('     all the same and one is all different a set sill occurs')
    print('')
    
    return


def printDeal(deal):
    # Print out the deal in a 3X4 table
    print("The current deal of Set cards is:")
    print('')
    for i in range(len(deal) // 3):
        print('   ', deal[i * 3], '  ', deal[((i*3) + 1)],
              '  ', deal[(i*3) + 2])
    print('')

    return


def printSet(goodSet, card1, card2, card3):
    if goodSet:
       print(card1, card2, "and", card3, "are a set")
    else:
       print(card1, card2, "and", card3, "are not a set")
    print('')

    return

def printEndScreen():
    # Print out the end screen
    print('Thank you for playing SET')
    
    return

''' Primary Functions --------------------------------------------------'''

def generateDeck():
    # Initialize the arrays
    deck = []
    numbers = ['1', '2', '3']
    colors = ['R', 'G', 'P']
    shadings = ['S', 'O', 'P']
    symbols = ['O', 'S', 'D']

    # Create the complete set deck
    for i in range(len(numbers)):
        for j in range(len(colors)):
            for k in range(len(shadings)):
                for l in range(len(symbols)):
                    # Initialize the card as blank
                    card = ''
                    # Create each card and append it to deck
                    card += numbers[i]
                    card += colors[j]
                    card += shadings[k]
                    card += symbols[l]
                    deck.append(card)
    
    return deck


def dealCards(deck):
    # Initialize the array
    deal = []
    
    for i in range(12):
        # Generate a randm number from 0 to 80
        index = random.randint(0, 80)
        # Use the random number to index the deck and put that card in deal
        card = deck[index]
        deal.append(card)

    # Find all of the sets in the deal
    
    return deal


def testSet(deal):
    # Get user input of a possible set, with exception handling
    card1, card2, card3 = cardExceptions(deal)

    # Initialize variables for the loop
    testing = True
    goodSet = True
    i = 0

    # Test to see if all of the features are the same or different
    while testing and i < len(card1):
       if card1[i] == card2[i] == card3[i]:
           # If all of the features are the same then the set is still
           #    good, test the next feature
           i += 1
       elif card1[i] != card2[i] != card3[i] and card1[i] != card3[i]:
           # If all of the features are different then the set is still
           #    good, test the next feature
           i += 1
       else:
           # If the feature isn't the all the same or all different between
           #    the 3 cards then they aren't a set
           goodSet = False
           testing = False
    
    # Print out whether or not the cards are a set
    printSet(goodSet, card1, card2, card3)
    
    return


def main():
    # Generate the deck of cards and create the first deal
    deck = generateDeck()
    deal = dealCards(deck)
    
    # Begin playing the game
    printIntroduction()
    playing = True
    menuOption = 'F'

    # Play the different game screens based on user input
    while playing:
        if menuOption is 'F':
            printDeal(deal)
            # Get input and test if it's a set
            testSet(deal)
            # Run the menu
            print("What would you like to do next?")
            menuOption = menuExceptions()

        if menuOption is 'D':
            # Redeal the cards
            deal = dealCards(deck)
            menuOption = 'F'

        if menuOption is 'Q':
            # Quit the game
            playing = False
    
    printEndScreen()

''' Execution ----------------------------------------------------------'''

main()
    
