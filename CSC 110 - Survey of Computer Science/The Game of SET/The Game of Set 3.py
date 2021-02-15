# Robert Gemma
# Due date of Progect

#                           The Game of Set


''' Program Description ------------------------------------------------'''

# Brief description of the program

# Print out instructions specific to # of players
# Set can be made using any combination of 3 cards in set inner array


''' Globals ------------------------------------------------------------'''

import random
global deck
global deal
global players
global player

''' Exception Handling -------------------------------------------------'''

def playerExceptions():
    global players
    
    noPlayers = True
    while noPlayers:
        players = input("Are you playing with 1 or 2 players? ")
        try:
            # Player must be an integer
            players = int(players)
        except ValueError:
            print('Player must be an integer, either 1 or 2')

        if players == 1 or players == 2:
            # There can only be 1 or 2 players
            noPlayers = False
        else:
            print('There can only be 1 or 2 players')

    print('')
    
    return

        
def menuExceptions():
    options = ['D', 'Q']

    noOption = True
    while noOption:
        # Get user and input and test if it's a valid option
        option = str(input("Option: "))
        if option not in options:
            if option == 'd' or option == 'q':
                # Option must be a capital letter
                print("Input must be a capital letter, please try again")
                
            elif "'" in option or '"' in option:
                # Option can't have quotes around it
                print("Do not include quotes in your letter, please try again")
            else:
                # Option must be in options
                print("Input must be D, or Q, please try again")
        else:
            # Option is valid, leave the loop
            print('')
            noOption = False
    
    return option


def cardTest():
    global deal
    
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


def cardExceptions():
    global deal
    
    # Get the first and second cards and make sure they aren't the same
    card1 = cardTest()
    card2 = cardTest()
    
    testing = True
    while testing:
        if card1 == card2:
            print("Your first and second cards can't be the same")
            print('')
            print("Your cards:  ", card1)
            card2 = cardTest()
        else:
            testing = False

    # Get the third card and make sure it isn't the same as card1 or card2
    card3 = cardTest()

    testing = True
    while testing:
        if card1 == card3:
            print("Your first and third cards can't be the same")
            print('')
            print("Your cards:  ", card1, card2)
            card3 = cardTest()
        elif card2 == card3:
            print("Your second and third cards can't be the same")
            print('')
            print("Your cards:  ", card1, card2)
            card3 = cardTest()
        else:
            testing = False

    print('')

    return card1, card2, card3

''' Print Functions ----------------------------------------------------'''

def printInstructions():
    global players
    
    # Print introduction and the game instructions
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
    print('Each correctly identified set will earn you 1 point.')

    if players == 1:
        print('Continue playing until all of the sets have been found!')
    elif players == 2:
        print('If your awnser is not a set, or the set has already been',
              'found, you lose your')
        print(' turn.')
        print('The round ends when all of the sets have been found!')

    print('')
    
    return

 
