
# ==================================
# Blackjack Setup
# ==================================

# Part of modules and functions topic

# We will work with tkinter to code a simple card game
# We will also explore more on functions and see why intellij warns about shadowing (using same name)
# variables in outer scope
# This game will help us look at this in more detail

# Blackjack is a simple card game. The aim is to get a higher score than the dealer
# but without going above a score of 21.
# If the total number of cards in a hand comes to more than 21, the player is said to have busted, hence game over.

# We will have the following conditions in our version of blackjack:

# The dealer deals one card to each player and to himself.
# Each player but not the dealer gets a second card
# The player then decides whether to stick with the total they have or "hit" (meaning to get another card)
# The player can hit as much as they like but if their total is more than 21, they are bust
# The cards that the player holds when they finish is called their "hand"
# Once all players are "stuck" (no new cards) or "bust", the dealer gets a second card and dealer then decides whether to stick or hit.
# If dealer goes over 21, they bust and the player that is not bust wins
# NOTE that the dealer cannot stick on less than 17 i.e. he has to get a card if he has less than 17
# The dealer also must stick if they have 17 or more. i.e. they cannot take another card to go closer to 21,
# Player plays against dealer. And whoever has highest highest number but below 21 wins.
# If the dealer and player have same number, they are draw
# There are 13 cards in each of 4 suits making a total of 52 cards in the pack
# First 10 cards are 1 to 10, then three facecards called Jack, King and Queen (each with value 10)
# The suits are called Hearts, Diamonds, Clubs and spades
# The Ace Card can have value of 1 or 11 and the player decides which value they should take

# You can view and download the cards here
# http://svg-cards.sourceforge.net/ > Download SVG Cards
# The images are in SVG, so I had to convert them to "png" and put them under folder "cardspng"
# Used this site for converting from SVG to PNG: http://svgtopng.com/
# Support for png files was added to tkinter version 8.6. So if you are using earlier version, use ppm image files
# We can use png files since our version is 8.6 (see how to check version below)
# But I tried to download latest version, and it was different from Trainer, so I used SVG-card-1.0
# After extracting the cards, they are in a folder named "svg", we rename that folder "cards" to match trainer video
# In my case, I had to convert them to PNG and put in folder named "cardspng"
# Then we copy that folder "cardspng" and put it in folder "32_Blackjack"
# and you will see "cardspng" pop up on the left side of this screen under "32_Blackjack" folder

# We also import random module because cards will be assigned in random

import random

# Then import tkinter

try:
    import tkinter
except ImportError:  # Python 2
    import Tkinter as tkinter

print(tkinter.TkVersion)  # How to check tkinter version. In our case, we have 8.6

# we set up mainWindow.

# NOTE about Tkinter.Tk()
# https://docs.python.org/2/library/tkinter.html
# class Tkinter.Tk(screenName=None, baseName=None, className='Tk', useTk=1)
# The Tk class is instantiated without arguments. This creates a toplevel widget of Tk which usually is the main window of an # # application.
# Each instance has its own associated Tcl interpreter.

mainWindow = tkinter.Tk()

# Set up screen and frame for the dealer and player

mainWindow.title("Black Jack")  # Define title for mainWindow
mainWindow.geometry("640x480")  # Set up dimensions for the mainWindow (Note its in string format under "")
#  NOTE: you can configure background of mainWindow here. in this case it is green.
# White is default if you don't configure it.
mainWindow.configure(background="green")

# Program needs to have space for dealer's and player's cards and somewhere to display results
#  and a place for them to choose whether to hit or stick.
# We will use one button to deal cards to player and another button to deal cards to dealer

result_text = tkinter.StringVar()  # http://effbot.org/tkinterbook/variable.htm
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# Embedded frame to hold the card images

dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

# Embedded frame to hold the card images and frame

player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

# Embedded frame to hold buttons

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')


# NOTE: we are commenting out "dealer_button" and "player_button" here because we will add "command=deal_dealer" later in the program
# but we keep this here to help understand how and why it was created

# Dealer button

dealer_button = tkinter.Button(button_frame, text="Dealer")
dealer_button.grid(row=0, column=0)

# Player Button

player_button = tkinter.Button(button_frame, text="Player")
player_button.grid(row=0, column=1)


# Now we will load the card images under folder "cards"
# cards are labeled 1_of_Clubs, 1_of_diamonds, 1_of_hearts, 1_of_Spades etc
# We can use a simple for loop to load them all in.
#
# The face card images can be retrieved by running a second loop that goes through the list of names (scroll down under cards)
# These list of names start with back_01 to 14, then black_joker, then jack_of_clubs etc
#
# so with both loops, all 52 card images can be added.
# This will only be done once but we will create a function to do it.
# By putting the loading code in its own function, the main program will be more readable because it just needs to call the loading function

# ========================
# Function to load images
# ========================
# NOTE: This can be placed immediately after "mainWindow = tkinter.Tk()" above.
# We place functions at the top so they can be called by any part of the program.
# But for now, we will add the function here


def load_images(card_images):  # define function named "load_images" set to accept parameter to be named "card_images"
    suits = ['of_clubs', 'of_diamonds', 'of_hearts', 'of_spades']  # Note these names are case sensitive
    face_cards = ['jack', 'king', 'queen']

    # Remember we said that tkinter version 8.6 is needed to use png files, so we will put a test here

    if tkinter.TkVersion >= 8.6:
        extension = 'png'  # if 8.6 or later, use picture extension of "png". in our case, we have files with "svg" so I use "svg" here
    else:
        extension = 'ppm'  # if less than 8.6, use picture extension ppm

    # Now we will create first loop which says
    # For each suit, retrieve the image for the cards.

    for suit in suits:  # suits include 'hearts', 'clubs', 'diamonds', 'spades' defined above.
        # Another for loop to retrieve number of cards from 1 to 10 using range from 1 to 11 (last one excluded in range)
        for card in range(1, 11):
            # We retrieve names under folder "cardspng" on the left where images are stored
            # So for number 1 in range, we go to "cardspng", and retrieve in format {}_{}.{} which comes to "01_of_hearts.png"
            # suit is either 'hearts', 'clubs', 'diamonds', 'spades'
            # extension is either svg or ppm (should be svg in our case)
            # Names will be put in variable "name". format(str(card)) gets range and converts it to string to add to "name" in string format

            # Here we assign 0 behind number if its less than 10, because our files start with 01, 02, 03 etc

            if card < 10:
                card = "0" + str(card)
            else:
                card = str(card)

            # First placement {} gets "card" (01 for first iteration)
            # Second placement {} gets "suit" (first one is "of_clubs")
            # Third placement {} gets "extension" which is "png" in our case because we have tkinter 8.6 and our files are in png

            name = 'cardspng/{}_{}.{}'.format(card, suit, extension)
            print(name)  # We can print to see what is in file "name" although this is optional

            # Now we extract the images themselves and store them in "images" variable.
            # We extract images using method named tkinter.PhotoImage
            # Image will be extracted using variable "name" we created above

            image = tkinter.PhotoImage(file=name)

            # Now we append the images from variable "image" above to "card_images" which is the parameter that
            # function "def load_images(card_images)" takes
            # This means we are retrieving card_images and giving them to function 'load_images" for it to load and print them.
            # they will be added in format "card, image". So first iteration will be 1, image, then 2 image etc

            card_images.append((card, image,))

        # We let above loop "for card in range(1, 11)" finish and then do a loop to retrieve face cards
        # face_cards are from function "def load_images" and are "face_cards = ['jack', 'king', 'queen']"

        for card in face_cards:
            # Since our images have extension_en e.g. jack_of_clubs_en.png
            # we added the third placement here to add "en"
            # First placement {} gets "str(card) i.e. card value (jack, king or queen) converted to string
            # Second placement {} gets "suit" (of_clubs, of_diamonds etc) from here: suits = ['of_clubs', 'of_diamonds', 'of_hearts', 'of_spades']
            # Third placement {} gets string "en"
            # Fourth placement {} gets extension, "png" in our case since we have tkinter 8.6

            name = 'cardspng/{}_{}_{}.{}'.format(str(card), suit, "en", extension)
            print(name)  # We can print to see what is in file "name" although this is optional
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))

