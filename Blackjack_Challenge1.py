
# ===========================================
# Blackjack Challenge continued
# ===========================================

# =================================
# Modifying global variable lists
# =================================

# In this example, we see that "dealer_hand = []" and "player_hand = []" are initialized as "lists" on global.
# These lists are referenced by the program as global variables.
# but we see these global variable lists being modified by functions dealer_hand and player_hand on these lines and intellij does not give error
# "dealer_hand.append(deal_card(dealer_card_frame))" & "player_hand.append(deal_card(player_card_frame))"

# The reason why this is acceptable is because adding or removing items from a list is not considered as modifying the list variable
# The list always has the same value i.e. the list. The contents of the list can change
# Adding items to a global list is still a "side effect" but is not considered as dangerous as changing the list that the variable holds for example.
# lists exist to have items added or removed, hence this is acceptable behavior hence no warning from intellij


# =============================
# Challenge - destroy method
# =============================

# Add a new button to the program with the text "new_game"
# This button should call a function that clears the cards from the screen,
# resets the players and dealers hands and starts a new game.

# The easiest way to clear the contents of the frame is to destroy the frame and create a new one with the same name
# That is why the program has "player_card_frame" and "dealer_card_frame"

# we will create "new_game" after "deal_player" function



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

    # if you play many times. play and new game, you will run out of cards
    # And since we are not re-initializing the deck, the program will crash after the cards run out
    # Solution 1:
    # We re-initialize the deck every time we execute a new game. We will not do this
    # Solution 2:
    # Every time a card is dealt, it will be put at the bottoom of the deck, hence we are reusing same deck
    # We will do this in the "deal_card" function here

    deck.append(next_card)

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


# =====================
# "new_game" function
# =====================
# using "destroy" method

# We will create a new function called "new_game"
# Remember that most of the initialization code in the main program concerns setting up the  GUI
# Hence we don't need to repeat all that every time a new game is started.
# But the "dealer_card_frame" and "player_card_frame" will need to be cleared using the "destroy" method

def new_game():
    # We reference global variables with keyword "global" because we will be changing the global variables
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand

    # Embedded frame to hold the card images (dealer_card)
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

    # Embedded frame to hold the card images (player_card)
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

    # Create the list to store dealers and players hand
    # This code is similar to global one after dealer_hand = [] global definition

    dealer_hand = []
    player_hand = []

    deal_player()  # one card for player
    dealer_hand.append(deal_card(dealer_card_frame))  # one card for dealer
    dealer_score_label.set(score_hand(dealer_hand))   # Displays the Card value of dealer in screen
    deal_player()  # one card for player

# Now we will add button code with "new_game_button" (search below) after player_button

# ==========================
# Shuffle function
# ==========================

# We define the shuffle function here to shuffle the deck

def shuffle():
    random.shuffle(deck)


# ==========================

# NOTE: dealer_button and player_button are defined above.
# After defining abovefunctions 3 & 4, we will connect the buttons
# using "command=deal_dealer" without parenthesis () ==> "command=deal_dealer()"
# This is because we are assigning the function that will be executed when the button is actually clicked

# Also NOTE that the mainWindow command below should be placed after all the functions have been defined
# We will later talk about having a "main Function"  to put the code that is not directly in functions.

# ======================
# we set up mainWindow.
# ======================

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

# New Game button

new_game_button = tkinter.Button(button_frame, text="New Game", command=new_game)  # Add without parenthesis
new_game_button.grid(row=0, column=2)  # Add it to grid

# Shuffle button
# We can also add a button to shuffle the deck

shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle)
shuffle_button.grid(row=0, column=3)




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


# deck = list(cards) + list(cards) + list(cards)  # Optional. Can use this to have several packs of cards in the deck
deck = list(cards)
# random.shuffle(deck)  # Then we shuffle the "deck" list to make it random. NOTE: We comment this out because we are using shuffle function
shuffle()  # instead we will call the shuffle command which we defined above

# # NOTE that we comment out this code here because it was put in "new_game" function to avoid duplication
#
# # We create a list to store dealers and player's hands
# # First we initialize them to empty list
#
# dealer_hand = []
# player_hand = []
#
# # NOTE: This is the code that is making us to have initial 2 player cards and 1 dealer card
# # In the main program, we don't want the dealer to play their turn as the initial card is dealt
# # we just want them to deal a card and store in their hand
# # Here player will get two cards and the dealer will have one card
#
# deal_player()  # one card for player
# dealer_hand.append(deal_card(dealer_card_frame))  # one card for dealer
# dealer_score_label.set(score_hand(dealer_hand))   # Displays the Card value of dealer in screen
# deal_player()  # one card for player

# Now we can call "new_game" function

dealer_hand = []
player_hand = []

new_game()


# Mainloop to give control to tkinter for execution
mainWindow.mainloop()
