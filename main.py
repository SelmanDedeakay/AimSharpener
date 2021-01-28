from tkinter import *
from random import *
import tkinter.messagebox

reply = tkinter.messagebox.askyesno("Menu", "Hard Mode?")
colors = ["black","green","red","dark blue","purple","blue"]
app = Tk()
app.iconbitmap('logo.ico')
app.title("Aim Sharpener")
app.resizable(False,False)
app.configure(bg="dark gray")
app.geometry("520x526+500+100")
app.counter = 0

countdownLabel = Label(app,fg="white",bg="black")
countdownLabel.place(x=15, y=15)
replay = False
def countdown(count):
    countdownLabel['text'] = f"Remaining time: {count}"
    global scoreButton
    global replay
    if count > 0:
        app.after(1000, countdown, count - 1)
    elif count == 0:
        again = tkinter.messagebox.askyesno(title="Game Over", message="Time is up!" + ' Point: ' + str(
            (app.counter) * 5) + "\nWould you like to play again?")
        if again == True:
            reply = tkinter.messagebox.askyesno("Menu", "Hard Mode?")
            replay = True
            if reply == True:
                countdown(30)
                scoreButton.destroy()
                scoreButton = Button(app, text="X", command=getPoint)
                scoreButton.pack()
                
            else:
                countdown(30)
                scoreButton.destroy()
                scoreButton = Button(app, text="Click!", command=getPoint)
                scoreButton.pack()
                
        else:
            app.destroy()


def getPoint():
    global replay
    app.counter += 1
    if replay == True:
        app.counter = 1
        replay = False
    scoreLabel['text'] = 'Point: ' + str((app.counter) * 5)
    scoreButton["fg"] = choice(colors)
    scoreButton.place(x=randint(100, 480), y=randint(100, 480))
if reply == True:
    countdown(30)
    scoreButton = Button(app,command=getPoint,text ="X")
    scoreButton.pack()
else:
    countdown(30)
    scoreButton = Button(app, text="Click!", command=getPoint)
    scoreButton.pack()


scoreLabel = Label(app, text="No clicks yet.",fg="white",bg="black")
scoreLabel.pack()

app.mainloop()