# Now we can test to see if these images load

cards = []  # we start with empty list
load_images(cards)  # load images

# Then print to see we get for cards. This gives you "[('01', <tkinter.PhotoImage object at 0x0553FD10>),
# etc show placement of card objects

print(cards)


# A new deck of cards can be created from the cards that we imported
# Then we can shuffle them using the using the "Shuffle" function from the "random" module that we imported
# The program will also need to store the cards dealt to each player

# We will first initialize a dealer hand and player hand

# Create a new list named "deck" to store cards and shuffle them.
# NOTE we create new list (deck) that contains same info as list (cards)
# We separate this because as the cards in "deck" are shuffled and assigned, python will be decrementing them until there is nothing left
# So we need to have two separate list of cards so we are not left with nothing to shuffle

# NOTE that "cards" was initially an empty list and we loaded it with images from "load_images(cards)"
# Here we create a list called "deck" and assign it information in list "cards"
# NOTE you can create a list in two ways. Using square brackets and using "list" constructor
#       list_1 = ["a", "b"]    # using square brackets
#       list_2 = list(x)  # using list constructor and passing it agument

deck = list(cards)
random.shuffle(deck)  # Then we shuffle the "deck" list to make it random

# We create a list to store dealers and player's hands
# First we initialize them to empty list

dealer_hand = []
player_hand = []


# Now we need to create some functions that will drive the game

# ==================================
# Function to deal cards to players
# ==================================
# We start with function to deal cards to players each time their button is clicked.
# We are going to make a function called "dealer_card"

# This function has a single parameter i.e. the "frame" that the image should be displayed on


def deal_card(frame):  # takes parameter "frame" which is the frame that the card will be displayed on.
    # We pop the next card off the top of the deck.
    # https://docs.python.org/2/tutorial/datastructures.html (for .pop description)
    # pop() is a way to retrieve an item from a list and also remove it from the list at the same time
    # it is the opposite of append which adds an item to the list
    # pop takes an item from the specified position in the list defaulting to the end if the position to be taken from is not specified
    # By specifying position 0, we can take cards from the top of the deck
    # If you leave () without anything, you will pop the card from the bottom of the deck
    # Both append and pop can also be used with an index to add or remove from the specified position
    next_card = deck.pop(0)

    # Once the next_card has been retrieved from the deck, the function creates a tkinter label in the frame that is passed to the function
    # and sets its image to the photo image stored in the next_card tuple.
    # The label is then "packed" against the left side of the frame so that all cards should stack against each other from left to right
    # as they are being added. With the newest one to the left.
    # Now we add image to a label and display the label. So we will actually see what that card is.
    # We pass "frame" to this label. This is the parameter that was passed to "dealer_card"
    # Image=next_card[1]
    # Use "pack" geometry manager to place the label text within the window on the left side. options are top, bottom, left, right
    # We use "pack" instead of using "grid" to place the label.
    # NOTE it is not advisable to use "pack" and "grid" in the same window as it will give an error. But you can use "pack" in its own window
    # Since every widget is a window, packing these images into this frame is fine as long as we don't try to add anything else to the frame using grid
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')

    # The function then returns the next_card tuple so that whatever is calling it can also check the face value of the card.
    # Now return the cards face value
    return next_card

# NOTE: Above functions should be created above the main program. But we created them in sequence here to understand the process

# Now we need to link up the functions to the buttons
# A "function" is associated with a "widget" using the "command" property
# it would be tempting to go to the dealer_button function and add "command=deal_card(dealer_card_frame)"
#
# dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_card(dealer_card_frame))
#
# however you have to be careful when setting up the "command' property widgets
# The value that you assign has to be the function that you want to execute when the button is clicked.
# So you don't want to call the function instead of assigning it the command
# So by attempting to pass the frame to the function ==> command=deal_card(dealer_card_frame)) => at the same time as assigning
# The function of the button
#
# So the correct code would be without passing dealer_card_frame
#
# dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_card)
#
# this introduces another problem because there is no way to specify the frame parameter that the function actually needs
# there is no way to pass a parameter when assigning a function this way.
# So by including (dealer_card_frame) in "command=deal_card(dealer_card_frame))", what you are doing is
# you are assigning the result of calling the function rather than assigning the function itself.
# We want to assign the function so that it is executed when the button is clicked.
# Now the problem is you cannot use the parenthesis to specify an argument, and if you can't do that, then you have no way of specifying an argument

# since we only have two functions here, we can create one function for the
# player and one for the dealer and assign them to the corresponding button
# This is not the only approach e.g. in calculator that has lots of buttons, it would not be practical
# we will look at other solutions to this later.
# but for now, we will create two functions

# These functions call the function that we need with the required parameter, "dealer_card_frame" or "player_card_frame"

def deal_dealer():
    deal_card(dealer_card_frame)

def deal_player():
    deal_card(player_card_frame)

# NOTE: dealer_button and player_button are defined above.

# Now we will connect the buttons using "command=deal_dealer" without parenthesis () ==> "command=deal_dealer()"
# This is because we are assigning the function that will be executed when the button is actually clicked

# Dealer button

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)  # Add without parenthesis
dealer_button.grid(row=0, column=0)

# Player Button

player_button = tkinter.Button(button_frame, text="Player", command=deal_player)  # Add without parenthesis
player_button.grid(row=0, column=1)



# Mainloop to give control to tkinter for execution
mainWindow.mainloop()






# =================================================
# (1) Configuring functions and code in right order
# =================================================
# (2) And demostrating dangers of variable shadowing (using same variable name for global and local variables
# =================================================


# (1) from above code, we defined the functions (starting with def ) in chronological order as we discussed them.
# but it is good practice to create functions at the top, and then the code that will be using the functions at the bottom
# We will rearrange the code above with functions definitions at the top
# NOTE: I also removed most of the comments, so if you want explanation, you should look in code above

# (2) This program is only displaying the cards and not showing the totals of the player and dealer
# we will modify "# Function 4: Function to call player card" to try to calculate the totals
# and also demonstrate the dangers of local variables shadowing global variables


# We import random module because cards will be assigned in random

import random

# Then import tkinter

try:
    import tkinter
except ImportError:  # Python 2
    import Tkinter as tkinter

print(tkinter.TkVersion)  # How to check tkinter version. In our case, we have 8.6


# =====================================
# Function 1: Function to load images
# =====================================

