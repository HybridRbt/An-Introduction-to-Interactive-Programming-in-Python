__author__ = 'jeredyang'

# implementation of card game - Memory

import simplegui
import random

cards = []  # deck of cards
exposed = range(16)
turn_counter = 0  # note number of turns

first_clicked_card_index = 0
second_clicked_card_index = 0

card_size = (50, 100)  # global, size of card


# helper function to initialize globals
def new_game():
    global cards, exposed, state, turn_counter

    state = 0
    cards = gen_cards()
    turn_counter = 0

    # create a second list called exposed
    for index in range(16):
        exposed[index] = False  # initialize the list w/ all unexposed


# Model the deck of cards. return a list of 16 cards
def gen_cards():
    # generate two lists of cards
    cards1 = range(0, 8)
    cards2 = range(0, 8)

    # concatenate them and shuffle
    whole_cards = cards1 + cards2
    random.shuffle(whole_cards)

    return whole_cards


# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, state, turn_counter
    global first_clicked_card_index, second_clicked_card_index

    card_clicked = pos[0] // card_size[0]

    if state == 0:  # no card exposed
        if not exposed[card_clicked]:  # if this card is not exposed
            exposed[card_clicked] = True  # flip it
            first_clicked_card_index = card_clicked  # note the card number
            state = 1
    elif state == 1:  # already have 1 card exposed
        if not exposed[card_clicked]:  # if this card is not exposed
            exposed[card_clicked] = True  # flip it
            second_clicked_card_index = card_clicked  # note the card number
            turn_counter += 1
            state = 2
    else:
        if not exposed[card_clicked]:  # if this card is not exposed
            exposed[card_clicked] = True  # flip it

            if cards[first_clicked_card_index] != cards[second_clicked_card_index]:
                # if previous two cards don't match
                # flip previous two cards over
                exposed[first_clicked_card_index] = False
                exposed[second_clicked_card_index] = False

            first_clicked_card_index = card_clicked
            state = 1


            # cards are logically 50x100 pixels in size


def draw(canvas):
    font_size = 60

    # draw card
    for card_index in range(0, 16):
        if exposed[card_index]:  # if exposed, draw text
            canvas.draw_text(str(cards[card_index]), get_char_pos(card_index), font_size, "White")
        else:  # else draw blank green card
            canvas.draw_polygon(get_blank_card_pos(card_index), 2, "White", "Green")

    label.set_text(get_turns_text())


def get_blank_card_pos(card_index):
    # get list of points of a square from list of its top left points
    pt1 = (card_index * card_size[0], 0)  # top left
    pt2 = ((pt1[0] + card_size[0]), 0)  # top right
    pt3 = (pt2[0], card_size[1])  # bottom right
    pt4 = (pt1[0], card_size[1])  # bottom left

    return pt1, pt2, pt3, pt4


def get_char_pos(card_index):
    # get pos of a number from its index as its bottom left corner
    pos_x = card_size[0] / 4 + card_index * card_size[0]
    pos_y = card_size[1] - card_size[1] / 4
    return pos_x, pos_y


def get_turns_text():
    return "Turns = " + str(turn_counter)

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label(get_turns_text())

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric