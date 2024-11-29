import tkinter
from tkinter import messagebox

# init window
root = tkinter.Tk()
root.title("Tic Tac Toe ✅")
root.resizable(False, False)
root.geometry("600x600")

# globals
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]  # 3x3


def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None  # no winner


def on_button_click(row, col, button):
    global current_player

    if board[row][col] == "":
        board[row][col] = current_player
        button.config(text=current_player, state="disabled")  # disabled button if clicked
        winner = check_winner()
        if winner:
            messagebox.showinfo("Victory", f"Player {winner} win")
            root.quit()
        elif all(all(cell != "" for cell in row) for row in board):
            messagebox.showinfo("Egual", "No winner")
            root.quit()
        else:  # else next player
            current_player = "O" if current_player == "X" else "X"


# init board
for row in range(3):  # 3 lines

    # grid takes all the size of the window
    root.grid_rowconfigure(row, weight=1)
    root.grid_columnconfigure(row, weight=1)

    for col in range(3):  # 3 rows
        btn = tkinter.Button(root, font=("Arial", 36))
        btn.grid(row=row, column=col, sticky="nsew")  # sticky : each button takes the available space
        btn.config(command=lambda r=row, c=col, b=btn: on_button_click(r, c, b)) # lambda : wait event


# important, dont delete
root.mainloop()


# for ia...
# => https://realpython.com/tic-tac-toe-ai-python/
