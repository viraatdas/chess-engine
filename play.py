from distutils.sysconfig import get_config_h_filename
from engine import Engine
from constants import VALID_COLOR_LIST


class Game:
    def __init__(self) -> None:
        self.HUMAN_COLOR = None
        self.CPU_COLOR = None
        self.engine = None

    def get_game_status(self):
        """
        return True if game is over (checkmate or stalemate)
        """
        is_checkmate = self.engine.is_checkmate()
        if is_checkmate:
            print(f"Checkmated")
            return True

        is_stalamate = self.engine.is_stalemate()
        if is_stalamate:
            print("Stalemate")
            return True

        is_check = self.engine.is_check()
        if is_check:
            print("Check")

        return False

    def human_make_next_move(self):
        """
        get input from user and make move if valid
        if not valid, print error message and ask again
        """
        input_move = input(f"{self.HUMAN_COLOR} Enter move: ")
        sucessfully_moved = self.engine.input_make_move(input_move)

        while not sucessfully_moved:
            print("Invalid move")
            input_move = input(f"{self.HUMAN_COLOR} Enter move: ")
            sucessfully_moved = self.engine.input_make_move(input_move)

        return input_move

    def cpu_make_next_move(self):
        move = self.engine.make_next_move()
        print(f"({self.CPU_COLOR}) CPU is moving: {move}")

    def game_setup(self):
        self.HUMAN_COLOR = input(
            "What color do you want to play as? (white/black) ")

        while self.HUMAN_COLOR not in VALID_COLOR_LIST:
            print("Invalid color. Please enter 'white' or 'black'.")
            self.HUMAN_COLOR = input(
                "What color do you want to play as? (white/black)")

        self.CPU_COLOR = VALID_COLOR_LIST[1]
        self.engine = Engine()

    def play(self):
        self.game_setup()

        # if human is black, CPU makes the first move
        if self.HUMAN_COLOR == VALID_COLOR_LIST[1]:
            self.cpu_make_next_move()
            self.CPU_COLOR = VALID_COLOR_LIST[0]

        is_game_terminated = self.get_game_status()

        while not is_game_terminated:
            self.engine.print_board()
            self.human_make_next_move()
            self.cpu_make_next_move()
            is_game_terminated = self.get_game_status()


game = Game()
game.play()
