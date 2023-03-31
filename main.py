from tkinter import Tk, Text, Label
from threading import Thread
import time
from unittest.mock import Mock

start = 0
end = 0
screen = Tk()
game_on = True
screen.title("Dangerous Text Editor")

def checker():
    global game_on
    while game_on:
        global start
        time.sleep(1)

        if start < 6:
            if start > 0 :
                label.config(text=f'Tick-Tick : {start}', background="pink")
            else:
                label.config(text="You fine for now", background="green")
            if mock.called:
                start = 0
            else:
                start += 1
        else:
            screen.quit()
            game_on = False


def key_released(d):
    global start
    start = 0


def key_pressed(d):
    global end
    end = d


# Mock to check if the function is called or not
mock = Mock(side_effect=key_pressed)

# label
label = Label(screen,text="You fine for now", background="green")
label.pack()

# Text area
text_area = Text(screen)
text_area.pack()
text_area.bind('<KeyPress>', key_pressed)
text_area.bind('<KeyRelease>', key_released)

# threading the checker function so that we can count how many seconds the typer is not typing
thread = Thread(target=checker)
thread.start()

screen.mainloop()
