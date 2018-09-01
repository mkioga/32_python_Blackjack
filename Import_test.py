
# ========================================================
# Import_test.py ==> Importing Techniques
# ========================================================

# We can include Blackjack program in another program
# We will import "Blackjack1.py" and see how it runs

# import Blackjack1  # NOTE we only use this for Blackjack1. We comment them out when doing Blackjack2

# We also need to have at least one line of code in the program. So we will use print(__name__)
# We will discuss about print(__name__) later

# print(__name__)  # NOTE we only use this for Blackjack1. We comment them out when doing Blackjack2

# When we run this program with only above two lines, it automatically runs the "Blackjack1" code
# And we are able to play the game just as if we ran the "Blackjack1" file itself

# Also note that the print(__name__) is only executed after you close the Blackjack window

# NOTE: code imports and runs the "Blackjack1" code
# But we would like for it to just import the program and not execute the code immediately, so we can be able to
# Call the code to execute it when we want
# In this example, we may want the main program (import_test) to provide a menu of games and then the user can
# choose the game they want and execute it.


# When you import a python module, its code is loaded into memory and then executed.
# This is why the blackjack game executed when we imported it.
# Here is the link to read more about the import system
# https://docs.python.org/3/reference/import.html

# ======================================
# Calling python file from command line
# ======================================

# if you want to run imported python module in command line (cmd), you can use code similar to this

# C:\Users\moe\Documents\Python\IdeaProjects\32_Blackjack> <<=== Make sure to reference correct directory
# C:\Users\moe\Documents\Python\IdeaProjects\32_Blackjack>dir
# 03/25/2018  12:24 PM            13,656 Blackjack1.py <<=== Python file exists here
# C:\Users\moe\Documents\Python\IdeaProjects\32_Blackjack>
# C:\Users\moe\Documents\Python\IdeaProjects\32_Blackjack>python -m Blackjack1.py <<== It will run
# 8.6
# cardspng/01_of_clubs.png
# cardspng/02_of_clubs.png
# cardspng/03_of_clubs.png

# ======================================
# Executing Module only when we run it
# ======================================

# Now in our case, we want to only execute the Blackjack code when we run the module

# Importing a module sorts out name spaces and executes code
# One thing that happens is that an attribute (__main__) of the module called is said to be the name of the module.
# This is the file name for that path or extension

# When a python module is executed as a script, the name is set to __main__
# you can see this when you run the command. It prints __main__ (NOTE: Not __name__)

# We can also see this by printing out an attribute before our code runs
# We can go to "Blackjack1.py" file and add "print(__name__)" right after "def shuffle" function

# Test 1
# When we run "Import_test.py" when "print(__name__) is not activated in "Blackjack1.py"
# We get result of __main__ after program ends

# Test 2
# When we run "Import_test.py" when "print(__name__) is activated in "Blackjack1.py"
# We get result of "Blackjack1" right after version 8.6 and then __main__ after program ends

# Therefore as a result of this, preventing the code from executing when the module is imported becomes very easy
# We just have to check the value of the name attribute and only execute the code if it has the value __main__ (in this case)

# So we go to "Blackjack1.py" and make test to say if __name__ equals __main__, then we can run the program
# This will also be done after module "def shuffle" in this case i.e. before the main program

# Test 3
# With test "if __name__ == "__main__" activated in "Blackjack1.py", if we run the imported code on "Import_test.py"
# We only get __main__ showing up after version 8.6 and the code does not execute.

# VITAL TO UNDERSTAND
# The program not running automatically means that the import is working correctly i.e. not running automatically
# When we import "Blackjack1.py" into "Import_test.py", its name is "Blackjack1" (Test 2 above) and not "__main__"
# Therefore it will fail test ==> "if __name__ == "__main__" and hence not execute the code under this test.
# That is how we make sure imported modules don't run automatically.
# So we are able to import the code and not execute it automatically

# =======================================
# How to run code that has been imported
# =======================================

# In this example, since we have now imported "Blackjack1.py", we can try to run it using command "Blackjack1.new_game()"
# This gives an error "'dealer_card_frame' is not defined"
# This is because the code after "if __name__ == "__main__"  is not running, hence all these variables e.g. dealer_card_frame
# Are not defined

# Blackjack1.new_game()  # Running code using this command gives error at this time



# =================
# blackjack2
# =================


# ==============================
# How to resolve this issue
# ==============================

# We will do this in "Blackjack2.py" so as to preserve "Blackjack1.py"
# So you can comment out "import Blackjack1" and "print(__name__) above