def load_images(card_images):  # define function named "load_images" set to accept parameter to be named "card_images"
    suits = ['of_clubs', 'of_diamonds', 'of_hearts', 'of_spades']  # Note these names are case sensitive
    face_cards = ['jack', 'king', 'queen']

    # Remember we said that tkinter version 8.6 is needed to use png files, so we will put a test here

    if tkinter.TkVersion >= 8.6:
        extension = 'png'  # if 8.6 or later, use picture extension of "png". in our case, we have files with "svg" so I use "svg" here
    else:
        extension = 'ppm'  # if less than 8.6, use picture extension ppm

    # Now we will create first loop which says
    # For each suit, retrieve the image for the cards.

    for suit in suits:  # suits include 'hearts', 'clubs', 'diamonds', 'spades' defined above.
        # Another for loop to retrieve number of cards from 1 to 10 using range from 1 to 11 (last one excluded in range)
        for card in range(1, 11):
            # We retrieve names under folder "cardspng" on the left where images are stored
            # So for number 1 in range, we go to "cardspng", and retrieve in format {}_{}.{} which comes to "01_of_hearts.png"
            # suit is either 'hearts', 'clubs', 'diamonds', 'spades'
            # extension is either svg or ppm (should be svg in our case)
            # Names will be put in variable "name". format(str(card)) gets range and converts it to string to add to "name" in string format

            # Here we assign 0 behind number if its less than 10, because our files start with 01, 02, 03 etc

            if card < 10:
                card = "0" + str(card)
            else:
                card = str(card)

            # First placement {} gets "card" (01 for first iteration)
            # Second placement {} gets "suit" (first one is "of_clubs")
            # Third placement {} gets "extension" which is "png" in our case because we have tkinter 8.6 and our files are in png

            name = 'cardspng/{}_{}.{}'.format(card, suit, extension)
            print(name)  # We can print to see what is in file "name" although this is optional

            # Now we extract the images themselves and store them in "images" variable.
            # We extract images using method named tkinter.PhotoImage
            # Image will be extracted using variable "name" we created above

            image = tkinter.PhotoImage(file=name)

            # Now we append the images from variable "image" above to "card_images" which is the parameter that
            # function "def load_images(card_images)" takes
            # This means we are retrieving card_images and giving them to function 'load_images" for it to load and print them.
            # they will be added in format "card, image". So first iteration will be 1, image, then 2 image etc

            card_images.append((card, image,))

        # We let above loop "for card in range(1, 11)" finish and then do a loop to retrieve face cards
        # face_cards are from function "def load_images" and are "face_cards = ['jack', 'king', 'queen']"

        for card in face_cards:
            # Since our images have extension_en e.g. jack_of_clubs_en.png
            # we added the third placement here to add "en"
            # First placement {} gets "str(card) i.e. card value (jack, king or queen) converted to string
            # Second placement {} gets "suit" (of_clubs, of_diamonds etc) from here: suits = ['of_clubs', 'of_diamonds', 'of_hearts', 'of_spades']
            # Third placement {} gets string "en"
            # Fourth placement {} gets extension, "png" in our case since we have tkinter 8.6

            name = 'cardspng/{}_{}_{}.{}'.format(str(card), suit, "en", extension)
            print(name)  # We can print to see what is in file "name" although this is optional
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


# Now we need to create some functions that will drive the game

# =================================================
# Function 2: Function to deal cards to players
# =================================================

# We start with function to deal cards to players each time their button is clicked.
# We are going to make a function called "dealer_card"

# This function has a single parameter i.e. the "frame" that the image should be displayed on

def deal_card(frame):  # takes parameter "frame" which is the frame that the card will be displayed on.
    # We pop the next card off the top of the deck.
    # https://docs.python.org/2/tutorial/datastructures.html (for .pop description)
    # pop() is a way to retrieve an item from a list and also remove it from the list at the same time
    # it is the opposite of append which adds an item to the list
    # pop takes an item from the specified position in the list defaulting to the end if the position to be taken from is not specified
    # By specifying position 0, we can take cards from the top of the deck
    # If you leave () without anything, you will pop the card from the bottom of the deck
    # Both append and pop can also be used with an index to add or remove from the specified position
    next_card = deck.pop(0)

    # Once the next_card has been retrieved from the deck, the function creates a tkinter label in the frame that is passed to the function
    # and sets its image to the photo image stored in the next_card tuple.
    # The label is then "packed" against the left side of the frame so that all cards should stack against each other from left to right
    # as they are being added. With the newest one to the left.
    # Now we add image to a label and display the label. So we will actually see what that card is.
    # We pass "frame" to this label. This is the parameter that was passed to "dealer_card"
    # Image=next_card[1]
    # Use "pack" geometry manager to place the label text within the window on the left side. options are top, bottom, left, right
    # We use "pack" instead of using "grid" to place the label.
    # NOTE it is not advisable to use "pack" and "grid" in the same window as it will give an error. But you can use "pack" in its own window
    # Since every widget is a window, packing these images into this frame is fine as long as we don't try to add anything else to the frame using grid
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')

    # The function then returns the next_card tuple so that whatever is calling it can also check the face value of the card.
    # Now return the cards face value
    return next_card

# ====================================================
# Now we need to link up the functions to the buttons
# ====================================================
#
# A "function" is associated with a "widget" using the "command" property
# it would be tempting to go to the dealer_button function and add "command=deal_card(dealer_card_frame)"
#
# dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_card(dealer_card_frame))
#
# however you have to be careful when setting up the "command' property widgets
# The value that you assign has to be the function that you want to execute when the button is clicked.
# So you don't want to call the function instead of assigning it the command
# So by attempting to pass the frame to the function ==> command=deal_card(dealer_card_frame)) => at the same time as assigning
# The function of the button
#
# So the correct code would be without passing dealer_card_frame
#
# dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_card)
#
# this introduces another problem because there is no way to specify the frame parameter that the function actually needs
# there is no way to pass a parameter when assigning a function this way.
# So by including (dealer_card_frame) in "command=deal_card(dealer_card_frame))", what you are doing is
# you are assigning the result of calling the function rather than assigning the function itself.
# We want to assign the function so that it is executed when the button is clicked.
# Now the problem is you cannot use the parenthesis to specify an argument, and if you can't do that, then you have no way of specifying an argument

# since we only have two functions here, we can create one function for the
# player and one for the dealer and assign them to the corresponding button
# This is not the only approach e.g. in calculator that has lots of buttons, it would not be practical
# we will look at other solutions to this later.
# but for now, we will create two functions

# These functions call the function that we need with the required parameter, "dealer_card_frame" or "player_card_frame"

# ====================================
# Function 3: function to dealer card
# ====================================

def deal_dealer():
    deal_card(dealer_card_frame)

# =========================================
# Function 4: Function to call player card
# =========================================

# This was the original code to display card without calculating player totals
# def deal_player():
#     deal_card(player_card_frame)

# We will modify it here to calculate player totals and also demonstrate danger or local variables shadowing global variables

# The best place to calculate players totals is just after every card is dealt
# the face value of a card can be obtained from the tuple returned by the "deal_card" function
# and that can be used to update the players totals
# The code also has to deal with the two values that an Ace can represent i.e. 1 or 11.
# This is not difficult in blackjack, because no matter how many Aces a player has, only one of them can have the value of 11
# otherwise if he has two with 11, total will be 22, which is higher than Max allowed 21 and player will go bust.
# So the technique we can use here is to give the first Ace value 11 and any subsequent Aces value of 1
# If the player goes bust by holding at least one Ace, 10 subtracted from the total and a check for being bust (>21) is performed again.
# So it will give the player to treat an Ace as 1 instead of 10 = 11 (Ace with 11) - 1 (subsequent Ace with 1)

# In order to do this, we need two more variables.
# One to store the players totals, and other to track whether the player holds an Ace that has the value of 11

