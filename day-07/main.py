import tkinter

# init window
root = tkinter.Tk()
root.title("Tic Tac Toe ✅")
root.resizable(False, False)
root.geometry("600x600")

# init board
for row in range(3):  # 3 lines

    # grid takes all the size of the window
    root.grid_rowconfigure(row, weight=1)
    root.grid_columnconfigure(row, weight=1)

    for col in range(3):  # 3 rows
        btn = tkinter.Button(root)
        btn.grid(row=row, column=col, sticky="nsew")  # sticky : each button takes the available space

# important, dont delete
root.mainloop()
