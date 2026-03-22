import tkinter
import random
import json

root = tkinter.Tk()
root.geometry("400x125")
root.grid_columnconfigure(2,weight=1)
root.grid_columnconfigure(1,weight=1)
root.grid_columnconfigure(3,weight=1)
root.grid_columnconfigure(4,weight=1)
root.grid_columnconfigure(5,weight=1)
root.grid_columnconfigure(6,weight=1)
choices = ["Rock", "Paper", "Scissors"]

t = {
    "wins" : 0,
    "loses" : 0
}

winss = 0
losess = 0

def change(b):
    global winss
    global losess
    if b:
        winss += 1
        t["wins"] = winss
    else:
        losess += 1
        t["loses"] = losess

def pres(button):
    choice = random.choice(choices)
    global wins, loses
    match button:
        case "Rock":
            if choice == "Rock":
                gam.configure(text="Bot chose Rock, tie!", fg="orange")
            elif choice == "Paper":
                change(False)
                loses.configure(text=f"Loses: {str(losess)}")
                gam.configure(text="Bot chose Paper, You lose!", fg="red")
            else:
                change(True)
                wins.configure(text=f"Wins: {str(winss)}")
                gam.configure(text="Bot chose Scissors, You won!", fg="green")
        case "Paper":
            
            if choice == "Paper":
                gam.configure(text="Bot chose Paper, tie!", fg="orange")
            elif choice == "Scissors":
                
                change(False)
                loses.configure(text=f"Loses: {str(losess)}")
                gam.configure(text="Bot chose Scissors, You lose!", fg="red")
            else:
                
                change(True)
                wins.configure(text=f"Wins: {str(winss)}")
                gam.configure(text="Bot chose Rock, You won!", fg="green")
        case "Scissors":
            if choice == "Scissors":
                gam.configure(text="Bot chose Scissors, tie!", fg="orange")
            elif choice == "Rock":
                
                change(False)
                loses.configure(text=f"Loses: {str(losess)}")
                gam.configure(text="Bot chose Rock, You lose!", fg="red")
            else:
                
                change(True)
                wins.configure(text=f"Wins: {str(winss)}")
                gam.configure(text="Bot chose Paper, You won!", fg="green")

title = tkinter.Label(root, text="RPS: The game", font=("Arial",15,"bold"))
title.grid(column=3, row=1, sticky="n", columnspan=2)

rock = tkinter.Button(root, text="Rock", font=("Arial",10,"bold"), command=lambda: pres("Rock"))
rock.grid(column=1, row=2, sticky="n", columnspan=2)
paper = tkinter.Button(root, text="Paper", font=("Arial",10,"bold"), command=lambda: pres("Paper"))
paper.grid(column=3, row=2, sticky="n", columnspan=2)
scissors = tkinter.Button(root, text="Scissors", font=("Arial",10,"bold"), command=lambda: pres("Scissors"))
scissors.grid(column=5, row=2, sticky="n", columnspan=2)

gam = tkinter.Label(root, text="You haven't played yet", font=("Arial",15,"bold"))
gam.grid(column=3, row=3, sticky="n", columnspan=2)

wins = tkinter.Label(root, text="Wins: 0", font=("Arial",15,"bold"))
wins.grid(column=2, row=4, sticky="n", columnspan=2)
loses = tkinter.Label(root, text="Loses: 0", font=("Arial",15,"bold"))
loses.grid(column=4, row=4, sticky="n", columnspan=2)

root.mainloop()