# The way to resolve this is to decide which bits of the "Blackjack2.py" module should be executed
# when the module is imported and then move the test for __main__ to allow that to happen

# So we will need to change the "Blackjack1.py" module to include a function called "play"
# that is resposible for "running the code that starts the game".
# NOTE that "running the code that starts the game" is not the initialization i.e. the code after the "mainWindow = tkinter.Tk()"
# Then we will test if the "Play" function can be used to run the game when it is imported

# Now we go to "Blackjack2.py"
# NOTE: We want this initialization to be executed on "Import_test.py" when it gets imported (code after test for __main__)
# We will create a new function called "play" in "Blackjack2.py". See explanation there


# import Blackjack2
#
# print(__name__)

# We will call the play function using this command.
# NOTE we will not use new_game() anymore

# When we run "Import_test.py" now, it works perfectly.
# NOTE: if you comment th "Blackjack2.play()" comment and run code, you will see the program does not run the game

# Blackjack2.play()

# ======================
# print card placements
# ======================

# you can also print card placements from "Import_test.py" using "print(Blackjack2.cards)"

# When we print the cards, it gives you card placements like "[('01', <tkinter.PhotoImage object at 0x0553FD10>),
# In "Blackjack2.py", we used command "print(cards)"
# We can do same thing here using "print(Blackjack2.cards)"

# print(Blackjack2.cards)


# ===============
# Blackjack3
# ===============

# ===============================================
# Creating module to put code repeated in
# "new_game" and "play" modules in "Blackjack2.py
# ===============================================

# We know that this code below is in both modules "new_game" and "play" in "Blackjack2.py
# We want to create a function to put this code so it is just called in other modules instead of being repeated

    # deal_player()  # one card for player
    # dealer_hand.append(deal_card(dealer_card_frame))  # one card for dealer
    # dealer_score_label.set(score_hand(dealer_hand))   # Displays the Card value of dealer in screen
    # deal_player()  # one card for player

# We will do this in "Blackjack3.py"

# import Blackjack3  # Imports Blackjack3
# print(__name__)  # Prints the name of the program. __main__
# Blackjack3.play()  # Calls the Play module in Blackjack3.py
# print(Blackjack3.cards)  # Optional. Prints card positions e.g. ('01', <tkinter.PhotoImage object at 0x050CFF30>)




# ==============================================
# Importing and Underscores in Variable names
# ==============================================

# ============
# Blackjack4
# ============


# We will talk about underscores in variable names
# When we CTRL + click a python module, it takes you to its source code and you notice
# that many object names starts and/or end with underscore (or double underscores) (__)

# We have previously discussed ending a name with a single underscore (_) when we looked at the
# spinbox widget in tkinter, and we can set the range of values that appear in the spinbox using
# "to" and "from" underscore arguments, but because "from" is a python keyword, we used "from_" instead of just "from"

# The convention is to use a single underscore after a name if it would otherwise conflict with a
# name that is built into python i.e. python keyword


# import Blackjack4
#
# print(__name__)
# Blackjack4.play()
# print(Blackjack4.cards)


# ==========================
# Other uses of underscores
# ==========================

# Unlike other languages, python has no concept of "private" or "protected" variables
# That means its possible to do things with a module that you probably should not do.
# We will demonstrate this with our "Blackjack4" module

# It is useful to be able to call play function "Blackjack4.play()"
# it is also useful to be able to print the cards list "print(Blackjack4.cards)" to create decks for other games

# Beyond that, there is nothing else in the "Blackjack4.py" module that makes any sense to use once it has been imported
# There is a "score_hand" function, but that is really very specific to "Blackjack4" and coule not be used to decide
# which of two poker hands have been up because its completely different algorithm

# In java for example, the "play" function and "cards" would be made available to other programs, everything else would be
# Marked "private" so it is hidden and would not actually show
# But python does not have any "private" objects, so we can do some silly things after importing "Blackjack4" module


# import Blackjack4
# print(__name__)

# Here for example, we are going to call "deal_card(dealer_card_frame)" to show you it can be done in python
# because python has no private objects.
# However this is not a wise thing to do. but we do it here for demonstration

# When we run this, the program runs and we now see "dealer" has two cards to begin with instead of one
# But only the second card's value is included in the dealer score (instead of the total of both)
# This is because we gave access to areas of Blackjack4 game which we would ordinarily not want someone who has
# imported the game to access because it is sort of like breaking the game.

# This is compounded by the fact that there is nothing in intellij that indicates that we should not be calling this function


