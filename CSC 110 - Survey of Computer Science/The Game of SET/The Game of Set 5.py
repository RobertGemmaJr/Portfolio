# Robert Gemma
# December 11, 2017

'''                         The Game of Set                             '''


''' Program Description ------------------------------------------------'''

# This program allows 1 or two players to play the game of set. The
# player(s) are taksed with finding a combination of 3 cards in which all
# of the 4 features are either all the same or all different. Further
# instructions about the game can be found in the printInstructions
# function, which is located in the third section of code.

# I split this code into 6 total sections. In the first section I declare
# all of the global variables I use in the program. Although this is not
# neccisary, I wanted them to all be present at the top of the
# program so I can keep track of them. The next section of code contains
# all of the code that deals with user input and exception handling.
# Each function deals with a different input, and contains 'exceptions' in
# their name. The third section of code contains what I call 'secondary
# functions.' These functions are generally shorter, and are called in the
# functions found in the 'primary functions' section. They perform short
# tasks but sometimes need to be called at different places so putting the
# code in a seperate function keep the primary functions relatively small.
# The next section contains all of the print functions. They do not perform
# any calculations but, like the secondary functions, prevent any functions
# from becoming uneccesarily long. After the print functions is
# the section that contains all of the primary functions. This is where
# most of the work of the program is done, and all of the primary functions
# are called in the main function. Finally, the last section of code
# actually executes the program. It defines the main function, and the last
# line of the program calls the it.

# I did not neccesarily use any of the algorithims we learned in class this
# semester. However, bits and pieces of each algorithim can be found
# throughout my program, all of which made my program much cleaner and more
# effecient. A lot of the algorithims we looked at that I needed in this
# program dealt with using arrays, which Python already had an operation
# for. Naturally, I just used the Python functions.

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
            # Players must be an integer
            players = int(players)
        except ValueError:
            print('Player must be an integer, either 1 or 2')

        if players == 1 or players == 2:
            # Option is valid, leave the loop
            noPlayers = False
        else:
            # Set is a one or two player game
            print('There can only be 1 or 2 players')

    print('')
    
    return


def warningExceptions():
    # Get a yes or no anwser for use menuExcpetions
    noAnwser = True
    while noAnwser:        
        anwser = str(input('Enter Y or N: '))
        if anwser != 'Y' and anwser != 'N':
            # Anwser must be Y or N
            print('Please enter Y if you wish to end the round or N if not')
        else:
            # Option is valid, leave the loop
            noAnwser = False

    return anwser

def menuExceptions(sets):
    global players
    options = ['F', 'D', 'Q']
    
    noOption = True
    while noOption:
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
        
        elif option == 'F' and len(sets) == 0:
            # All sets have been found, can't find another
            print('There are no more sets to find')

        elif option == 'D' and players == 2 and len(sets) > 0:
            # Starting a new round will cancel the round's score
            print('The round is not complete, are you sure you want to,'
                  'begin a new one?')
            print('The scores for this round will be lost')
            # Get user response to warning
            anwser = warningExceptions()
            if anwser == 'Y':
                # If players want to continue, leave the loop
                print('')
                noOption = False   

        else:
            # Option is valid, leave the loop
            print('')
            noOption = False
    
    return option


def cardTest():
    global deal
    
    noCard = True
    while noCard:
        card = str(input("Enter a card "))
        
        if card not in deal:
            if "'" in card or '"' in card:
                # Card can't have quotes around it
                print("Do not include quotes in your card, please try again")
            else:
                # Card must be in the current deal
                print("Your card must be in the deal, please try again")
        else:
            # Option is valid, leave the loop
            noCard = False

    return card