# First we go down to line "player_score_label = tkinter.IntVar()" and add some global variables
# These are "player_score" and player_ace" (That tracks if customer has an Ace in their hand)
# NOTE that we will also use a local variable named "player_score" in function "deal_player" below to help demonstrate dangers of shadowing

def deal_player():
    # Initialize local variable "player_score" to 0. NOTE it has same name as global variable "player_score" defined after "player_score_label = tkinter.IntVar()
    # This will demonstrate the dangers of local variables shadowing global variables.

    player_score = 0

    # We assign result from "deal_card" function to variable "card_value"
    # Note that we use [0] to specify position 0 of the card which lists the Number of the card e.g. 01_of_clubs, position 0 has card number 01
    # Also note that values in position 0 may be strings. So we convert them to integers using int() before adding them to card_value

    card_value = int(deal_card(player_card_frame)[0])

    # You can optionally print card_value and player_ace value to see them with each iteration
    # print("card value is {}".format(card_value))
    # print("Ace value is {}".format(player_ace))

    # Now we do some checking
    # if "card_value" obtained from deal_card function above is not equal to 1,
    # And is not an Ace (player_ace, currently a global variable initialized as False) i.e. Player does not have an Ace in their Hand
    # Then we assign card value to 11.
    # This means if first card is an Ace with value 1, and player does not have an Ace in their hand, we assign that Ace value 11
    if card_value == 1 and not player_ace:
        card_value = 11

        # NOTE: Say we got Ace card above and want to assign player_ace to be True.
        # If we use this command, we see there is an error.
        # We are getting this error because when we try to modify global variable "player_ace", python creates a local variable
        # with same name and stores it in the function.
        # The error comes about because of line "if card_value == 1 and not player_ace" where we tried to compare to "player_ace"
        # which is now turned into a local variable, and "player_ace" is not initialized in the function like we initialized "player_score"
        # Hence the error message of referring to undefined local variable.
        # We will comment out this line for now.

        # player_ace = True

    # Now we are going to update variable "player_score", initialized as 0 above, with the value of the card from "card_value"

    player_score += card_value  # Adding card_value to player_score

    # If player is bust i.e. has more than 21, check if he has an ace and subtract 10

    if player_score > 21 and player_ace:  # if player_score > 21 and he has an Ace i.t. player_ace is True
        player_score -= 10  # We remove 10 from player_score
    player_score_label.set(player_score)  # Then we update player_score_label with new player_score
    if player_score > 21:  # If player score is still more than 21 even after removing 10
        result_text.set("Dealer Wins")  # update result_text to say Dealer has won, because player is bust.

    # NOTE: When we run the code now, and click player several times
    # We see that it is diplaying the value of the last card displayed and not the total of all the cards
    # This is because we used local variable "player_score" under function "def deal_player()" and it overode
    # the global variable "player_score". So the local variable is being zeroed out every time function deal_player()
    # iterates hence it only stores the last card

    # NOTE: that intellij does not give shadowing warning for "player_ace" like it gives for "player_score"
    # because the function above does not Assign anything to "player_ace" like it assigns values to "player_score.
    # If you are trying to use a global variable in a function, python will let you do that but as soon as you try to
    # assign anything to that global variable from the function, python creates a local variable with the same name
    # and you can no longer refer to the global variable.

    # A Good way to determine if a variable is global or local is to CTRL+click it.
    # It will take you to the place where it is defined e.g. if you CTRL+click player_ace, it takes you to global variable below
    # Do same for player_score, it takes you to local variable.

    # You can also use command below to print local variables.
    # In this case, we see card_value and player_score are both local, hence we are not using the global player_score
    # This will give result like this to show card value and player score value
    # NOTE at this time, both have same value because player_score is being zeroed out and only prints the last card put in it.
    # {'card_value': 8, 'player_score': 8}

    print(locals())



# ===============================================

# NOTE: dealer_button and player_button are defined above.
# After defining abovefunctions 3 & 4, we will connect the buttons
# using "command=deal_dealer" without parenthesis () ==> "command=deal_dealer()"
# This is because we are assigning the function that will be executed when the button is actually clicked

# Also NOTE that the mainWindow command below should be placed after all the functions have been defined
# We will later talk about having a "main Function"  to put the code that is not directly in functions.

# we set up mainWindow.

mainWindow = tkinter.Tk()



# =======================================================
# Set up screen and frame for the dealer and player
# =======================================================

mainWindow.title("Black Jack")  # Define title for mainWindow
mainWindow.geometry("640x480")  # Set up dimensions for the mainWindow (Note its in string format under "")
mainWindow.configure(background="green") #  NOTE: you can configure background of mainWindow here. in this case it is green.
result_text = tkinter.StringVar()  # http://effbot.org/tkinterbook/variable.htm
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# Embedded frame to hold the card images

dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

# We will add "global" variables "player_score" and "player_ace" here

player_score_label = tkinter.IntVar()
player_score = 0    # To track players score. Initialize to zero.
player_ace = False  # To track if player has Ace in their hand. initialize it to false

tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

# Embedded frame to hold the card images and frame

player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

# Embedded frame to hold buttons

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

# NOTE: See explanation for "command=deal_dealer" and "command=deal_player" in above program

# Dealer button

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)  # Add without parenthesis
dealer_button.grid(row=0, column=0)

# Player Button

player_button = tkinter.Button(button_frame, text="Player", command=deal_player)  # Add without parenthesis
player_button.grid(row=0, column=1)



# Now we can test to see if these images load

cards = []  # we start with empty list
load_images(cards)  # load images

# Then print to see we get for cards. This gives you "[('01', <tkinter.PhotoImage object at 0x0553FD10>),
# etc show placement of card objects

print(cards)


# A new deck of cards can be created from the cards that we imported
# Then we can shuffle them using the using the "Shuffle" function from the "random" module that we imported
# The program will also need to store the cards dealt to each player

# We will first initialize a dealer hand and player hand

# Create a new list named "deck" to store cards and shuffle them.
# NOTE we create new list (deck) that contains same info as list (cards)
# We separate this because as the cards in "deck" are shuffled and assigned, python will be decrementing them until there is nothing left
# So we need to have two separate list of cards so we are not left with nothing to shuffle

# NOTE that "cards" was initially an empty list and we loaded it with images from "load_images(cards)"
# Here we create a list called "deck" and assign it information in list "cards"
# NOTE you can create a list in two ways. Using square brackets and using "list" constructor
#       list_1 = ["a", "b"]    # using square brackets
#       list_2 = list(x)  # using list constructor and passing it agument

deck = list(cards)
random.shuffle(deck)  # Then we shuffle the "deck" list to make it random

# We create a list to store dealers and player's hands
# First we initialize them to empty list

dealer_hand = []
player_hand = []

# Mainloop to give control to tkinter for execution
mainWindow.mainloop()






# ===========================================================
# Rewriting function so it does not use global variables
# ===========================================================

# Ideally, a function should be self contained and not make changes to anything outside of itself
# And when a function changes things like global variables, the changes are known as "side effects"
# And these changes should be avoided whenever possible

# Python usually discourages changes to global variables by making local variables in the function
# if the function tries to make changes to the global variable

# However, sometimes these changes or "side effects" are necessary
# So python provides a way to make changes to global variables within a function
# We will see how to do this in function deal_player below




# We import random module because cards will be assigned in random

import random

# Then import tkinter

try:
    import tkinter
except ImportError:  # Python 2
    import Tkinter as tkinter

