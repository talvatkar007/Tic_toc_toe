import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        self.c_player = 'X'
        self.winner_found = False

        self.label = tk.Label(self.root, text=f"Player {self.c_player}'s turn", font=('Arial', 24))
        self.label.grid(row=3, column=0, columnspan=3)

        self.buttons = [tk.Button(self.root, text="", font=('Arial', 24), width=5, height=2, 
                                  command=lambda i=i: self.button_click(i)) for i in range(9)]

        for i, button in enumerate(self.buttons):
            button.grid(row=i//3, column=i%3)

    def button_click(self, index):
        if self.buttons[index]['text'] == "" and not self.winner_found:
            self.buttons[index]['text'] = self.c_player
            self.check_winner()
            if not self.winner_found:
                self.toggle_player()

    def toggle_player(self):
        self.c_player = 'O' if self.c_player == 'X' else 'X'
        self.label.config(text=f"Player {self.c_player}'s turn")

    def check_winner(self):
        win_combos = [
            [0,1,2], [3,4,5], [6,7,8],  # Rows
            [0,3,6], [1,4,7], [2,5,8],  # Columns
            [0,4,8], [2,4,6]            # Diagonals
        ]

        for combo in win_combos:
            if (self.buttons[combo[0]]['text'] == self.buttons[combo[1]]['text'] == self.buttons[combo[2]]['text'] != ""):
                for i in combo:
                    self.buttons[i].config(bg='green')
                self.winner_found = True
                messagebox.showinfo("Winner", f"{self.buttons[combo[0]]['text']} wins!")
                self.root.quit()
                break

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