def cardExceptions():
    global deal
    
    # Get the first and second cards
    card1 = cardTest()
    card2 = cardTest()

    testing = True
    while testing:
        if card1 == card2:
            # Each card must be unique
            print("Your first and second cards can't be the same")
            print('')
            # Print saved cards and find the second card again
            print("Your cards:", card1)
            card2 = cardTest()
        else:
            # Option is valid, leave the loop
            testing = False

    # Get the third card
    card3 = cardTest()

    testing = True
    while testing:
        if card1 == card3:
            # Each card must be unique
            print("Your first and third cards can't be the same")
            print('')
            # Print saved cards and find the third card again
            print("Your cards:  ", card1, card2)
            card3 = cardTest()
        elif card2 == card3:
            # Each card must be unique
            print("Your second and third cards can't be the same")
            print('')
            # Print saved cards and find the third card again
            print("Your cards:  ", card1, card2)
            card3 = cardTest()
        else:
            # Option is valid, leave the loop
            testing = False
            print('')

    # Save the cards as a list
    testSet = [card1, card2, card3]
    
    return testSet

''' Secondary Functions ------------------------------------------------'''

def changePlayer():
    global player

    # Swap between player 1 and player 2
    if player == 1:
        player = 2
        print("It's player 2's turn!")
    elif player == 2:
        player = 1
        print("It's player 1's turn!")

    print('')

    return


def getRightPlayer(roundNum):
    global player   
    modRound = roundNum % 2

    if modRound == 1 and player == 1:
        # Begin odd rounds with player one, which is current player
        print("It's player 1's turn!")
    elif modRound == 0 and player == 2:
        # Begin even rounds with player 2, which is current player
        print("It's player 2's turn!")
    else:
        # Player must be changed before the new round can start
        changePlayer()

    return

''' Print Functions ----------------------------------------------------'''

def printInstructions():
    global players
    
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

    # Single player rules
    if players == 1:
        print('Continue playing until all of the sets have been found!')
    # Multiplayer rules
    elif players == 2:
        print('If your awnser is not a set, or the set has already been',
              'found, you lose your')
        print('     turn.')
        print('The round ends when all of the sets have been found!')

    print('')
    
    return

 
