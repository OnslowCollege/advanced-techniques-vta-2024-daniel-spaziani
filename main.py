"""
Main.

Created by: Daniel Spaziani
Date: 17/6/24
"""

# Enter your code here.

# Constant for number of cards players start with in their hands.
NUMBER_OF_CARDS_IN_HAND = 7


class Card:
    """Template for a card, stores all required information."""

    def __init__(self, number: int, colour: str, function) -> None:
        """Save all info to function."""
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

    def calculate_change(self, card_placed_on: Card) -> bool:
        """Based on card that this one is being placed on,
        calculates what values to change."""
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
            # TODO: This section.
            # The programme now knows that the move is valid.
            # Now works out what exact operation to make.
            # Then updates the card on top to the new one.
            # First removes the card from the user's hand.
            # Then checks if it's a specific purpose card, and checks its use.
            # If it's a colour change card, then passes that on.
            # Else if it's a plus two or four card, then passes on that value.
            pass


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
    """Main game function."""
    # Starts by dealing cards to both the user and the other player.
    # Gets seven random cards from the deck, and gives them to each player.
