from tkinter import*

class simple_window():
    def __init__(self):
        self.title = 'Othello'
        self.size = '385x330'
        self.color_dict = {'O': 'white', 'X': 'black', '-': 'green'}
        self.sfen = '---------------------------OX------XO---------------------------B1'

    def init_window(self):
        self.window = Tk()
        self.window.title(self.title)
        self.window.geometry(self.size)
        self.update_board_frame()
        self.window.update()
        return

    def update_board_frame(self):
        D = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
        print_d = {'B': 'Black', 'W': 'White'}
        width = 54
        self.turn_of = Label(self.window, text='Turn of ' + print_d[self.sfen[64]],
                             bg='dark blue', fg='gold', width=width, height=1)
        
        self.turn_of.grid(column=0, row=0)
        self.board_frame = Frame(self.window, width=width, height=27)
        self.sq = []
        for i in range(8):
            rank = []
            for j in range(8):
                rank.append(Label(self.board_frame, text=D[j] + str(i + 1),
                                 fg = 'red', bd=2, bg=self.color_dict[self.sfen[(i * 8) + j]],
                                 relief='ridge', width=6, height=2))
            self.sq.append(rank)
        for i in range(8):
            for j in range(8):
                self.sq[i][j].grid(column=j, row=i)
        self.board_frame.grid(column=0, row=1)

        black_stones = str(self.sfen.count('X'))
        white_stones =  str(self.sfen.count('O'))
        self.stones = Label(self.window, text='Black ' + black_stones + ' | ' + white_stones + ' White',
                            bg='dark blue', fg='gold', width=width, height=1)
        self.stones.grid(column=0, row=2)
        return

    def update_window(self, sfen):
        self.sfen = sfen
        self.update_board_frame()
        self.window.update()
        return

    def del_window(self):
        self.window.destroy()
        return


if __name__ == '__main__':
    import time
    t = simple_window()
    t.init_window()
    sfen = '---------------------------OX------XO---------------------------B1'
    t.update_window(sfen)
    time.sleep(5)
    sfen = '---------------------------OX------XO---------------------------W2'
    t.update_window(sfen)