print(tkinter.TkVersion)  # How to check tkinter version. In our case, we have 8.6


# =====================================
# Function 1: Function to load images
# =====================================

def load_images(card_images):  # define function named "load_images" set to accept parameter to be named "card_images"
    suits = ['of_clubs', 'of_diamonds', 'of_hearts', 'of_spades']  # Note these names are case sensitive
    face_cards = ['jack', 'king', 'queen']

    # Remember we said that tkinter version 8.6 is needed to use png files, so we will put a test here

    if tkinter.TkVersion >= 8.6:
        extension = 'png'  # if 8.6 or later, use picture extension of "png". in our case, we have files with "svg" so I use "svg" here
    else:
        extension = 'ppm'  # if less than 8.6, use picture extension ppm

    # Now we will create first loop which says
    # For each suit, retrieve the image for the cards.

    for suit in suits:  # suits include 'hearts', 'clubs', 'diamonds', 'spades' defined above.
        # Another for loop to retrieve number of cards from 1 to 10 using range from 1 to 11 (last one excluded in range)
        for card in range(1, 11):
            # We retrieve names under folder "cardspng" on the left where images are stored
            # So for number 1 in range, we go to "cardspng", and retrieve in format {}_{}.{} which comes to "01_of_hearts.png"
            # suit is either 'hearts', 'clubs', 'diamonds', 'spades'
            # extension is either svg or ppm (should be svg in our case)
            # Names will be put in variable "name". format(str(card)) gets range and converts it to string to add to "name" in string format

            # Here we assign 0 behind number if its less than 10, because our files start with 01, 02, 03 etc

            if card < 10:
                card = "0" + str(card)
            else:
                card = str(card)

            # First placement {} gets "card" (01 for first iteration)
            # Second placement {} gets "suit" (first one is "of_clubs")
            # Third placement {} gets "extension" which is "png" in our case because we have tkinter 8.6 and our files are in png

            name = 'cardspng/{}_{}.{}'.format(card, suit, extension)
            print(name)  # We can print to see what is in file "name" although this is optional

            # Now we extract the images themselves and store them in "images" variable.
            # We extract images using method named tkinter.PhotoImage
            # Image will be extracted using variable "name" we created above

            image = tkinter.PhotoImage(file=name)

            # Now we append the images from variable "image" above to "card_images" which is the parameter that
            # function "def load_images(card_images)" takes
            # This means we are retrieving card_images and giving them to function 'load_images" for it to load and print them.
            # they will be added in format "card, image". So first iteration will be 1, image, then 2 image etc

            card_images.append((card, image,))

        # We let above loop "for card in range(1, 11)" finish and then do a loop to retrieve face cards
        # face_cards are from function "def load_images" and are "face_cards = ['jack', 'king', 'queen']"

        for card in face_cards:
            # Since our images have extension_en e.g. jack_of_clubs_en.png
            # we added the third placement here to add "en"
            # First placement {} gets "str(card) i.e. card value (jack, king or queen) converted to string
            # Second placement {} gets "suit" (of_clubs, of_diamonds etc) from here: suits = ['of_clubs', 'of_diamonds', 'of_hearts', 'of_spades']
            # Third placement {} gets string "en"
            # Fourth placement {} gets extension, "png" in our case since we have tkinter 8.6

            name = 'cardspng/{}_{}_{}.{}'.format(str(card), suit, "en", extension)
            print(name)  # We can print to see what is in file "name" although this is optional
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


# Now we need to create some functions that will drive the game

# =================================================
# Function 2: Function to deal cards to players
# =================================================

# We start with function to deal cards to players each time their button is clicked.
# We are going to make a function called "dealer_card"

# This function has a single parameter i.e. the "frame" that the image should be displayed on

def deal_card(frame):  # takes parameter "frame" which is the frame that the card will be displayed on.
    # We pop the next card off the top of the deck.
    # https://docs.python.org/2/tutorial/datastructures.html (for .pop description)
    # pop() is a way to retrieve an item from a list and also remove it from the list at the same time
    # it is the opposite of append which adds an item to the list
    # pop takes an item from the specified position in the list defaulting to the end if the position to be taken from is not specified
    # By specifying position 0, we can take cards from the top of the deck
    # If you leave () without anything, you will pop the card from the bottom of the deck
    # Both append and pop can also be used with an index to add or remove from the specified position
    next_card = deck.pop(0)

    # Once the next_card has been retrieved from the deck, the function creates a tkinter label in the frame that is passed to the function
    # and sets its image to the photo image stored in the next_card tuple.
    # The label is then "packed" against the left side of the frame so that all cards should stack against each other from left to right
    # as they are being added. With the newest one to the left.
    # Now we add image to a label and display the label. So we will actually see what that card is.
    # We pass "frame" to this label. This is the parameter that was passed to "dealer_card"
    # Image=next_card[1]
    # Use "pack" geometry manager to place the label text within the window on the left side. options are top, bottom, left, right
    # We use "pack" instead of using "grid" to place the label.
    # NOTE it is not advisable to use "pack" and "grid" in the same window as it will give an error. But you can use "pack" in its own window
    # Since every widget is a window, packing these images into this frame is fine as long as we don't try to add anything else to the frame using grid
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')

    # The function then returns the next_card tuple so that whatever is calling it can also check the face value of the card.
    # Now return the cards face value
    return next_card

# ====================================================
# Now we need to link up the functions to the buttons
# ====================================================
#
# A "function" is associated with a "widget" using the "command" property
# it would be tempting to go to the dealer_button function and add "command=deal_card(dealer_card_frame)"
#
# dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_card(dealer_card_frame))
#
# however you have to be careful when setting up the "command' property widgets
# The value that you assign has to be the function that you want to execute when the button is clicked.
# So you don't want to call the function instead of assigning it the command
# So by attempting to pass the frame to the function ==> command=deal_card(dealer_card_frame)) => at the same time as assigning
# The function of the button
#
# So the correct code would be without passing dealer_card_frame
#
# dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_card)
#
# this introduces another problem because there is no way to specify the frame parameter that the function actually needs
# there is no way to pass a parameter when assigning a function this way.
# So by including (dealer_card_frame) in "command=deal_card(dealer_card_frame))", what you are doing is
# you are assigning the result of calling the function rather than assigning the function itself.
# We want to assign the function so that it is executed when the button is clicked.
# Now the problem is you cannot use the parenthesis to specify an argument, and if you can't do that, then you have no way of specifying an argument

# since we only have two functions here, we can create one function for the
# player and one for the dealer and assign them to the corresponding button
# This is not the only approach e.g. in calculator that has lots of buttons, it would not be practical
# we will look at other solutions to this later.
# but for now, we will create two functions

# These functions call the function that we need with the required parameter, "dealer_card_frame" or "player_card_frame"

# ====================================
# Function 3: function to dealer card
# ====================================

def deal_dealer():
    deal_card(dealer_card_frame)

# ====================================================================================
# Function 4: Function to call player card - Changing global variables in a function
# ====================================================================================

# Sometimes these changes or "side effects" are necessary
# So python provides a way to make changes to global variables within a function
# We will see how to do this in function deal_player below

# We change global variables by specifying that we intend to
# use global variables by using the "global" keyword.


