import game_framework
import urllib
from urllib.request import Request
from urllib.request import urlopen
from urllib.parse import quote_plus
from urllib.parse import urlencode
import json
from pprint import pprint
from xml.etree import ElementTree
import smtplib
from email.mime.text import MIMEText

from tkinter import Tk, ttk, StringVar,messagebox
from tkinter import *
from tkinter import ttk
import xml_data


def sendMail(you, msg):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login('skuin2004@gmail.com', 'fyqagbhejffalhew')
    msg = MIMEText(msg)
    msg['Subject'] = '병원정보서비스'
    smtp.sendmail('skuin2004@gmail.com', you, msg.as_string())
    smtp.quit()
    messagebox.showinfo("메일전송", you+"로 메일을 전송하였습니다.")

#sendMail("skuin2004@naver.com", "테스트 메일")

def run():
    global window
    window = Tk()
    window.title('병원정보')
    window.geometry('800x600')

    label3 = Label(window, text='질병선택',relief='ridge', width=8, height=1)
    label3.place(x=20, y=100)

    # 콤보박스
    str2 = StringVar()
    combo = ttk.Combobox(window, width=20, textvariable=str2)
    combo['values'] = ('정신질환', '천식', '폐렴', '폐암', '대장암', '혈액투석', '관상동맥우회술')
    combo.place(x=100, y = 100)
    combo.current(0)

    def clickMe():
        label = Label(window, text=combo.get(), relief='ridge', width=15, height=2)
        label.place(x=120, y=180)

        label2 = Label(window, text='지역선택', relief='ridge', width=8, height=1)
        label2.place(x=20, y=230)

        strSigun = StringVar()
        strGrade = StringVar()
        combo2 = ttk.Combobox(window, width=20, textvariable=strSigun)
        combo2['values'] = ('수원시', '구리시', '군포시', '부천시', '성남시', '시흥시', '안산시', '안양시', '평택시', '화성시',
                            '하남시', '포천시', '파주시', '이천시', '의정부시', '의왕시', '용인시')
        combo2.place(x=100, y=230)
        combo2.set('시도군 선택')

        if combo.get() == '정신질환':
            action2 = ttk.Button(window, text="확인", command=lambda: xml_data.Grade(window, combo2.get()))
            action2.place(x=135, y=260)
            labelMail = Label(window, text='메일전송', relief='ridge', width=8, height=1)
            labelMail.place(x=20, y=320)
            entry = Entry(window)
            entry.place(x= 100, y=320)
            send = ttk.Button(window, text="전송", command=lambda: sendMail(entry.get(), msg=infoMsg))
            send.place(x=260, y=318)

        elif combo.get() == '천식':
            action2 = ttk.Button(window, text="확인", command=lambda: xml_data.Chensick(window,combo2.get()))
            action2.place(x=135, y=260)
            labelMail = Label(window, text='메일전송', relief='ridge', width=8, height=1)
            labelMail.place(x=20, y=320)
            entry = Entry(window)
            entry.place(x=100, y=320)
            send = ttk.Button(window, text="전송", command=lambda: sendMail(entry.get(), msg=chenMsg))
            send.place(x=260, y=318)

        elif combo.get() == '폐렴':
            action2 = ttk.Button(window, text="확인", command=lambda: xml_data.Paeream(window,combo2.get()))
            action2.place(x=135, y=260)
            labelMail = Label(window, text='메일전송', relief='ridge', width=8, height=1)
            labelMail.place(x=20, y=320)
            entry = Entry(window)
            entry.place(x=100, y=320)
            send = ttk.Button(window, text="전송", command=lambda: sendMail(entry.get(), msg=paeRyeomMsg))
            send.place(x=260, y=318)

        elif combo.get() == '폐암':
            action2 = ttk.Button(window, text="확인", command=lambda: xml_data.PaeCancer(window,combo2.get()))
            action2.place(x=135, y=260)
            labelMail = Label(window, text='메일전송', relief='ridge', width=8, height=1)
            labelMail.place(x=20, y=320)
            entry = Entry(window)
            entry.place(x=100, y=320)
            send = ttk.Button(window, text="전송", command=lambda: sendMail(entry.get(), msg=paecancerMsg))
            send.place(x=260, y=318)

        elif combo.get() == '대장암':
            action2 = ttk.Button(window, text="확인", command=lambda: xml_data.DaejangCancer(window, combo2.get()))
            action2.place(x=135, y=260)
            labelMail = Label(window, text='메일전송', relief='ridge', width=8, height=1)
            labelMail.place(x=20, y=320)
            entry = Entry(window)
            entry.place(x=100, y=320)
            send = ttk.Button(window, text="전송", command=lambda: sendMail(entry.get(), msg=DaecancerMsg))
            send.place(x=260, y=318)

        elif combo.get() == '혈액투석':
            action2 = ttk.Button(window, text="확인", command=lambda: xml_data.Blood(window,combo2.get()))
            action2.place(x=135, y=260)
            labelMail = Label(window, text='메일전송', relief='ridge', width=8, height=1)
            labelMail.place(x=20, y=320)
            entry = Entry(window)
            entry.place(x=100, y=320)
            send = ttk.Button(window, text="전송", command=lambda: sendMail(entry.get(), msg=bloodMsg))
            send.place(x=260, y=318)

        elif combo.get() == '관상동맥우회술':
            action2 = ttk.Button(window, text="확인", command=lambda: xml_data.GwansangDongmak(window,combo2.get()))
            action2.place(x=135, y=260)
            labelMail = Label(window, text='메일전송', relief='ridge', width=8, height=1)
            labelMail.place(x=20, y=320)
            entry = Entry(window)
            entry.place(x=100, y=320)
            send = ttk.Button(window, text="전송", command=lambda: sendMail(entry.get(), msg=gwanMsg))
            send.place(x=260, y=318)

    action = ttk.Button(window, text="확인", command=clickMe)
    action.place(x=135, y=130)



    label = Label(window, text='병원정보서비스',relief='ridge',width=30,height=3)
    label.place(x=90, y=20)



    photo = PhotoImage(file="hospital.gif")
    imageLabel = Label(window, image=photo)
    imageLabel.place(x= 60, y=380)

    hosInfo = Listbox(window)
    hosInfo.place(x=400, y=10, width=380, height=570)

    window.mainloop()


#init()
