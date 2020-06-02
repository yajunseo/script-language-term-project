import game_framework
import hospital_data
import pharmacy_data
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

def go_pharmacy():
    game_framework.change_state(pharmacy_data)

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

    button2 = Button(window, text="약국 조회", command=go_pharmacy)
    button2.place(x=290, y=380)

    window.mainloop()




