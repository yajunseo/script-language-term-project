import game_framework
import start_state
import hospital_data
from tkinter import *

global window
global bookMarkInfo

def go_start():
    game_framework.change_state(start_state)

def go_hodpital():
    game_framework.change_state(hospital_data)

def exit():
    window.destroy()
    pass

def booklist():
    global bookMarkInfo
    bookMarkInfo = Listbox(window)
    return bookMarkInfo

def run():

    global window
    global bookMarkInfo
    window = Tk()
    window.title('즐겨찾기')
    window.geometry('400x600')

    button1 = Button(window, text="메인 화면", command=go_start)
    button1.place(x=0, y=0)

    button2 = Button(window, text="병원 정보", command=go_hodpital)
    button2.place(x=70, y=0)

    bookMarkInfo = Listbox(window)
    bookMarkInfo.place(x=20, y=200, width=360, height=340)


    pass