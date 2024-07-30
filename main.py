"""
Main.

Created by: Daniel Spaziani
Date: 17/6/24
"""

# Enter your code here.

from random import randint
import pygame
import pygame_menu
from pygame_menu import themes

# Constant for number of cards players start with in their hands.
HAND_SIZE = 7


class Card:
    """Template for a card, store all required information."""

    def __init__(self, number: int, colour: str, function) -> None:
        """
        Save all info to function.

        number - the card's numerical number, not read if not a normal card.
        colour - red, green, blue, or yellow.
        function - says what kind of special card it is.
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

    def calculate_change(self, card_placed_on, player_who_placed) -> bool:
        """Based on cards, calculate validity and what values to change."""
        # Starts by working out whether the card play is valid or not.
        if (
            self.colour != card_placed_on.colour
            and self.number != card_placed_on.number
        ):
            # If neither attribute matches, then it's not valid.
            valid = False
        else:
            # Else it is valid.
            valid = True
        if valid is True:
            # The programme now knows that the move is valid.
            # Now works out what exact operation to make.
            if self.function == "normal":
                # It's a normal card, so it can just add it to pile.
                play_pile.append(self)
            # Then checks if it's a specific purpose card, and checks its use.
            elif self.function == "skip":
                # The next turn must be skipped.
                # TODO: FINISH THIS ONCE LOGIC DONE.
            # If it's a colour change card, then passes that on.
            elif self.function == "wildcard":
                # The player can now change the colour..
                # TODO: FINISH THIS ONCE LOGIC DONE.
            # Else if it's a plus two or four card, then passes on that value.
            elif self.function == "reverse":
                # Reverse the direction of play, giving user another turn.
                # TODO: FINISH THIS ONCE LOGIC DONE.
            elif self.function == "pickup two":
                # Next player must pick up two.
                # TODO: FINISH THIS ONCE LOGIC DONE.
            elif self.function == "pickup four":
                # The next player must pick up four.
                # TODO: FINISH THIS ONCE LOGIC DONE.
            # Then can remove it from the player's hand.
            player_who_placed.hand.pop(self)
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

    def move(self, card_placed_on) -> None:
        """Lets player make their move, and runs card change function."""
        # Sets up valid variable which is used to validate the move.
        valid = False
        # Repeats until a valid move is attained.
        while valid is False:
            # Asks player which card to choose.
            # Runs function on card chosen, to work out correct move.
            card.calculate_change(card_placed_on, self)


# Constant for deck of cards, with card items to create deck list to pick from.
DECK: list[Card] = [
    # Red card set.
    Card(0, "red", "normal"),
    Card(1, "red", "normal"),
    Card(1, "red", "normal"),
    Card(2, "red", "normal"),
    Card(2, "red", "normal"),
    Card(3, "red", "normal"),
    Card(3, "red", "normal"),
    Card(4, "red", "normal"),
    Card(4, "red", "normal"),
    Card(5, "red", "normal"),
    Card(5, "red", "normal"),
    Card(6, "red", "normal"),
    Card(6, "red", "normal"),
    Card(7, "red", "normal"),
    Card(7, "red", "normal"),
    Card(8, "red", "normal"),
    Card(8, "red", "normal"),
    Card(9, "red", "normal"),
    Card(9, "red", "normal"),
    Card(0, "red", "skip"),
    Card(0, "red", "skip"),
    Card(0, "red", "reverse"),
    Card(0, "red", "reverse"),
    Card(0, "red", "pickup two"),
    Card(0, "red", "pickup two"),
    # Yellow card set.
    Card(0, "yellow", "normal"),
    Card(1, "yellow", "normal"),
    Card(1, "yellow", "normal"),
    Card(2, "yellow", "normal"),
    Card(2, "yellow", "normal"),
    Card(3, "yellow", "normal"),
    Card(3, "yellow", "normal"),
    Card(4, "yellow", "normal"),
    Card(4, "yellow", "normal"),
    Card(5, "yellow", "normal"),
    Card(5, "yellow", "normal"),
    Card(6, "yellow", "normal"),
    Card(6, "yellow", "normal"),
    Card(7, "yellow", "normal"),
    Card(7, "yellow", "normal"),
    Card(8, "yellow", "normal"),
    Card(8, "yellow", "normal"),
    Card(9, "yellow", "normal"),
    Card(9, "yellow", "normal"),
    Card(0, "yellow", "skip"),
    Card(0, "yellow", "skip"),
    Card(0, "yellow", "reverse"),
    Card(0, "yellow", "reverse"),
    Card(0, "yellow", "pickup two"),
    Card(0, "yellow", "pickup two"),
    # Green card set.
    Card(0, "green", "normal"),
    Card(1, "green", "normal"),
    Card(1, "green", "normal"),
    Card(2, "green", "normal"),
    Card(2, "green", "normal"),
    Card(3, "green", "normal"),
    Card(3, "green", "normal"),
    Card(4, "green", "normal"),
    Card(4, "green", "normal"),
    Card(5, "green", "normal"),
    Card(5, "green", "normal"),
    Card(6, "green", "normal"),
    Card(6, "green", "normal"),
    Card(7, "green", "normal"),
    Card(7, "green", "normal"),
    Card(8, "green", "normal"),
    Card(8, "green", "normal"),
    Card(9, "green", "normal"),
    Card(9, "green", "normal"),
    Card(0, "green", "skip"),
    Card(0, "green", "skip"),
    Card(0, "green", "reverse"),
    Card(0, "green", "reverse"),
    Card(0, "green", "pickup two"),
    Card(0, "green", "pickup two"),
    # Blue card set.
    Card(0, "blue", "normal"),
    Card(1, "blue", "normal"),
    Card(1, "blue", "normal"),
    Card(2, "blue", "normal"),
    Card(2, "blue", "normal"),
    Card(3, "blue", "normal"),
    Card(3, "blue", "normal"),
    Card(4, "blue", "normal"),
    Card(4, "blue", "normal"),
    Card(5, "blue", "normal"),
    Card(5, "blue", "normal"),
    Card(6, "blue", "normal"),
    Card(6, "blue", "normal"),
    Card(7, "blue", "normal"),
    Card(7, "blue", "normal"),
    Card(8, "blue", "normal"),
    Card(8, "blue", "normal"),
    Card(9, "blue", "normal"),
    Card(9, "blue", "normal"),
    Card(0, "blue", "skip"),
    Card(0, "blue", "skip"),
    Card(0, "blue", "reverse"),
    Card(0, "blue", "reverse"),
    Card(0, "blue", "pickup two"),
    Card(0, "blue", "pickup two"),
    # Special Cards.
    Card(0, "none", "wildcard"),
    Card(0, "none", "wildcard"),
    Card(0, "none", "wildcard"),
    Card(0, "none", "wildcard"),
    Card(0, "none", "pickup four"),
    Card(0, "none", "pickup four"),
    Card(0, "none", "pickup four"),
    Card(0, "none", "pickup four"),
]


def game():
    """Do main game function."""
    # Creates the pile for cards being played.
    play_pile = []
    # Creates user instance of Player.
    user = Player()
    # TODO: DELETE THIS, ONLY FOR DEBUGGING.
    computer = Player()
    # Asks user who they want to face, validates, and then selects opponent.
    # Starts by dealing cards to both the user and the other player.
    # # Gets seven random cards from the deck, and gives them to each player.
    # Ensures there are no double ups, and that cards are all unique.
    verify_deal(user, computer)
    # Then starts game.
    # Creates variable to check whether or not the game should keep running.
    game_running = True
    # Repeats until one of the players has no cards left in their hand.
    while game_running is True:
        # Asks user for input, checks it, and makes the move.
        user.move()
        # Generates the computer's move.
        generate_move(computer)
        # Checks if either of the hands are empty and if so ends the game.
        if user.hand == [] or computer.hand == []:
            game_running = False
    # TODO: Win Message


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


# Starts game.
game()

# Starts pygame.
pygame.init()
# Creates display.
res = (720,720)
# Opens it up.
screen = pygame.display.set_mode(res) 

