from tkinter import Tk, Text
from threading import Thread
import time
from unittest.mock import Mock

start = 0
end = 0
screen = Tk()
game_on = True


def checker():
    global game_on
    while game_on:
        global start
        time.sleep(1)

        if start < 5:
            print(start)
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


mock = Mock(side_effect=key_pressed)
text_area = Text()
text_area.grid()
text_area.bind('<KeyPress>', key_pressed)
text_area.bind('<KeyRelease>', key_released)
thread = Thread(target=checker)
thread.start()

screen.mainloop()
