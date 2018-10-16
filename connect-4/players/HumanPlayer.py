from players.BasePlayer import BasePlayer

class HumanPlayer(BasePlayer):
    """ Represents a human player.

        Prompts for input instead of calculating the optimum move.

        Attributes:
            name: A string representing the Player's name.
            token: Their board tile, X or O.
    """

    def __init__(self, name):
        """ Initializes a HumanPlayer.
        """

        # Initializes a Player
        super().__init__(name)

    def chooseMove(self):
        chosen_move = input("What move would you like to play? \n")
        return chosen_move
