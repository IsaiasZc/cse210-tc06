import random

class Board:
    
    def __init__(self):
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


    def to_string(self):
        text = "\n--------------------"
        """!IMPORTANT: The only thing that we could not 
        figure out was how to insert players names in their
        appropriate postion"""
        for number,guess in self._chosen_number:
            text += (f"\nPlayer #: {number},{guess}")


        text += "\n--------------------"
        return text

    def _prepare(self):
        # To get the random number and transform it into to_string
        # It's necessary to store it as string for the comparisson
        number = random.randint(1000,9999)
        self._numbers = str(number)

    def next_player(self):
        self.current = (self.current + 1) % len(self._chosen_number)