def deal_player():
    # These two commands tells python to use the global versions of variable "player_score" and "player_ace"
    # instead of creating local variables with the same names.

    global player_score
    global player_ace

    # Now we see even if we did not initialize the "player_score" and "player_ace" in this function
    # There is no error because it will reference the global variables and there is no more shadowing
    # Also we see we can change both variables and it will change global variables
    # When you run this command now, you will see that the Totals are being updated

    card_value = int(deal_card(player_card_frame)[0])
    if card_value == 1 and not player_ace:
        player_ace = True  # we can update value of player_ace to True if an Ace card is picked
        card_value = 11

    player_score += card_value  # Adding card_value to player_score

    # If player is bust i.e. has more than 21, check if he has an ace and subtract 10

    if player_score > 21 and player_ace:  # if player_score > 21 and he has an Ace i.t. player_ace is True
        player_score -= 10  # We remove 10 from player_score
        player_ace = False  # Also remember to set player_ace to False after you remove the Ace

    player_score_label.set(player_score)  # Then we update player_score_label with new player_score
    if player_score > 21:  # If player score is still more than 21 even after removing 10
        result_text.set("Dealer Wins")  # update result_text to say Dealer has won, because player is bust.

    # You can also use command below to print local variables.
    # We see the local variable printed here is only card_value.

    print(locals())

# NOTE: After you run the command several times, you will see that after players score passes 21
# There is a message displayed saying "Dealer Wins"

# NOTE: Although this code for "deal_player" function works, there is no way of knowing that only
# function "deal_player" is modifying global variables "player_score" and "player_ace"
# And if another function is modifying these global variables, then the results for function "deal_player" will not be accurate
# This is why "side effects" (modifying global variables in outer scope from a function) are discouraged



# ===============================================

# NOTE: dealer_button and player_button are defined above.
# After defining abovefunctions 3 & 4, we will connect the buttons
# using "command=deal_dealer" without parenthesis () ==> "command=deal_dealer()"
# This is because we are assigning the function that will be executed when the button is actually clicked

# Also NOTE that the mainWindow command below should be placed after all the functions have been defined
# We will later talk about having a "main Function"  to put the code that is not directly in functions.

# we set up mainWindow.

mainWindow = tkinter.Tk()



# =======================================================
# Set up screen and frame for the dealer and player
# =======================================================

mainWindow.title("Black Jack")  # Define title for mainWindow
mainWindow.geometry("640x480")  # Set up dimensions for the mainWindow (Note its in string format under "")
mainWindow.configure(background="green") #  NOTE: you can configure background of mainWindow here. in this case it is green.
result_text = tkinter.StringVar()  # http://effbot.org/tkinterbook/variable.htm
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# Embedded frame to hold the card images

dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

# We will add "global" variables "player_score" and "player_ace" here

player_score_label = tkinter.IntVar()
player_score = 0    # To track players score. Initialize to zero.
player_ace = False  # To track if player has Ace in their hand. initialize it to false

tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

# Embedded frame to hold the card images and frame

player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

# Embedded frame to hold buttons

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

# NOTE: See explanation for "command=deal_dealer" and "command=deal_player" in above program

# Dealer button

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)  # Add without parenthesis
dealer_button.grid(row=0, column=0)

# Player Button

player_button = tkinter.Button(button_frame, text="Player", command=deal_player)  # Add without parenthesis
player_button.grid(row=0, column=1)



# Now we can test to see if these images load

cards = []  # we start with empty list
load_images(cards)  # load images

# Then print to see we get for cards. This gives you "[('01', <tkinter.PhotoImage object at 0x0553FD10>),
# etc show placement of card objects

print(cards)


# A new deck of cards can be created from the cards that we imported
# Then we can shuffle them using the using the "Shuffle" function from the "random" module that we imported
# The program will also need to store the cards dealt to each player

# We will first initialize a dealer hand and player hand

# Create a new list named "deck" to store cards and shuffle them.
# NOTE we create new list (deck) that contains same info as list (cards)
# We separate this because as the cards in "deck" are shuffled and assigned, python will be decrementing them until there is nothing left
# So we need to have two separate list of cards so we are not left with nothing to shuffle

# NOTE that "cards" was initially an empty list and we loaded it with images from "load_images(cards)"
# Here we create a list called "deck" and assign it information in list "cards"
# NOTE you can create a list in two ways. Using square brackets and using "list" constructor
#       list_1 = ["a", "b"]    # using square brackets
#       list_2 = list(x)  # using list constructor and passing it agument

deck = list(cards)
random.shuffle(deck)  # Then we shuffle the "deck" list to make it random

# We create a list to store dealers and player's hands
# First we initialize them to empty list

dealer_hand = []
player_hand = []


# Mainloop to give control to tkinter for execution
mainWindow.mainloop()







# =============================================================
# Using function to calculate score for both dealer and player
# =============================================================


# Now that we have made code to keep player_score in above code, we will need to do same for dealer
# So it makes sense to create a function to keep track of the score, both dealer and player and maybe more players

# We will make a new function called "score_hand" to look at a hand and calculate a score based on that hand
# We will create function "score_hand" right under "deal_card"


# We import random module because cards will be assigned in random

import random

# Then import tkinter

try:
    import tkinter
except ImportError:  # Python 2
    import Tkinter as tkinter

print(tkinter.TkVersion)  # How to check tkinter version. In our case, we have 8.6


# =====================================
# Function 1: Function to load images
# =====================================

def load_images(card_images):  # define function named "load_images" set to accept parameter to be named "card_images"
    suits = ['of_clubs', 'of_diamonds', 'of_hearts', 'of_spades']  # Note these names are case sensitive
    face_cards = ['jack', 'king', 'queen']

    # Remember we said that tkinter version 8.6 is needed to use png files, so we will put a test here

    if tkinter.TkVersion >= 8.6:
        extension = 'png'  # if 8.6 or later, use picture extension of "png". in our case, we have files with "svg" so I use "svg" here
    else:
        extension = 'ppm'  # if less than 8.6, use picture extension ppm

    # Now we will create first loop which says
    # For each suit, retrieve the image for the cards.

    for suit in suits:  # suits include of_clubs', 'of_diamonds', 'of_hearts', 'of_spades' defined above.
        # Another for loop to retrieve number of cards from 1 to 10 using range from 1 to 11 (last one excluded in range)
        for card in range(1, 11):
            # We retrieve names under folder "cardspng" on the left where images are stored
            # So for number 1 in range, we go to "cardspng", and retrieve in format {}_{}.{} which comes to "01_of_hearts.png"
            # suit is either 'of_hearts', 'of_clubs', 'of_diamonds', 'of_spades'
            # extension is either png or ppm (should be png in our case)

            # Here we assign 0 behind number if its less than 10, because our files start with 01, 02, 03 etc

            if card < 10:
                card = "0" + str(card)
            else:
                card = str(card)

            # First placement {} gets "card" (01 for first iteration)
            # Second placement {} gets "suit" (first one is "of_clubs")
            # Third placement {} gets "extension" which is "png" in our case because we have tkinter 8.6 and our files are in png

            # Names will be put in variable "name". format(str(card)) gets range and converts it to string to add to "name" in string format

            name = 'cardspng/{}_{}.{}'.format(card, suit, extension)
            print(name)  # We can print to see what is in file "name" although this is optional

            # Now we extract the images themselves and store them in "images" variable.
            # We extract images using method named tkinter.PhotoImage
            # Image will be extracted using variable "name" we created above

            image = tkinter.PhotoImage(file=name)

            # Now we append the images from variable "image" above to "card_images" which is the parameter that
            # function "def load_images(card_images)" takes
            # This means we are retrieving card_images and giving them to function 'load_images" for it to load and print them.
            # they will be added in format "card, image". So first iteration will be 1, image, then 2 image etc
            # "card" is the card number.

            card_images.append((card, image,))

        # We let above loop "for card in range(1, 11)" finish and then do a loop to retrieve face cards
        # face_cards are from function "def load_images" and are "face_cards = ['jack', 'king', 'queen']"

        for card in face_cards:
            # Since our images have extension_en e.g. jack_of_clubs_en.png
            # we added the third placement here to add "en"
            # First placement {} gets "str(card) i.e. card value (jack, king or queen) converted to string
            # Second placement {} gets "suit" (of_clubs, of_diamonds etc) from here: suits = ['of_clubs', 'of_diamonds', 'of_hearts', 'of_spades']
            # Third placement {} gets string "en"
            # Fourth placement {} gets extension, "png" in our case since we have tkinter 8.6

            name = 'cardspng/{}_{}_{}.{}'.format(str(card), suit, "en", extension)
            print(name)  # We can print to see what is in file "name" although this is optional
            image = tkinter.PhotoImage(file=name)

            # NOTE: 10 is the value of the card. Here it looks like all the "face_cards" have the value of 10

            card_images.append((10, image,))


