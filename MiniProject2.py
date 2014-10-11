# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

# initialize global variables used in your code
secret_number = 0  # store the number generated
choose_range = 100  # define the range
guess = 0  # user guesses
number_of_guesses_left = int(math.ceil(math.log(choose_range, 2)))
number_of_guesses_used = 0


# helper function to start and restart the game
def new_game():
    # :rtype : object

    global secret_number
    global number_of_guesses_left
    global number_of_guesses_used

    number_of_guesses_left = int(math.ceil(math.log(choose_range, 2)))
    # print number_of_guesses_left   #for debug

    number_of_guesses_used = 0

    secret_number = random.randrange(0, choose_range)

    #print secret_number    #for debug
    print "New game. Range: 0 - " + str(choose_range) + "."
    print "I am ready. Now you guess my secret number."
    print "You have " + str(number_of_guesses_left) + " guesses left."
    print ""  # print an empty line for better format


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global choose_range

    choose_range = 100
    button_100.set_text('Range: 0 - 100 is chosen.')
    button_1000.set_text('Range: 0 - 1000')
    print "You have chosen Range: 0 - 100. Game will now restart. "
    print ""  # print an empty line for better format
    new_game()
    # print choose_range  #for debug


def range1000():
    # button that changes range to range [0,1000) and restarts
    global choose_range
    choose_range = 1000

    button_1000.set_text('Range: 0 - 1000 is chosen.')
    button_100.set_text('Range: 0 - 100')
    print "You have chosen Range: 0 - 1000. Game will now restart. "
    print ""  # print an empty line for better format
    new_game()
    # print choose_range   #for debug


def input_guess(guess):
    # main game logic goes here	
    global number_of_guesses_left
    global number_of_guesses_used

    print "Your guess is " + guess
    # print secret_number #for debug

    number_of_guesses_left -= 1
    number_of_guesses_used += 1

    if int(guess) == secret_number:
        print "Correct! You got me in " + str(number_of_guesses_used) + " guesses. :)"
        print "Game will now restart."
        print ""  # print an empty line for better format
        new_game()
    else:
        if int(guess) > secret_number:
            print "No, lower. "
            print "You have " + str(number_of_guesses_left) + " guesses left. "
            print ""  # print an empty line for better format
        else:
            print "No, higher. "
            print "You have " + str(number_of_guesses_left) + " guesses left. "
            print ""  # print an empty line for better format

        if number_of_guesses_left == 0:
            print "You failed to guess my secret number. The answer should be " + str(secret_number)
            print "Game will now restart."
            print ""  # print an empty line for better format
            new_game()

            # create frame


frame = simplegui.create_frame('Guess A Number', 100, 135)

# register event handlers for control elements
button_100 = frame.add_button('Range: 0 - 100', range100, 200)
button_1000 = frame.add_button('Range: 0 - 1000', range1000, 200)
guess = frame.add_input('You guess:', input_guess, 150)

# call new_game and start frame
new_game()
frame.start()

# always remember to check your completed program against the grading rubric
