import random

class Board:
    
    def __init__(self):
        """A designated playing surface. The responsibility of Board is to keep track of the pieces in play.
    
    Stereotype: 
        Information Holder
    Attributes:
        _numbers (list): Stores a random a number between 1000-9999.
        _chosen_number (Tuple): Two elements to do the comparison.
        current (integer): Value of the user´s turn.
    """
        self._numbers = None # Store the random number
        self._chosen_number = [["----","****"],["----","****"]] # Two elements to do the comparison
        self.current = -1 # The current user
        self._prepare()

    def is_match(self):
        match = False
        for number, guess in self._chosen_number:
            if number == self._numbers:
                match = True
                break
        return match


    def apply(self, move):
        """Applies the given move to the playing surface. In this case, that 
        means comparing the guessed numbers with the random numbers.
        
        Args:
            self (Board): an instance of Board.
            move (Move): The move to apply.
        """

        # here we call the guessed number
        number = str(move.get_numbers())
        # and work with it's player
        player = self._chosen_number[self.current]
        # Clear the list to write the new information
        player.clear()
        guessed = ""
        # Compare the  right number with the guessed
        for idx,character in enumerate(number):
            if character == self._numbers[idx]:
                guessed += "x"
            elif character in self._numbers:
                guessed += "o"
            else:
                guessed += "*"
        # Store the information in its list
        player.append(number)
        player.append(guessed)            


    def to_string(self, name):
        """Converts the board data to its string representation.
        Args:
           self (Board): an instance of Board.
        Returns:
            string: A representation of the current board and players names.
        """ 
        text = "\n--------------------"
        ## !IMPORTANT: I dont know how to add the players
        ## name but the information it's ok
        ## You could try to get the roster players in the  director
        ## and bring it here as a parameter, I'm not sure
        for number,guess in self._chosen_number:
            text += (f"\nPlayer {name}: {number}, {guess}")


        text += "\n--------------------"
        return text

    def _prepare(self):
        """Sets up the board with a random number between 1000-9999.
        
        Args:
            self (Board): an instance of Board.
        """
        # To get the random number and transform it into to_string
        # It's necessary to store it as string for the comparisson
        number = random.randint(1000,9999)
        self._numbers = str(number)

    def next_player(self):
        self.current = (self.current + 1) % len(self._chosen_number)