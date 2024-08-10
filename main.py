"""
Main.

Created by: Daniel Spaziani
Date: 17/6/24
"""

# Enter your code here.

from random import randint
import pygame

# Constant for number of cards players start with in their hands.
HAND_SIZE = 7
# Constants for colours to use.
LIGHT_GREEN = (50,205,50)
DARK_GREEN = (0,100,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
RED = (255,0,0)
WHITE = (255,255,255)
# Screen size constants.
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
# Variable to hold special card functions for each turn.
functions = []
# Starts pygame.
pygame.init()
pygame.display.init()
# Creates text font.
text_font = pygame.font.SysFont("Helvetica", 30)
# Creates display.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(LIGHT_GREEN)
# Variable to use when using wildcards.
wildcard_colour_choice = None
# Constants for default button text position.
BUTTON_TEXT_X = 5
BUTTON_TEXT_Y = 5
# List to store all buttons as they're created.
# List formatted like this: [[x, y, x_size, y_size, text, colour, button]]
buttons: list = []
# Constants for accessing list.
# Constant for x coordinate.
BUTTONS_X = 0
# Constant for y coordinate.
BUTTONS_Y = 1
# Constant for width.
BUTTONS_X_SIZE = 2
# Constant for height.
BUTTONS_Y_SIZE = 3
# Constant for text content.
BUTTONS_TEXT = 4
# Constant for button colour.
BUTTONS_COLOUR = 5
# Constant for GUI surface button object.
BUTTONS_BUTTON_OBJECT = 6
# Creates constant for accessing each card.
CARD_1_INDEX = 0
CARD_2_INDEX = 1
CARD_3_INDEX = 2
CARD_4_INDEX = 3
CARD_5_INDEX = 4
CARD_6_INDEX = 5
CARD_7_INDEX = 6
# Creates the pile for cards being played.
play_pile = []
# List for buttons for wildcard colour selection.
wildcard_colour_buttons = []
# Loads in images.
card_back = pygame.image.load("card_back.png")
# Loads all sets of images into lists by number.
# Starts by making constant for number of numbered cards in a set.
NUMBERED_CARD_SET = 10
# Creates blank lists for cards.
blue_images = []
red_images = []
green_images = []
yellow_images = []
# Now uses constant to iterate through numbered cards and load them.
for card_number in range(NUMBERED_CARD_SET):
    blue_images.append(pygame.image.load(f"blue_{card_number}.png"))
    red_images.append(pygame.image.load(f"red_{card_number}.png"))
    green_images.append(pygame.image.load(f"green_{card_number}.png"))
    yellow_images.append(pygame.image.load(f"yellow_{card_number}.png"))
# Now loads special cards.
# Pickup two cards.
blue_picker = pygame.image.load("blue_picker.png")
red_picker = pygame.image.load("red_picker.png")
green_picker = pygame.image.load("green_picker.png")
yellow_picker = pygame.image.load("yellow_picker.png")
# Reverse cards.
blue_reverse = pygame.image.load("blue_reverse.png")
red_reverse = pygame.image.load("red_reverse.png")
green_reverse = pygame.image.load("green_reverse.png")
yellow_reverse = pygame.image.load("yellow_reverse.png")
# Skip cards.
blue_skip = pygame.image.load("blue_skip.png")
red_skip = pygame.image.load("red_skip.png")
green_skip = pygame.image.load("green_skip.png")
yellow_skip = pygame.image.load("yellow_skip.png")
# Wildcard and pickup four.
wildcard = pygame.image.load("wild_colour_changer.png")
pickup_four = pygame.image.load("wild_pick_four.png")


class Card:
    """Template for a card, store all required information."""

    def __init__(self, number: int, colour: str, function, display) -> None:
        """
        Save all info to function.

        number - the card's numerical number, not read if not a normal card.
        colour - red, green, blue, or yellow.
        function - says what kind of special card it is.
        display - stores display object for the card.
        """
        self.number = int(number)
        self.colour = colour
        # This can be one of four values.
        # "normal" - a normal card.
        # "skip" - skips the next turn.
        # "pickup two" - next player has to pick up two cards.
        # "pickup four" - next player has to pick up four cards, also wildcard.
        # "reverse" - flips direction of play.
        # "wildcard" - allows placer to change colour to whatever they want.
        self.function = function
        self.display = display

    def calculate_change(self, card_placed_on, player_who_placed) -> bool:
        """Based on cards, calculate validity and what values to change."""
        # Starts by working out whether the card play is valid or not.
        if (
            self.colour != card_placed_on.colour
            and self.number != card_placed_on.number
        ):
            # Then has to check if the card is a wildcard of some description.
            if self.function == "wildcard" or self.function == "pickup four":
                # If it is then it immediately becomes valid.
                valid = True
            else:
                # If neither attribute matches, then it's not valid.
                valid = False
        else:
            # Else it is valid.
            valid = True
        if valid is True:
            # The programme now knows that the move is valid.
            # Now appends the function to the list.
            functions.append(self.function)
            # Adds card to play pile since it's been played.
            play_pile.append(self)
            # Then can remove it from the player's hand.
            player_who_placed.hand.pop(player_who_placed.hand.index(self))
        return valid


class Player:
    """Store methods and data for each player."""

    def __init__(self) -> None:
        """
        Set up variables for player data.

        hand - list of cards in player's posession.
        """
        self.hand: list = []

    def deal(self):
        """Deal cards to the player."""
        # Repeats until player has enough cards in their hand.
        while len(self.hand) < HAND_SIZE:
            # Chooses a random card from the deck.
            card_to_add = DECK[randint(0, len(DECK) - 1)]
            # Now checks it isn't already in hand.
            if card_to_add not in self.hand:
                # Then adds card to hand.
                self.hand.append(card_to_add)

    def move(self, user_card, card_placed_on) -> bool:
        """Lets player make their move, and runs card change function."""
        return user_card.calculate_change(card_placed_on, self)


# Constant for deck of cards, with card items to create deck list to pick from.
DECK: list[Card] = [
    # Red card set.
    Card(0, "red", "normal", red_images[0]),
    Card(1, "red", "normal", red_images[1]),
    Card(1, "red", "normal", red_images[1]),
    Card(2, "red", "normal", red_images[2]),
    Card(2, "red", "normal", red_images[2]),
    Card(3, "red", "normal", red_images[3]),
    Card(3, "red", "normal", red_images[3]),
    Card(4, "red", "normal", red_images[4]),
    Card(4, "red", "normal", red_images[4]),
    Card(5, "red", "normal", red_images[5]),
    Card(5, "red", "normal", red_images[5]),
    Card(6, "red", "normal", red_images[6]),
    Card(6, "red", "normal", red_images[6]),
    Card(7, "red", "normal", red_images[7]),
    Card(7, "red", "normal", red_images[7]),
    Card(8, "red", "normal", red_images[8]),
    Card(8, "red", "normal", red_images[8]),
    Card(9, "red", "normal", red_images[9]),
    Card(9, "red", "normal", red_images[9]),
    Card(0, "red", "skip", red_skip),
    Card(0, "red", "skip", red_skip),
    Card(0, "red", "reverse", red_reverse),
    Card(0, "red", "reverse", red_reverse),
    Card(0, "red", "pickup two", red_picker),
    Card(0, "red", "pickup two", red_picker),
    # Yellow card set.
    Card(0, "yellow", "normal", yellow_images[0]),
    Card(1, "yellow", "normal", yellow_images[1]),
    Card(1, "yellow", "normal", yellow_images[1]),
    Card(2, "yellow", "normal", yellow_images[2]),
    Card(2, "yellow", "normal", yellow_images[2]),
    Card(3, "yellow", "normal", yellow_images[3]),
    Card(3, "yellow", "normal", yellow_images[3]),
    Card(4, "yellow", "normal", yellow_images[4]),
    Card(4, "yellow", "normal", yellow_images[4]),
    Card(5, "yellow", "normal", yellow_images[5]),
    Card(5, "yellow", "normal", yellow_images[5]),
    Card(6, "yellow", "normal", yellow_images[6]),
    Card(6, "yellow", "normal", yellow_images[6]),
    Card(7, "yellow", "normal", yellow_images[7]),
    Card(7, "yellow", "normal", yellow_images[7]),
    Card(8, "yellow", "normal", yellow_images[8]),
    Card(8, "yellow", "normal", yellow_images[8]),
    Card(9, "yellow", "normal", yellow_images[9]),
    Card(9, "yellow", "normal", yellow_images[9]),
    Card(0, "yellow", "skip", yellow_skip),
    Card(0, "yellow", "skip", yellow_skip),
    Card(0, "yellow", "reverse", yellow_reverse),
    Card(0, "yellow", "reverse", yellow_reverse),
    Card(0, "yellow", "pickup two", yellow_picker),
    Card(0, "yellow", "pickup two", yellow_picker),
    # Green card set.
    Card(0, "green", "normal", green_images[0]),
    Card(1, "green", "normal", green_images[1]),
    Card(1, "green", "normal", green_images[1]),
    Card(2, "green", "normal", green_images[2]),
    Card(2, "green", "normal", green_images[2]),
    Card(3, "green", "normal", green_images[3]),
    Card(3, "green", "normal", green_images[3]),
    Card(4, "green", "normal", green_images[4]),
    Card(4, "green", "normal", green_images[4]),
    Card(5, "green", "normal", green_images[5]),
    Card(5, "green", "normal", green_images[5]),
    Card(6, "green", "normal", green_images[6]),
    Card(6, "green", "normal", green_images[6]),
    Card(7, "green", "normal", green_images[7]),
    Card(7, "green", "normal", green_images[7]),
    Card(8, "green", "normal", green_images[8]),
    Card(8, "green", "normal", green_images[8]),
    Card(9, "green", "normal", green_images[9]),
    Card(9, "green", "normal", green_images[9]),
    Card(0, "green", "skip", green_skip),
    Card(0, "green", "skip", green_skip),
    Card(0, "green", "reverse", green_reverse),
    Card(0, "green", "reverse", green_reverse),
    Card(0, "green", "pickup two", green_picker),
    Card(0, "green", "pickup two", green_picker),
    # Blue card set.
    Card(0, "blue", "normal", blue_images[0]),
    Card(1, "blue", "normal", blue_images[1]),
    Card(1, "blue", "normal", blue_images[1]),
    Card(2, "blue", "normal", blue_images[2]),
    Card(2, "blue", "normal", blue_images[2]),
    Card(3, "blue", "normal", blue_images[3]),
    Card(3, "blue", "normal", blue_images[3]),
    Card(4, "blue", "normal", blue_images[4]),
    Card(4, "blue", "normal", blue_images[4]),
    Card(5, "blue", "normal", blue_images[5]),
    Card(5, "blue", "normal", blue_images[5]),
    Card(6, "blue", "normal", blue_images[6]),
    Card(6, "blue", "normal", blue_images[6]),
    Card(7, "blue", "normal", blue_images[7]),
    Card(7, "blue", "normal", blue_images[7]),
    Card(8, "blue", "normal", blue_images[8]),
    Card(8, "blue", "normal", blue_images[8]),
    Card(9, "blue", "normal", blue_images[9]),
    Card(9, "blue", "normal", blue_images[9]),
    Card(0, "blue", "skip", blue_skip),
    Card(0, "blue", "skip", blue_skip),
    Card(0, "blue", "reverse", blue_reverse),
    Card(0, "blue", "reverse", blue_reverse),
    Card(0, "blue", "pickup two", blue_picker),
    Card(0, "blue", "pickup two", blue_picker),
    # Special Cards.
    Card(0, "none", "wildcard", wildcard),
    Card(0, "none", "wildcard", wildcard),
    Card(0, "none", "wildcard", wildcard),
    Card(0, "none", "wildcard", wildcard),
    Card(0, "none", "pickup four", pickup_four),
    Card(0, "none", "pickup four", pickup_four),
    Card(0, "none", "pickup four", pickup_four),
    Card(0, "none", "pickup four", pickup_four)
]


def verify_deal(user: Player, computer: Player):
    """Ensure that the player and the computer don't have the same cards."""
    # Starts assuming hand won't need to be reshuffled, unless proven.
    reshuffle_hand = False
    # Creates variable to run loop, which will stay true until valid.
    run_verify = True
    while run_verify is True:
        # Starts by dealing to them both.
        user.deal()
        computer.deal()
        # Now compares the two and sees if there's any overlap.
        # Runs through each of the user's cards.
        for card in user.hand:
            # Checks if the card is also in the computer's hand.
            if card in computer.hand:
                # Makes computer reshuffle their cards.
                # Make computer shuffle instead of user to minimise disruption.
                reshuffle_hand = True
        # Now that verification is done, checks if it's valid or not.
        # If reshuffle hand is true then it must reshuffle.
        # Otherwise it's valid and can continue.
        if reshuffle_hand is False:
            # Values are valid.
            # Continues with programme.
            run_verify = False
        elif reshuffle_hand is True:
            # Invalid, needs to run again.
            # Resets the variable so it can use it to check again next time.
            reshuffle_hand = False
            # And resets players' hands for next time.
            user.hand = []
            computer.hand = []


def draw_text(text):
    """Takes in text, a font, and coordinates, and outputs."""
    return text_font.render(text, True, (0, 0, 0))


def button_click(mouse_x, mouse_y, buttons):
    """Checks where mouse is, using list checks which button has been clicked."""
    # Runs through each button in the list.
    for button in buttons:
        # Checks if its coordinates match the mouse.
        if button[BUTTONS_X] <= mouse_x <= button[BUTTONS_X] + button[BUTTONS_X_SIZE] and button[
            BUTTONS_Y] <= mouse_y <= button[BUTTONS_Y] + button[BUTTONS_Y_SIZE]:
            # Coordinates match, so returns button.
            return button


# Game setup.
# Creates user instance of Player.
user = Player()
# TODO: DELETE THIS, ONLY FOR DEBUGGING.
computer = Player()
# Asks user who they want to face, validates, and then selects opponent.
# Starts by dealing cards to both the user and the other player.
# Gets seven random cards from the deck, and gives them to each player.
# Ensures there are no double ups, and that cards are all unique.
verify_deal(user, computer)
# Now gets random card from deck and puts it into play pile to start.
play_pile.append(DECK[randint(0, len(DECK) - 1)])
# Now button lists are created and added to button list.
# test_button = [0, 0, 200, 50, "Button", RED]
# buttons.append(test_button)
# BUTTONS_TEST_BUTTON = 0
card_1_button = [285, 750, 130, 182, "Card 1", LIGHT_GREEN]
buttons.append(card_1_button)
card_2_button = [485, 750, 130, 182, "Card 2", LIGHT_GREEN]
buttons.append(card_2_button)
card_3_button = [685, 750, 130, 182, "Card 3", LIGHT_GREEN]
buttons.append(card_3_button)
card_4_button = [885, 750, 130, 182, "Card 4", LIGHT_GREEN]
buttons.append(card_4_button)
card_5_button = [1085, 750, 130, 182, "Card 5", LIGHT_GREEN]
buttons.append(card_5_button)
card_6_button = [1285, 750, 130, 182, "Card 6", LIGHT_GREEN]
buttons.append(card_6_button)
card_7_button = [1485, 750, 130, 182, "Card 7", LIGHT_GREEN]
buttons.append(card_7_button)
# Now puts each button on the screen.
for button in buttons:
    # Starts by making a surface with the x and y sizes.
    # Saves the surface to the list.
    button.append(pygame.Surface((button[BUTTONS_X_SIZE], button[BUTTONS_Y_SIZE])))
    # Fills it with the required colour.
    button[BUTTONS_BUTTON_OBJECT].fill(button[BUTTONS_COLOUR])
    # Adds card image.
    button[BUTTONS_BUTTON_OBJECT].blit(user.hand[buttons.index(button)].display, (0, 0))
    # Finally adds button to screen.
    screen.blit(button[BUTTONS_BUTTON_OBJECT], (button[BUTTONS_X], button[BUTTONS_Y]))
# The buttons are added to a list that can be checked.
# Creates red button.
wildcard_colour_buttons.append([1300, 400, 50, 50, "", RED])
# Creates green button.
wildcard_colour_buttons.append([1400, 400, 50, 50, "", DARK_GREEN])
# Creates blue button.
wildcard_colour_buttons.append([1300, 600, 50, 50, "", BLUE])
# Creates yellow button.
wildcard_colour_buttons.append([1400, 600, 50, 50, "", YELLOW])
# Font test.
# screen.blit(draw_text("Test 123"), (300, 250))
# Shapes for testing.
# pygame.draw.rect(screen, RED, [200, 300, 100, 50])
# pygame.draw.rect(screen, DARK_GREEN, [250, 400, 200, 50])
# pygame.draw.rect(screen, RED, [0, 0, 100, 100])
# Creates card visuals.
# Variable to continue running loop.
running = True
# Variable to store number of moves in.
moves_made = 0
# Loop to run programme.
# Checks user input and responds.
while running:
    # Adds the top card of the play pile to the GUI.
    pygame.draw.rect(screen, LIGHT_GREEN, [885, 350, 130, 182])
    screen.blit(play_pile[-1].display, (885, 350))
    # Updates display every loop.
    pygame.display.update()
    # Checks if either of the hands are empty and if so ends the game.
    if user.hand == []:
        # Tells the user they won if their hand is empty first.
        print("You won!")
        running = False
    elif computer.hand == []:
        # If computer won then tells user they lost.
        print("You lost")
        running = False
    # Checks for new events.
    for event in pygame.event.get():
        # If the game has been told to quit then exits loop.
        if event.type == pygame.QUIT:  
            running = False
        # If the user has clicked.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Gets position of their mouse.
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if wildcard_colour_choice == None:
                # Then checks what they've clicked.
                button_clicked = button_click(mouse_x, mouse_y, buttons)
                # Checks if there was an actual button clicked.
                if button_clicked != None:
                    # Checks that against the list and responds.
                    # Depending on which button is pushed, runs appropriate code.
                    # if buttons.index(button_clicked) == BUTTONS_TEST_BUTTON:
                        # print("Test Button")
                        # screen.blit(test_image, (0, 0))
                    # Gets the card associated with the index the user selected.
                    chosen_card = user.hand[buttons.index(button_clicked)]
                    # Checks user choice, and makes the move.
                    valid = user.move(chosen_card, play_pile[-1])
                    if valid is True:
                        # Now continues with the turn.
                        moves_made += 1
                        # Now regenerates user hand GUI.
                        for button in buttons:
                            try:
                                screen.blit(
                                    user.hand[buttons.index(button)].display,
                                    (button[BUTTONS_X], button[BUTTONS_Y]))
                            except IndexError:
                                # If the hand has less cards then doesn't draw that card.
                                pygame.draw.rect(screen, LIGHT_GREEN, [
                                    button[BUTTONS_X], button[BUTTONS_Y],
                                    button[BUTTONS_X_SIZE], button[BUTTONS_Y_SIZE]])
                        # Now checks whether the player put down a special card.
                        # If they put down a wildcard then changes the colour to selected one.
                        if chosen_card.function == "wildcard" or chosen_card.function == "pickup four":
                            # Asks user which colour they want to change wildcard to.
                            # Draws it onscreen.
                            pygame.draw.rect(screen, RED, [1300, 300, 600, 400])
                            screen.blit(draw_text("Select the colour to change to:"), (1400, 310))
                            for button in wildcard_colour_buttons:
                                surface = pygame.Surface((button[BUTTONS_X_SIZE], button[BUTTONS_Y_SIZE]))
                                surface.fill(button[BUTTONS_COLOUR])
                                screen.blit(surface, (button[BUTTONS_X], button[BUTTONS_Y]))
                            wildcard_colour_choice = "UNDECIDED"
                        else:
                            # If they put down a pickup two or four then makes computer pick up.
                            # If they put down a reverse or skip then switches the turn back to player.
                            # computer.generate_card()
                            print(moves_made)
                    else:
                        print("Invalid move.")
                else:
                    print("No button pressed.")
            else:
                # Then checks what they've clicked.
                button_clicked = button_click(mouse_x, mouse_y, wildcard_colour_buttons)
                # Checks if there was an actual button clicked.
                if button_clicked != None:
                    wildcard_colour_choice = button_clicked[BUTTONS_COLOUR]
                    # Takes the colour of the button and saves.
                    wildcard_colour_choice = button_clicked[BUTTONS_COLOUR]
                    # Updates its colour to the colour user asked for.
                    chosen_card.colour = wildcard_colour_choice
                    # Resets variable.
                    wildcard_colour_choice = None
                    # Now draws over popup to hide it.
                    pygame.draw.rect(screen, LIGHT_GREEN, [1300, 300, 600, 400])
                    # Debug print.
                    print(chosen_card.colour)
                    # If they put down a pickup two or four then makes computer pick up.
                    # If they put down a reverse or skip then switches the turn back to player.
                    # computer.generate_card()
                    print(moves_made)