# Now we need to create some functions that will drive the game

# =================================================
# Function 2: Function to deal cards to players
# =================================================

# We start with function to deal cards to players each time their button is clicked.
# We are going to make a function called "deal_card"

# This function has a single parameter i.e. the "frame" that the image should be displayed on

def deal_card(frame):  # takes parameter "frame" which is the frame that the card will be displayed on.
    # We pop the next card off the top of the deck.
    # https://docs.python.org/2/tutorial/datastructures.html (for .pop description)
    # pop() is a way to retrieve an item from a list and also remove it from the list at the same time
    # it is the opposite of append which adds an item to the list
    # pop takes an item from the specified position in the list defaulting to the end if the position to be taken from is not specified
    # By specifying position 0, we can take cards from the top of the deck
    # If you leave () without anything, you will pop the card from the bottom of the deck
    # Both append and pop can also be used with an index to add or remove from the specified position
    next_card = deck.pop(0)

    # Once the next_card has been retrieved from the deck, the function creates a tkinter label in the frame that is passed to the function
    # and sets its image to the photo image stored in the next_card tuple.
    # The label is then "packed" against the left side of the frame so that all cards should stack against each other from left to right
    # as they are being added. With the newest one to the left.
    # Now we add image to a label and display the label. So we will actually see what that card is.
    # We pass "frame" to this label. This is the parameter that was passed to "dealer_card"
    # Image=next_card[1]
    # Use "pack" geometry manager to place the label text within the window on the left side. options are top, bottom, left, right
    # We use "pack" instead of using "grid" to place the label.
    # NOTE it is not advisable to use "pack" and "grid" in the same window as it will give an error. But you can use "pack" in its own window
    # Since every widget is a window, packing these images into this frame is fine as long as we don't try to add anything else to the frame using grid
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')

    # The function then returns the next_card tuple so that whatever is calling it can also check the face value of the card.
    # Now return the cards face value
    return next_card

# ====================================================
# Now we need to link up the functions to the buttons
# ====================================================
#
# A "function" is associated with a "widget" using the "command" property
# it would be tempting to go to the dealer_button function and add "command=deal_card(dealer_card_frame)"
#
# dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_card(dealer_card_frame))
#
# however you have to be careful when setting up the "command' property widgets
# The value that you assign has to be the function that you want to execute when the button is clicked.
# So you don't want to call the function instead of assigning it the command
# So by attempting to pass the frame to the function ==> command=deal_card(dealer_card_frame)) => at the same time as assigning
# The function of the button
#
# So the correct code would be without passing dealer_card_frame
#
# dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_card)
#
# this introduces another problem because there is no way to specify the frame parameter that the function actually needs
# there is no way to pass a parameter when assigning a function this way.
# So by including (dealer_card_frame) in "command=deal_card(dealer_card_frame))", what you are doing is
# you are assigning the result of calling the function rather than assigning the function itself.
# We want to assign the function so that it is executed when the button is clicked.
# Now the problem is you cannot use the parenthesis to specify an argument, and if you can't do that, then you have no way of specifying an argument

# since we only have two functions here, we can create one function for the
# player and one for the dealer and assign them to the corresponding button
# This is not the only approach e.g. in calculator that has lots of buttons, it would not be practical
# we will look at other solutions to this later.
# but for now, we will create two functions

# These functions call the function that we need with the required parameter, "dealer_card_frame" or "player_card_frame"


# ====================================
# Function 5: function score_hand
# ====================================

# This function returns a score when given a list of cards
# it will be given a hand, and calculate a score based on that hand

def score_hand(hand):  # We give it parameter called "hand"
    # Calculate the total score of all cards in the list
    # Only one Ace can have value of 11, and this will be reduced to 1 if the hand would bust (go over 21)
    # We are going to create local variables "score" and "ace" and initialize them.

    print("calling function 'score_hand'")
    print("-------------")

    score = 0  # initialize score to 0 because there is initially no score
    ace = False  # Ace is initialized to false because we don't have any cards

    # Now we will go through all the cards one after another

    for next_card in hand:

        print("next_card = : {}".format(next_card))  # Optional print to see tuple

        card_value = next_card[0]  # We assign card_value the integer of next_card e.g. if 01_of_clubs, we assign position 0 which is 01

        print("next_card[0] = : {}".format(card_value))  # optional print to see position 0
        print("next_card[1] = : {}".format(next_card[1]))  # optional print to see position 1

        if card_value == "01" and not ace: # if we get card value 1 and don't already have an Ace (initially ace = False)
            ace = True  # Then we make ace to be True (because we now have an Ace)
            card_value = 11  # And make card_value to be 11
        else:
            card_value = int(card_value)  # Here we convert card value from string to integer

            print("next_card[0] integer : {}".format(card_value))  # optional print to see position 0 converted to integer

        # Then we add the score
        score += card_value  # we add card value to the score.

        print("Score Total = : {}".format(score))
        print("-----------------------")

        # If we bust (score > 21), check if there is ace and subtract 10

        if score > 21 and ace:  # if score is >21 and ace = True (there is an Ace)
            score -= 10  # remove 10 from score
            print("score after removing 10 = {}".format(score))  # optional print to check score after removing 10
            ace = False  # Make ace to False because we removed it

    # After the whole loop runs, it returns total score in variable "score"
    # NOTE: This code should be at same indent as the "for next_card in hand" loop
    # Otherwise you will not see the scores incrementing

    return score

# Now we will go to function "deal_player" and "deal_dealer" and make them use function "score_hand" to calculate score.




# ====================================
# Function 3: function to dealer card
# ====================================

