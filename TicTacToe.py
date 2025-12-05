import tkinter as tk
from tkinter import PhotoImage
root = tk.Tk()
WIDTH = 500
HEIGHT = 500
root.geometry(f'{WIDTH}x{HEIGHT}')
root.title('Кресики-нолики')
icon = PhotoImage(file='/home/yegor/PythonFiles/Projects/TicTac/image.png')
root.iconphoto(False, icon)
buttons = []
current_player = "X"

def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for comb in winning_combinations:
        a, b, c = comb
        if buttons[a]["text"]  == buttons[b]["text"] == buttons[c]["text"]  != "":
            return True
    return False

def on_click(index):
    global current_player
    if buttons[index]['text']=='':
        buttons[index]['text'] = current_player

        if check_winner():
            if current_player == "X":
                print("Победили крестики")
            else:
                print("Победили нолики")
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
        
for i in range(9):
    button = tk.Button(
        root,
        text="",
        font = ('Arial', 14),
        width=13,
        height=7,
        command=lambda idx=i: on_click(idx),
        )
    button.grid(row=i//3, column=i%3)
    buttons.append(button)
root.mainloop()
