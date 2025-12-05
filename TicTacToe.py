import tkinter as tk
from tkinter import PhotoImage, messagebox
root = tk.Tk()
WIDTH = 475
HEIGHT = 520
root.geometry(f'{WIDTH}x{HEIGHT}')
root.title('Кресики-нолики')
icon = PhotoImage(file='/home/yegor/PythonFiles/Projects/TicTac/image.png')
root.iconphoto(False, icon)
buttons = []
current_player = "X"

def reset_game():
    global current_player
    current_player = "X"
    for button in buttons:
        button.config(text="", bg='grey',fg='white')

def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for comb in winning_combinations:
        a, b, c = comb
        if buttons[a]["text"]  == buttons[b]["text"] == buttons[c]["text"]  != "":
            buttons[a].config(bg='lightgreen', fg='blue')
            buttons[b].config(bg='lightgreen', fg='blue')
            buttons[c].config(bg='lightgreen', fg='blue')
            return True
    return False

def on_click(index):
    global current_player
    if buttons[index]['text']=='':
        buttons[index]['text'] = current_player

        if check_winner():
            if current_player == "X":
                messagebox.showinfo("Победа!", "Победили крестики!")
            else:
                messagebox.showinfo("Победа!", "Победили нолики!")
        elif all(button['text'] != "" for button in buttons):
            for button in buttons:
                button.config(bg='red')
            messagebox.showinfo("", "Ничья!")
        else:
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
        
for i in range(9):
    button = tk.Button(
        root,
        text="",
        font = ('Arial', 14),
        bg='grey',
        fg='white',
        width=13,
        height=7,
        command=lambda idx=i: on_click(idx),
        )
    button.grid(row=i//3, column=i%3)
    buttons.append(button)
reset_button=tk.Button(root, text='Новая игра', font=('Arial', 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, sticky="we")
root.mainloop()
