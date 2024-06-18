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
        """Saves all info to function."""
        self.number = int(number)
        self.colour = colour
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
DECK: list[Card] = [""]


def game():
    """Main game function."""
    # Starts by dealing cards to both the user and the other player.
    # Gets seven random cards from the deck, and gives them to each player.