# Blackjack4.deal_card(Blackjack4.dealer_card_frame)
#
# Blackjack4.play()
# print(Blackjack4.cards)


# ===========================================
# protected function (defined using _itsname
# ===========================================

# By convention, starting a name with an underscore (_) indicates that it should be treated as "Protected",
# meaning it is not intended to be used outside the module that it exist in.

# There is a little more to that when dealing with "Classes" and we will talk about that when looking at object oriented programming.

# Import_test 1: Refactor
#=========================

# We can go back to "Blackjack4 and refactor function "deal_card" and call it "_deal_card"
# NOTE that it renames it in both "Blackjack4.py" and in "Import_test.py"

#
#
# import Blackjack4
# print(__name__)
#
# # NOTE that intellij here gives warning "Access to a protected member _deal_card of a module"
# # This is because anything starting with _ is a protected member, hence _deal_card is a protected member
# # NOTE that even with this warning, we can still run the program and it works
#
# Blackjack4._deal_card(Blackjack4.dealer_card_frame)  # deal_card renamed here after refactoring
#
# Blackjack4.play()
# print(Blackjack4.cards)
#
# # So if you find yourself using an object with a name starting with underscore (_), bear in mind that
# # it is protected and you should not be accessing it if it exist in a module that you did not write/not in your code.
#
# # Another point is it is good to import modules as shown e.g. import Blackjack4
# # so that when using functions from imported module, you will specify the module first and then function e.g. Blackjack4.play
# # This will easily help you to know that the functions you are using are from the imported module




# ===========================
# Using import Blackjack4:
# ==========================

# By default, when using "import Blackjack4", names starting with _ are not imported

# There is another implication of using underscore (_) to start up a name
# if you use an alternate way of importing Blackjack4, anything with a name starting with
# underscore (_) is not actually imported.

# We have recommended before that we don't do an import * from a module because all of the names from the imported module
# then become part of your module namespace and it is easy to lose track of what name belong to what.

# To demonstrate this, we will import "Blackjack4.py" and then display all the global namespaces in "Blackjack4.py"

# import Blackjack4

# Here we are trying to print all the global names
# Note that after we run this command, it prints first "Global from Blackjack4.py = __name__"
# Then gets an error message: RuntimeError: dictionary changed size during iteration
# This is because the new variable we have created has altered the dictionary itself.
# So we cannot actually use this method to access the globals.

# for x in globals():
#     print("Global from Blackjack4.py = {}".format(x))


# A solution to this is to take a copy of the globals dictionary and iterate through that.

# We make a copy of globals and put it in variable g.
# so if we change g, it will not change the original dictionary
#
# g = sorted(globals())
#
# # Then loop through g to access the global names
#
# for x in g:
#     print("Global from Blackjack4.py = {}".format(x))

# When we run above code, we get this result and no errors
# We can see the list of names is small, all starting with __
# And the only object here is Blackjack4 that we imported.

# Global from Blackjack4.py = Blackjack4
# Global from Blackjack4.py = __annotations__
# Global from Blackjack4.py = __builtins__
# Global from Blackjack4.py = __cached__
# Global from Blackjack4.py = __doc__
# Global from Blackjack4.py = __file__
# Global from Blackjack4.py = __loader__
# Global from Blackjack4.py = __name__
# Global from Blackjack4.py = __package__
# Global from Blackjack4.py = __spec__


# =================================================
# importing all using "from Blackjack4 import * "
# =================================================

# When importing all using "from Blackjack4 import * " , names starting with _ are not imported

# Now we import all modules from Blackjack4


# from Blackjack4 import *
#
# g = sorted(globals())


# Then loop through g to access the global names


# for x in g:
#     print("Global from Blackjack4.py = {}".format(x))

# We see its importing all the functions and variables from "Blackjack4.py"
# Everything in "Blackjack4" module namespace appears in "Import_test"
# This includes all names with no underscores, and all that "start" and "end" with two underscores (__)

# NOTE: If we created an an object called "cards" in "Import_test.py", then the
# object "cards" from "Blackjack4" would not be available because it will be replaced by
# the new "cards" object we created.

# NOTE that our "_deal_card" function from "Blackjack4" is not imported.
# And if you try to use it, you will get an error of "Unresolved reference"
# So the python import mechanism takes note of this convention and it will
# not import any object that start with underscore (_) when using "import * "

# When we import Blackjack4, the objects from the Blackjack4 module are not imported separately
# So everything, even names beginning with underscore (_) are available when
# prefixing them with Blackjack4. e.g. Blackjack4._deal_card


