import textwrap

from board import Board
from player import Player


class TicTacToeGame:

    def start(self):
        print(textwrap.dedent('''
        ****************************
           Welcome to Tic-Tac-Toe
        ****************************
        '''))
        board = Board()
        player_name = input("Enter your name: ")
        player = Player(player_name)
        computer = Player(is_human=False)

        while True:
            board.print_board()
            while True:
                human_move = player.get_human_move()
                board.submit_move(player, human_move)
                board.print_board()

                if board.check_is_tie():
                    print("It's a tie! Try again 👍")
                    break
                elif board.check_is_game_over(player, human_move):
                    print(f"Excellent {player.name}! You won this round 🎉")
                    break
                else:
                    computer_move = player.get_computer_move()
                    board.submit_move(computer, computer_move)
                    board.print_board()

                    if board.check_is_game_over(computer, computer_move):
                        print("Oops....😲 The computer won. Try again.")
                        break

            play_again = input("Would you like to play again?\n"
                               "Enter Y/N: ").upper()

            if play_again == "N":
                print("Bye! Come back soon 👋")
                break
            elif play_again == "Y":
                self.start_new_round(board)
            else:
                print("Invalid input!\n"
                      "we assume that you don't want to continue. 👋")
                break

    def start_new_round(self, board):
        print(textwrap.dedent('''
        ********************
          New round begins
        ********************
        '''))
        board.reset_board()
        Player.reset_input_choices()
