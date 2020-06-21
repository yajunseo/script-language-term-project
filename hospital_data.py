import start_state
import bookmark
import game_framework
import xml_data
from tkinter import *
from tkinter import ttk
import xml_data

global check

def go_start():
    game_framework.change_state(start_state)

def go_bookmark():
    game_framework.change_state(bookmark)

def exit():
    window.destroy()
    pass


def run():
    global window
    global check
    check = 1
    window = Tk()
    window.title('병원정보')
    window.geometry('400x600')

    button1 = Button(window, text="메인 화면", command=go_start)
    button1.place(x=0, y=0)

    button2 = Button(window, text="즐겨 찾기", command=go_bookmark)
    button2.place(x=70, y=0)

    label3 = Label(window, text='질병',relief='ridge', width=8, height=1)
    label3.place(x=20, y=100)

    label = Label(window, text='병원 정보',relief='ridge',width=30,height=2)
    label.place(x=90, y=40)

    str2 = StringVar()
    combo = ttk.Combobox(window, width=20, textvariable=str2)
    combo['values'] = ('관상동맥우회술','대장암','정신질환', '천식', '폐암','폐렴', '혈액투석')
    combo.place(x=100, y = 100)
    combo.current(0)
    combo.set('질병 선택')

    label3 = Label(window, text='지역', relief='ridge', width=8, height=1)
    label3.place(x=20, y=150)

    strSigun = StringVar()
    strGrade = StringVar()
    combo3 = ttk.Combobox(window, width=20, textvariable=strSigun)
    combo3['values'] = ('구리시','군포시','부천시','성남시','수원시','시흥시','안산시','안양시','용인시','이천시',
                        '의왕시', '의정부시','파주시', '평택시','포천시','하남시', '화성시',)


    combo3.place(x=100, y=150)
    combo3.set('지역 선택')

    action2 = ttk.Button(window, text="확인", command=lambda: xml_data.Grade(window, combo3.get()))
    action2.place(x=270, y=150)

    def clickMe():
        strSigun = StringVar()
        strGrade = StringVar()
        combo2 = ttk.Combobox(window, width=20, textvariable=strSigun)
        combo2['values'] = ('구리시','군포시','부천시','성남시','수원시','시흥시','안산시','안양시','용인시','이천시',
                        '의왕시', '의정부시','파주시', '평택시','포천시','하남시', '화성시',)
        combo2.place(x=100, y=150)


        if combo.get() == '정신질환':
            action2 = ttk.Button(window, text="확인", command=lambda: xml_data.Grade(window, combo2.get()))
            action2.place(x=270, y=150)

        elif combo.get() == '천식':
            action2 = ttk.Button(window, text="확인", command=lambda: xml_data.Chensick(window,combo2.get()))
            action2.place(x=270, y=150)

        elif combo.get() == '폐렴':
            action2 = ttk.Button(window, text="확인", command=lambda: xml_data.Paeream(window,combo2.get()))
            action2.place(x=270, y=150)

        elif combo.get() == '폐암':
            action2 = ttk.Button(window, text="확인", command=lambda: xml_data.PaeCancer(window,combo2.get()))
            action2.place(x=270, y=150)

        elif combo.get() == '대장암':
            action2 = ttk.Button(window, text="확인", command=lambda: xml_data.DaejangCancer(window, combo2.get()))
            action2.place(x=270, y=150)

        elif combo.get() == '혈액투석':
            action2 = ttk.Button(window, text="확인", command=lambda: xml_data.Blood(window,combo2.get()))
            action2.place(x=270, y=150)

        elif combo.get() == '관상동맥우회술':
            action2 = ttk.Button(window, text="확인", command=lambda: xml_data.GwansangDongmak(window,combo2.get()))
            action2.place(x=270, y=150)


    action = ttk.Button(window, text="확인", command=clickMe)
    action.place(x=270, y=98)



    hosInfo = Listbox(window)
    hosInfo.place(x=20, y=220, width=360, height=360)

    window.mainloop()


#init()