def printDeal():
    global deal
    # Print out the deal in a 3X4 table
    print("The current deal of Set cards is:")
    print('')
    for i in range(len(deal) // 3):
        print('   ', deal[i * 3], '  ', deal[((i*3) + 1)],
              '  ', deal[(i*3) + 2])
    print('')

    return


def printSet(sets, foundSets, testSet, card1, card2, card3, goodSet):
    # Print whether or not the three inputed cards form set
    if goodSet:
        print(card1, card2, "and", card3, "are a set")
        print('There are', len(sets) - 1, 'sets remaining in this deal')
    elif testSet in foundSets:
        print('This set has already been found')
        print('There are', len(sets), 'sets remaining in this deal')
       
    else:
        print(card1, card2, "and", card3, "are not a set")
        print('There are', len(sets), 'sets remaining in this deal')

    print('')

    return


def printMenu():
    # Print the menu options
    print('What would you like to do next?')
    print('')
    print("D    Deal another 12 cards")
    print("Q    Quit the game")
    print('')


def printEndScreen(players, p1Score, p2Score):
    # Prit out the score
    print("Player 1's Score: ", p1Score)
    if players == 2:
        print("Player 2's Score: ", p2Score)

        # Print who won
        if p1Score > p2Score:
            print("Player 1 wins!")
        elif p2Score > p1Score:
            print("Player 2 wins!")
        else:
            print("It's a tie!")

    print('')
    print('Thank you for playing SET')

    return


''' Primary Functions --------------------------------------------------'''

def generateDeck():
    # Initialize the arrays
    global deck
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
    
    return


def dealCards():
    # Initialize the arrays
    global deck
    global deal
    deckCopy = deck
    deal = []
    
    for i in range(12):
        # Generate a random number from to index the deck (copy)
        index = random.randint(0, (len(deckCopy) - 1))
        # Use the random number to index the deck (copy) and it in deal
        card = deckCopy.pop(index)
        deal.append(card)
    
    return


def findSets():
    global deal
    
    # Initialize the array holding all of the sets in the deal
    sets = []
    
    # Test all of the possible combinations of deal to find all the sets
    for i in range(len(deal)):
        for j in range(len(deal) - (i+1)):
            for k in range(len(deal) - (j+i+2)):              
                card1 = deal[i]
                card2 = deal[(j+i) + 1]
                card3 = deal[(k+j+i) + 2]
                
                # Initialize variables for the test loop
                testing = True
                goodSet = True
                ch = 0

                # Test if the 3 cards form a set
                while testing and ch < len(card1):
                   if card1[ch] == card2[ch] == card3[ch]:
                       # If all features are the same then the set is still
                       #    good, test the next one
                       ch += 1
                   elif card1[ch] != card2[ch] != card3[ch] and card1[ch] != card3[ch]:
                       # If all of the features are different then the set
                       #    is still good, test the next one
                       ch += 1
                   else:
                       # If the feature isn't the all the same or all
                       #    different then the 3 cards aren't a set
                       goodSet = False
                       testing = False

                # If all of the testing passes, the card is a set
                if goodSet:
                    # Save the set as a list and append it to sets
                    SET = [card1, card2, card3]
                    sets.append(SET)

    return sets


def changePlayer():
    global player
    
    if player == 1:
        player = 2
        print("It's player 2's turn!")
    elif player == 2:
        player = 1
        print("It's player 1's turn!")
    print('')

    return

def checkSet(sets, foundSets, p1Score, p2Score):
    global deal
    global players
    goodSet = False
    
    # Get user input of a possible set, with exception handling
    card1, card2, card3 = cardExceptions()
    # Save the cards as a list
    testSet = [card1, card2, card3]

    # Test if the list of cards are in set
    for i in range(len(sets)):
        if testSet in sets:
            goodSet = True

    # Print out whether or not the cards are a set
    printSet(sets, foundSets, testSet, card1, card2, card3, goodSet)

    if goodSet and testSet not in foundSets:
        # Pulls the set out of sets and puts in in foundSets
        sets.remove(testSet)
        foundSets += [testSet]

        # If a new set was found, add 1 to the players score
        if player == 1:
            p1Score += 1
        elif player == 2:
            p2Score += 1
    else:
        # Change players if playing with multiple people
        if players == 2:
            changePlayer()

    return sets, foundSets, p1Score, p2Score


def main():
    global deal
    global player
    global players
    player = 1
    p1Score = 0
    p2Score = 0
    
    # Generate the deck of cards and print out the intro
    generateDeck()
    print('                                 Welcome to SET')
    print('')

    # Determine how many players there are and print the game instructions
    playerExceptions()
    printInstructions()

    # Begin playing the game
    menuOption = 'D'
    playing = True
    
    # Run the different game screens based on user input
    while playing:
        if menuOption is 'F':
# DEBUGGING
            for i in range(len(sets)):
                print(sets[i])
            print('')
            for i in range(len(foundSets)):
                print(foundSets[i])
            
            # Get user input, and check if it's a set
            sets, foundSets, p1Score, p2Score = checkSet(sets, foundSets, p1Score, p2Score)

            # Display the menu when all of the sets have been found
            if len(sets) == 0:
                printMenu()
                menuOption = menuExceptions()
    
        elif menuOption is 'D':
            # Deal 12 new cards
            dealCards()

            # Print the deal and find all the sets in it
            printDeal()
            sets = findSets()
            foundSets = []

            # Begin finding a set
            menuOption = 'F'

        elif menuOption is 'Q':
            # Quit the game
            playing = False
    
    printEndScreen(players, p1Score, p2Score)

''' Execution ----------------------------------------------------------'''

main()
