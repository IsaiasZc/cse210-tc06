class Move:
    """A maneuver in the game. The responsibility of Move is to keep track of the stones to remove and which pile to remove them from.
    
    Stereotype: 
        Information Holder

    Attributes:
        _numbers
    """
    def __init__(self, numbers):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._numbers = numbers

    def get_numbers(self):
        """Returns the pile to remove from.

        Args:
            self (Move): an instance of Move.
        """
        return self._numbers
