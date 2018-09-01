
# ===========================================
# Blackjack3.py
# ===========================================

# =================================================
# Creating module to put code repeated in
# "new_game" and "play" modules in "Blackjack2.py
# ================================================

# We know that this code below is in both modules "new_game" and "play" in "Blackjack2.py
# We want to create a function to put this code so it is just called in other modules instead of being repeated

    # deal_player()  # one card for player
    # dealer_hand.append(deal_card(dealer_card_frame))  # one card for dealer
    # dealer_score_label.set(score_hand(dealer_hand))   # Displays the Card value of dealer in screen
    # deal_player()  # one card for player

# We will put this code in a new module called "initial_deal"




# ========================================

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

    for suit in suits:  # suits include of_clubs', 'of_diamonds', 'of_hearts', 'of_spades' defined above.
        # Another for loop to retrieve number of cards from 1 to 10 using range from 1 to 11 (last one excluded in range)
        for card in range(1, 11):
            if card < 10:
                card = "0" + str(card)
            else:
                card = str(card)

            name = 'cardspng/{}_{}.{}'.format(card, suit, extension)
            print(name)  # We can print to see what is in file "name" although this is optional

            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))

        for card in face_cards:
            name = 'cardspng/{}_{}_{}.{}'.format(str(card), suit, "en", extension)
            print(name)  # We can print to see what is in file "name" although this is optional
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


# Now we need to create some functions that will drive the game

# =================================================
# Function 2: Function to deal cards to players
# =================================================

def deal_card(frame):  # takes parameter "frame" which is the frame that the card will be displayed on.
    next_card = deck.pop(0)
    deck.append(next_card)
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    return next_card

# ====================================================
# Now we need to link up the functions to the buttons
# ====================================================
#
# ====================================
# Function 5: function score_hand
# ====================================

def score_hand(hand):  # We give it parameter called "hand"
    print("calling function 'score_hand'")
    print("-------------")
    score = 0  # initialize score to 0 because there is initially no score
    ace = False  # Ace is initialized to false because we don't have any cards

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

        score += card_value  # we add card value to the score.

        print("Score Total = : {}".format(score))
        print("-----------------------")

        if score > 21 and ace:  # if score is >21 and ace = True (there is an Ace)
            score -= 10  # remove 10 from score
            print("score after removing 10 = {}".format(score))  # optional print to check score after removing 10
            ace = False  # Make ace to False because we removed it

    return score

# Now we will go to function "deal_player" and "deal_dealer" and make them use function "score_hand" to calculate score.

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

def deal_player():

    print("=" * 60)
    print("Initial player_hand: {}".format(player_hand))  # optional. initial player hand is a list with nothing
    print("-------------")

    player_hand.append(deal_card(player_card_frame))

    print("Appended player_hand: {}".format(player_hand))  # optional. Appended player hand shows object appended to player_hand
    print("-------------")

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



# ========================
# "initial_deal" function
# ========================

# We put this code that was duplicated under functions "new_game" and "play"
# under its own function "initial_deal"
# Then We just call function "initial_deal()" whenever we need to use it.

def initial_deal():
    deal_player()  # one card for player
    dealer_hand.append(deal_card(dealer_card_frame))  # one card for dealer
    dealer_score_label.set(score_hand(dealer_hand))   # Displays the Card value of dealer in screen
    deal_player()  # one card for player



# =====================
# "new_game" function
# =====================
# using "destroy" method

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

    # We need to add this code to new_game function so that after you click New Game and destroy the frame
    # it will recreate the frames again.
    # We call the function "intial_deal" here which has the code
    initial_deal()


    # NOTE: we will put this code in the "play" function below and will comment it out here

    # deal_player()  # one card for player
    # dealer_hand.append(deal_card(dealer_card_frame))  # one card for dealer
    # dealer_score_label.set(score_hand(dealer_hand))   # Displays the Card value of dealer in screen
    # deal_player()  # one card for player

# Now we will add button code with "new_game_button" (search below) after player_button

# ==========================
# Shuffle function
# ==========================

# We define the shuffle function here to shuffle the deck

def shuffle():
    random.shuffle(deck)

# ==============================
# We add print(__name__) here
# ==============================

# NOTE: We will comment out this whole section from here to end when running "if __name__ == "__main__" test code

# First run the code here without the print(__name__) below. There is nothing printed for name after version 8.6 is printed
# When you run with print(__name__), it will show __main__ right after version 8.6.
# __main__ is the default name of the code. hence it shows up when we specify to print (__name__)
# Now we will test it on "Import_test" when importing "Blackjack_for_import".

print(__name__)

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

# deck = list(cards) + list(cards) + list(cards)  # Optional. Can use this to have several packs of cards in the deck
deck = list(cards)
# random.shuffle(deck)  # Then we shuffle the "deck" list to make it random. NOTE: We comment this out because we are using shuffle function
shuffle()  # instead we will call the shuffle command which we defined above

# Now we can call "new_game" function

dealer_hand = []
player_hand = []

new_game()

# Mainloop to give control to tkinter for execution
mainWindow.mainloop()


# ==============
# play function
# ==============

# This play function will be executed when we are ready to run the game.


def play():
    # These four lines were originally under "def new_game()" function and we will add them here
    # we call function "initial_deal" here because it has the code.
    initial_deal()

    mainWindow.mainloop()  # We also add mainloop here to execute code. And comment it out in initialization code below



# ====================
# initialization code
# ====================

# NOTE: We want this initialization to be executed on "Import_test.py" when it gets imported. So we remove the indent.
# But we only want the code for function "play" above to run when it is specifically called.

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

# deck = list(cards) + list(cards) + list(cards)  # Optional. Can use this to have several packs of cards in the deck
deck = list(cards)
# random.shuffle(deck)  # Then we shuffle the "deck" list to make it random. NOTE: We comment this out because we are using shuffle function
shuffle()  # instead we will call the shuffle command which we defined above

# Now we can call "new_game" function

dealer_hand = []
player_hand = []


# ==========================
# Test code for name = main
# ==========================
# NOTE: This test comes at the bottom here so that initialization takes place before the "play" function is called
# This test makes sure this program runs when run from "Blackjack2.py" because it will have a name of __main__

if __name__ == "__main__":  # if this is true, we call the play function above
    play()


# We comment this out because it's code is already in function "play" above
# new_game()

# Mainloop to give control to tkinter for execution
# In Blackjack2, we will move the mainloop to the "play" module. So we comment it out here

mainWindow.mainloop()

