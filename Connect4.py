from tkinter import *
from tkinter import messagebox
import numpy as np

root = Tk()

# X starts so true
clicked = True
count = 0

# disable all the buttons
def disable_all_buttons(buttonList):
    for x in np.nditer(buttonList):
        x.config(state = DISABLED)

# Check to see if someone won
def checkifwon(bm):
    winner = False
    for ray in bm: 
        for c in range (4):
            if ray[c]["text"] == ray[c+1]["text"] and ray[c+1]["text"] == ray[c+2]["text"] and ray[c+2]["text"] == ray[c+3]["text"] and ray[c]["text"] != " ":
                    winner = True
                    messagebox.showinfo("Connect Four", "CONGRATULATIONS!" + " " + ray[c]["text"] + " WINS!!")
                    disable_all_buttons()
    bm2 = np.transpose(bm)
    for ray in bm2: 
        for c in range (3):
            if ray[c]["text"] == ray[c+1]["text"] and ray[c+1]["text"] == ray[c+2]["text"] and ray[c+2]["text"] == ray[c+3]["text"] and ray[c]["text"] != " ":
                    winner = True
                    messagebox.showinfo("Connect Four", "CONGRATULATIONS!" + " " + ray[c]["text"] + " WINS!!")
                    disable_all_buttons()
    ## diags
    for i in range(6):
        for j in range(7):
            y = i
            x = j
            prev = bm[y][x].cget('bg')
            cnt = 1

            if prev != "RED" and prev != "YELLOW":
                continue

            while y < 5 and x < 6:
                y += 1
                x += 1
                bColor = bm[y][x].cget('bg')
                if prev == bColor:
                    prev = bColor
                    cnt += 1
                else:
                    break

            if cnt >= 4:
                if bm[i][j].cget('bg') == "RED": 
                    messagebox.showinfo("Connect Four","CONGRATULATIONS!" + " RED WINS!!")
                else:
                    messagebox.showinfo("Connect Four","CONGRATULATIONS!" + " YELLOW WINS!!")
                winner = True
                disable_all_buttons()
    for i in range(6):
        for j in range(7):
            y = i
            x = j
            prev = bm[y][x].cget('bg')
            cnt = 1

            if prev != "RED" and prev != "YELLOW":
                continue

            while y < 5 and x > 0:
                y += 1
                x -= 1
                bColor = bm[y][x].cget('bg')
                if prev == bColor:
                    prev = bColor
                    cnt += 1
                else:
                    break

            if cnt >= 4:
                if bm[i][j].cget('bg') == "RED": 
                    messagebox.showinfo("Connect Four","CONGRATULATIONS!" + " RED WINS!!")
                else:
                    messagebox.showinfo("Connect Four","CONGRATULATIONS!" + " YELLOW WINS!!")
                winner = True
                disable_all_buttons()
    # Check if tie
    if count == 42 and winner == False:
        messagebox.showinfo("Connect Four", "It's A Tie!\n No One Wins!")
        disable_all_buttons()

# Button clicked function
def b_click(bm, j):
    global clicked, count   
    bmt = np.transpose(bm)
    
    for b in reversed(bmt[j]):
        if b["text"] == " ":
            if clicked == TRUE:
                b.config(bg="RED")
                b["text"] = "RED"
            else:
                b.config(bg="YELLOW")
                b["text"] = "YELLOW"
            clicked = not clicked
            count += 1
            checkifwon(bm)
            break
            

def makeButton(i, j, buttonList):
    x = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="GRAY", command=lambda: b_click(buttonList, j), activebackground="ORANGE", bd=1)
    x.grid(row = i, column= j)
    return x 

def reset():
    buttonList = [[],[],[],[],[],[]]
    for i in range (0,6):
        for j in range (0,7):
            buttonList[i].append(makeButton(i, j, buttonList))


    
# Create menue
my_menu = Menu(root)
root.config(menu=my_menu)
reset()
root.mainloop()