# _deal_card(dealer_card_frame)  # We get error "Unresolved reference" on this command

# Global from Blackjack4.py = __annotations__
# Global from Blackjack4.py = __builtins__
# Global from Blackjack4.py = __cached__
# Global from Blackjack4.py = __doc__
# Global from Blackjack4.py = __file__
# Global from Blackjack4.py = __loader__
# Global from Blackjack4.py = __name__
# Global from Blackjack4.py = __package__
# Global from Blackjack4.py = __spec__
# Global from Blackjack4.py = button_frame
# Global from Blackjack4.py = card_frame
# Global from Blackjack4.py = cards
# Global from Blackjack4.py = deal_dealer
# Global from Blackjack4.py = deal_player
# Global from Blackjack4.py = dealer_button
# Global from Blackjack4.py = dealer_card_frame
# Global from Blackjack4.py = dealer_hand
# Global from Blackjack4.py = dealer_score_label
# Global from Blackjack4.py = deck
# Global from Blackjack4.py = initial_deal
# Global from Blackjack4.py = load_images
# Global from Blackjack4.py = mainWindow
# Global from Blackjack4.py = new_game
# Global from Blackjack4.py = new_game_button
# Global from Blackjack4.py = play
# Global from Blackjack4.py = player_button
# Global from Blackjack4.py = player_card_frame
# Global from Blackjack4.py = player_hand
# Global from Blackjack4.py = player_score_label
# Global from Blackjack4.py = random
# Global from Blackjack4.py = result
# Global from Blackjack4.py = result_text
# Global from Blackjack4.py = score_hand
# Global from Blackjack4.py = shuffle
# Global from Blackjack4.py = shuffle_button
# Global from Blackjack4.py = tkinter



# ========================
# Double underscore (__) at the start (Not end)
# ========================

# Using Double underscore (__) at the "start" of a Name invokes pythons name mangling rules
# This convention exist to prevent name clashes when sub classing objects
# We will look at this more in object oriented programming.

# In our "Blackjack4" module, starting name with two Underscores (__) will not serve any useful purpose
# because anything that starts with two underscores (__) automatically starts with one (_)
# So "import * " will not import them


# ===================================================
# Names Starting and Ending with two underscores (__)
# ====================================================

# ==================================
# Import_test 2: renaming __name__
# ==================================

# These names should never be changed.

# The names that start and end with two underscores are things you should not be changing
# Example is the __name__ that we used to restrict the code when the module was imported.

# We will try to change __name__ in "Blackjack4.py" and you will see what happens
# we will use ==> __name__ = "__main__" just above "mainWindow = tkinter.Tk()" in "Blackjack4.py"

# First we test this before modifying __name__ in "Blackjack4.py". It works fine

# import Blackjack4
# Blackjack4._deal_card(Blackjack4.dealer_card_frame)
# Blackjack4.play()

# After we change __name__ in "Blackjack4.py" and then run code here, first you see window runs fine
# But Dealer has only one card instead of two. Meaning the code under "Import_test.py" has not executed.
# This is the original effect that we saw when we imported Blackjack.
# Because __name__ has been set to __main__, the test that restricts code execution on import is no longer
# valid and the code runs when we import the module.

# When we close the program window, we get this error:
# _tkinter.TclError: can't invoke "label" command: application has been destroyed

# This is because by closing the window, we have destroyed all the tkinter objects so that nothing works
# and the game cannot be played according to the play function

# NOTE: Python does not prevent you from modifying these variables
# But if you modify them, the results are undefined and you can run into all sorts of errors.

# Now we will remove the __name__ = "__main__" in "Blackjack4.py"


# ===================================
# Underscore and double underscore (throwaway value)
# ===================================

# A variable that is just named _ with nothing else indicates a throwaway value.
# Underscore (_) by itself is a valid variable name and rather than thinking up a name for something that
# will not be used, the convention is to call it _ (underscore) or __ (double undescore)

# Examples of things that you may have to access but will not use include tuples
# We want to use some of the values of a tuple but not all of them

# In this example, we will assign Name, Age and Country to a tuple named "personal_details"

personal_details = ("Dylan", 42, "American")

# Then we can access just the Name and Country by unpacking tuple "personal_details" into different variables
# NOTE here we are unpacking age to a variable named _ which we don't intend to use


name, _, country = personal_details
print(name, _, country)  # if we print including variable _, it will print fine.
print(name, country)  # But since we did not intend to use _, we will not print it

# So _ and __ are valid variable names and are normally used when you don't want to access them
# otherwise you should give them a more descriptive name.