def printDeal():
    global deal
    
    print("The current deal of Set cards is:")
    print('')
    
    # Print out the deal in a 3X4 table
    for i in range(len(deal) // 3):
        print('   ', deal[i * 3], '  ', deal[((i*3) + 1)],
              '  ', deal[(i*3) + 2])

    print('')

    return


def printSet(sets, testSet, setResponse):
    if setResponse == 0:
        # A new set was found
        print(testSet[0], testSet[1], "and", testSet[2], "are a set")

    elif setResponse == 1:
        # An old set was found, change player if needed
        print('This set has already been found')
        if players == 2:            
            changePlayer()

    else:
        # The cards do not form a set, change player if needed
        print(testSet[0], testSet[1], "and", testSet[2], "are not a set")
        if players == 2:            
            changePlayer()

    print('There are', len(sets), 'sets remaining in this deal')
    print('')

    return


# Function displays all of the new and found sets in the deal, use to debug
#   other parts of the code without having to manuallly find the sets
def debugSets(sets, foundSets):
    # Display all of the found sets
    print('Found sets:')
    for i in range(len(foundSets)):
        print(foundSets[i])
    print('')
    
    # Display all of the remaining sets
    print('Sets remaining:')
    for i in range(len(sets)):
        print(sets[i])
    print('')
    
    return


def printMenu():
    # Print the menu options
    print('What would you like to do next?')
    print('')
    print('F    Find another set')
    print("D    Deal another 12 cards")
    print("Q    Quit the game")
    print('')

    return


def printRoundScore(p1Score, p2Score):
    # Print the scores after a round is complete
    print('Player one scored', p1Score, 'points this round')
    if players == 2:
        print('Player two scored', p2Score, 'points this round')

    print('')
    
    return


def printEndScreen(players, finalScore1, finalScore2):
    # Print out the final score
    print("Player 1's Final Score: ", finalScore1)
    
    if players == 2:
        # Print both player's scores if it's a multiplayer game
        print("Player 2's Final Score: ", finalScore2)

        # Print who won
        if finalScore1 > finalScore2:
            print("Player 1 wins!")
        elif finalScore2 > finalScore1:
            print("Player 2 wins!")
        else:
            print("It's a tie!")

    print('')
    print('Thank you for playing SET')

    return

''' Primary Functions --------------------------------------------------'''

def generateDeck():
    global deck
    deck = []

    # Lists of the 3 possibilities for the 4 card features
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
    global deck
    global deal
    deal = []
    
    # Create a copy of the deck to manipulate
    deckCopy = deck
    
    for i in range(12):
        # Generate a random number
        index = random.randint(0, (len(deckCopy) - 1))
        
        # Use the random number to index the deck (copy) and put it in deal
        card = deckCopy.pop(index)
        deal.append(card)
    
    return

def findSets():
    global deal
    sets = []
    
    # For loop denerates each unique combination of 3 cards for all cards
    #   in the deal
    for i in range(len(deal)):
        for j in range(len(deal) - (i+1)):
            for k in range(len(deal) - (j+i+2)):
                # Create the 3 cards
                card1 = deal[i]
                card2 = deal[(j+i) + 1]
                card3 = deal[(k+j+i) + 2]
                
                # Test if the 3 cards form a set
                testing = True
                goodSet = True
                ch = 0
                while testing and ch < len(card1):
                    # The feature is the same for all 3 cards
                    allSame = card1[ch] == card2[ch] == card3[ch]
                    # The feature is different for each card
                    allDifferent = card1[ch] != card2[ch] != card3[ch] and card1[ch] != card3[ch]
                    
                    if allSame or allDifferent:
                        # Test the next feature
                        ch += 1
                    else:
                        # If the feature isn't the all the same or all
                        #   different then the 3 cards aren't a set
                        goodSet = False
                        testing = False

                # If all of the testing passes, the cards are a set
                if goodSet:
                    # Save the set as a list and append it to sets
                    SET = [card1, card2, card3]
                    sets.append(SET)

    # Make sure foundSets is empty
    foundSets = []
    
    return sets, foundSets


def checkSet(sets, foundSets, p1Score, p2Score):
    global deal
    global players
    goodSet = False
    
    # Get user input of a possible set, with exception handling
    testSet = cardExceptions()

    # Test if the list of cards are in sets
    i = 0
    while not goodSet and i < len(sets):
        # Turn lists into sets because order does not matter
        setOfSets = set(sets[i])
        setOfTestSet = set(testSet)    

        # Check if testSet is in sets
        if setOfTestSet == setOfSets:
            goodSet = True
        else:
            # Compare the testSet to the next set in sets
            i += 1

    if goodSet and testSet not in foundSets:
        # A new set was found
        setResponse = 0
        
        # Put the set in foundSets and remove it from sets
        foundSets += [sets[i]]
        sets.remove(sets[i])

        # Increment the player's score
        if player == 1:
            p1Score += 1
        elif player == 2:
            p2Score += 1

    elif testSet in foundSets:
        # An old set was found
        setResponse = 1

    else:
        # The cards do not form a set
        setResponse = 3

    # Print out whether or not the cards are a set
    printSet(sets, testSet, setResponse)
    
    return sets, foundSets, p1Score, p2Score

''' Execution ----------------------------------------------------------'''

def main():
    # Intialize variables
    global deal
    global player
    global players
    player = 1
    roundNum = 0
    p1Score = 0
    p2Score = 0
    finalScore1 = 0
    finalScore2 = 0
    
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
    while playing:  
        if menuOption is 'D':
            # Deal 12 new cards and find all the sets in it
            dealCards()
            sets, foundSets = findSets()

            # Begin a new round
            roundNum += 1
            if players == 2:                
                getRightPlayer(roundNum)

            # Rest the round scores
            p1Score = 0
            p2Score = 0

            # Find the first set
            menuOption = 'F'
            
        elif menuOption is 'F':
            # Print out the deal
            printDeal()
            
            # Print out all of the sets and found sets for debugging code
            #debugSets(sets, foundSets)

            # Get user input, and check if it's a set
            sets, foundSets, p1Score, p2Score = checkSet(sets, foundSets, p1Score, p2Score)

            # If the round is over, print the round score and add it to
            #   the final score
            if len(sets) == 0:
                printRoundScore(p1Score, p2Score)
                finalScore1 += p1Score
                finalScore2 += p2Score
            
            # Display the menu and get user input of what to do next
            printMenu()
            menuOption = menuExceptions(sets)

        elif menuOption is 'Q':
            # Stop the game
            playing = False

    # Print the end screen
    printEndScreen(players, finalScore1, finalScore2)

main()
