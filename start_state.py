import game_framework
import hospital_data
import bookmark
from tkinter import *

name = "StartState"

def enter():
    pass

def update():
    pass

def exit():
    window.destroy()
    pass

def go_hodpital():
    game_framework.change_state(hospital_data)

def go_bookmark():
    game_framework.change_state(bookmark)

def run():
    global window
    window = Tk()
    window.title('전국 약국 병원 정보')
    window.geometry('500x500')  # width x height + 가로격자+세로격자

    map = 'Hospital.png'
    img = PhotoImage(file=map)

    map_label = Label(window, image=img)
    map_label.place(x=50, y=50)
    button1 = Button(window,text="병원 조회",command = go_hodpital)
    button1.place(x=150,y=380)

    button2 = Button(window, text="즐겨 찾기", command=go_bookmark)
    button2.place(x=290, y=380)

    window.mainloop()




