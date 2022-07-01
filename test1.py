import creversi as reversi
from Board_to_sfen import board_to_sfen
import numpy as np
from othello_sfen_viewer1 import simple_window
import time

def test():
    window = simple_window()
    board = reversi.Board()
    window.init_window()
    for i in range(60):
        board.move(np.random.choice(list(board.legal_moves)))
        sfen = board_to_sfen(board, i + 2)
        window.update_window(sfen)
        time.sleep(0.1)
        if board.is_game_over():
            break
    input('すすむ:')
    window.del_window()
    input('おわり:')
    return

test()