def deal_dealer():

    print("--------------------------")
    print("Initial: dealer_hand: = {}".format(dealer_hand))  # Optional: Initially there is nothing.
    print("-------------")

    dealer_hand.append(deal_card(dealer_card_frame))  # We append deal_card with dealer_card_frame

    print("Appended: dealer_hand: {}".format(dealer_hand))  # optional. Appended dealer hand shows object appended to dealer_hand
    print("-------------")

    dealer_score = score_hand(dealer_hand)

    print("-------------")
    print("dealer_score = : {}".format(dealer_score))
    print("-------------")

    print("Initial: dealer_score_label: = {}".format(dealer_score_label))  # optional. Gives result PY_VAR1, a reference to intvar
    py_var1 = dealer_score_label.get()
    print("Initial PY_VAR1 = dealer_score_label.get(): = {}".format(py_var1))
    print("-------------")

    dealer_score_label.set(dealer_score)  # Here we use ".set" function to set value of "dealer_score_label" to "dealer_score"

    # Now we check to see if its game over

    player_score = score_hand(player_hand)  # This gives you the current player_score

    # Now we test to see who wins
    # If player_score is > 21, they bust and Dealer wins

    if player_score > 21:
        result_text.set("Dealer Wins !")  # Displays "Dealer wins" in result_text

    # if dealer score is more than 21 (bust) or less than player_score, then player wins

    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins !")  # We display "Player wins" in result_text

    # But if bothh have not bust and dealer score is greater than player score, then dealer wins

    elif dealer_score > player_score:
        result_text.set("Dealer Wins !")  # Display "dealer wins" in result_text

    # Other option is if both draw.
    else:
        result_text.set("Draw !")




# =========================================
# Function 3 - deal_dealer (Another way
# =========================================

# This function is supposed to make the dealer_cards get new card automatically
# player just need to click his cards



def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:  # if score is less than 17, dealer will automatically grab another card
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer wins !")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins ! ")
    elif dealer_score > player_score:
        result_text.set("Dealer Wins !")
    else:
        result_text.set("Draw !")



# ====================================================================================
# Function 4: deal_player - to call player cards and calculate player score
# ====================================================================================

# The logic of this function will change, since we are now using "score_hand" function to calculate score
# if you want to see original logic without "score_hand", check code above.

def deal_player():

    print("=" * 60)
    print("Initial player_hand: {}".format(player_hand))  # optional. initial player hand is a list with nothing
    print("-------------")
    # "deal_card" function returns "next_card"
    # "player_card_frame" is Embedded frame to hold the card images and frame
    # So here we take "player_hand" which is initially a global list defined below with nothing
    # Then append to it "deal_card" function, which returns "next_card", hence we are appending "next_card" to "player_hand"
    # but we pass "player_card_frame" to "deal_card" to add it to frame

    player_hand.append(deal_card(player_card_frame))

    print("Appended player_hand: {}".format(player_hand))  # optional. Appended player hand shows object appended to player_hand
    print("-------------")

    # Now we create a local variable called "player_score" to track player score
    # We assign it result from "score_hand" given parameter "player_hand"
    # "score_hand" returns score and is passed "player_hand" which is the appended "player_hand"

    player_score = score_hand(player_hand)

    print("-------------")
    print("score_hand = : {}".format(score_hand))  # result shows " <function score_hand at 0x055B3108>"
    print("player_hand = : {}".format(player_hand))  # result shows "[('08', <tkinter.PhotoImage object at 0x05872910>)]" for first card
    print("player_score = score_hand(player_hand) = : {}".format(player_score))  # result show 8 for first card (or whatever card is first)
    print("-------------")
    # NOTE: "player_score_label = tkinter.IntVar()" displays the player score on the left side of the screen

    print("initial: player_score_label = : {}".format(player_score_label))  # optional. gives result "PY_VAR2", a reference object to intvar()
    py_var2 = player_score_label.get()  # optional. We use the "get" method to access what is in that reference object
    print("Initial: PY_VAR2 = player_score_label.get() = : {}".format(py_var2))
    print("-------------")

    player_score_label.set(player_score)  # Here we use ".set" function to set value of "player_score_label" to "player_score"

    print("New: player_score_label.set(player_score) = {}".format(player_score_label))  # Gives "PY_VAR2". a reference object to intvar()
    py_var2 = player_score_label.get()  # optional. We use the "get" method to access what is in that reference object
    print("New: PY_VAR2 = player_score_label.get() = {}".format(py_var2))  # Gives result of score after passing player_score to it

    if player_score > 21:  # Now we test if player goes bust and if true, we print results as "dealer wins"
        result_text.set("Dealer Wins! ")

    print("=" * 60)
# We will delete the global variables "player_score" and "player_ace" defined
# below code ==>  player_score_label = tkinter.IntVar()
# We don't need them anymore and intellij is flagging them for shadowing





# ===============================================

# NOTE: dealer_button and player_button are defined above.
# After defining abovefunctions 3 & 4, we will connect the buttons
# using "command=deal_dealer" without parenthesis () ==> "command=deal_dealer()"
# This is because we are assigning the function that will be executed when the button is actually clicked

# Also NOTE that the mainWindow command below should be placed after all the functions have been defined
# We will later talk about having a "main Function"  to put the code that is not directly in functions.

# we set up mainWindow.

mainWindow = tkinter.Tk()



# =======================================================
# Set up screen and frame for the dealer and player
# =======================================================

mainWindow.title("Black Jack")  # Define title for mainWindow
mainWindow.geometry("640x480")  # Set up dimensions for the mainWindow (Note its in string format under "")
mainWindow.configure(background="green") #  NOTE: you can configure background of mainWindow here. in this case it is green.
result_text = tkinter.StringVar()  # http://effbot.org/tkinterbook/variable.htm
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# Embedded frame to hold the card images

dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

# We will add "global" variables "player_score" and "player_ace" here in the player_score_label
# This is displayed at the left side of the screen after running code
# intvar returns integers

player_score_label = tkinter.IntVar()


tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

# Embedded frame to hold the card images and frame

player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

# Embedded frame to hold buttons

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

# NOTE: See explanation for "command=deal_dealer" and "command=deal_player" in above program

# Dealer button

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)  # Add without parenthesis
dealer_button.grid(row=0, column=0)

# Player Button

player_button = tkinter.Button(button_frame, text="Player", command=deal_player)  # Add without parenthesis
player_button.grid(row=0, column=1)



# Now we can test to see if these images load

cards = []  # we start with empty list
load_images(cards)  # load images

# Then print to see we get for cards. This gives you "[('01', <tkinter.PhotoImage object at 0x0553FD10>),
# etc show placement of card objects

print(cards)


# A new deck of cards can be created from the cards that we imported
# Then we can shuffle them using the using the "Shuffle" function from the "random" module that we imported
# The program will also need to store the cards dealt to each player

# We will first initialize a dealer hand and player hand

# Create a new list named "deck" to store cards and shuffle them.
# NOTE we create new list (deck) that contains same info as list (cards)
# We separate this because as the cards in "deck" are shuffled and assigned, python will be decrementing them until there is nothing left
# So we need to have two separate list of cards so we are not left with nothing to shuffle

# NOTE that "cards" was initially an empty list and we loaded it with images from "load_images(cards)"
# Here we create a list called "deck" and assign it information in list "cards"
# NOTE you can create a list in two ways. Using square brackets and using "list" constructor
#       list_1 = ["a", "b"]    # using square brackets
#       list_2 = list(x)  # using list constructor and passing it agument

deck = list(cards)
random.shuffle(deck)  # Then we shuffle the "deck" list to make it random

# We create a list to store dealers and player's hands
# First we initialize them to empty list

dealer_hand = []
player_hand = []

# NOTE: This is the code that is making us to have initial 2 player cards and 1 dealer card
# In the main program, we don't want the dealer to play their turn as the initial card is dealt
# we just want them to deal a card and store in their hand
# Here player will get two cards and the dealer will have one card

deal_player()  # one card for player
dealer_hand.append(deal_card(dealer_card_frame))  # one card for dealer
dealer_score_label.set(score_hand(dealer_hand))   # Displays the Card value of dealer in screen
deal_player()  # one card for player

# Mainloop to give control to tkinter for execution
mainWindow.mainloop()