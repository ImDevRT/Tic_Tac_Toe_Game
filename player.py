import random

from move import Move


class Player:

    PLAYER_MARKER = "X"
    COMPUTER_MARKER = "O"
    move_choices = list(range(1, 10))

    def __init__(self, name="Player", is_human=True):
        self._name = name
        self._is_human = is_human

        if is_human:
            self._marker = Player.PLAYER_MARKER
        else:
            self._marker = Player.COMPUTER_MARKER

    @property
    def name(self):
        return self._name

    @property
    def is_human(self):
        return self._is_human

    @property
    def marker(self):
        return self._marker

    def get_move(self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()

    def get_human_move(self):
        while True:
            user_input = int(input("Enter your move (1-9): "))
            move = Move(user_input)
            if move.is_valid():
                Player.move_choices.remove(move.value)
                break
            else:
                print("Please enter an integer between 1 to 9.\n")
        return move

    def get_computer_move(self):
        random_choice = random.choice(Player.move_choices)
        Player.move_choices.remove(random_choice)
        move = Move(random_choice)
        print(f"Computer's move is: {move.value}\n")
        return move

    @classmethod
    def reset_input_choices(cls):
        cls.move_choices = list(range(1, 10))
