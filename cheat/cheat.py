import pyautogui
import time
from tkinter import *
import keyboard
buttonimages = ["click_black.png","click_purple.PNG","click_darkblue.png","click_green.PNG",
                "click_red.png","click_blue.png","click_starting.PNG","click_black1.png","click_purple1.PNG",
                "click_darkblue1.png","click_green1.PNG","click_red1.png","click_blue1.png"]

cheaterapp = Tk()
cheaterapp.title("Cheat-AimSharpener")
cheaterapp.geometry("250x250+100+100")
def terminate():
    cheaterapp.destroy()
def startBot():
    while 1:
        try:
            for img in buttonimages:
                x,y = pyautogui.locateCenterOnScreen("images/"+img,confidence=0.7)
                pyautogui.moveTo(x,y)
                pyautogui.click()
        except:
            time.sleep(.1)
            continue
            

button = Button(text="Click To Start The Clicker Bot",bg="black",fg="white",command=startBot)
button.pack()
label = Label(text="Press 'ESC' to stop the bot",bg="black",fg="red")
label.pack()
keyboard.add_hotkey("esc",terminate)
cheaterapp.mainloop()

    
