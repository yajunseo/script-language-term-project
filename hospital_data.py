import game_framework
import start_state
import pharmacy_data
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

# 정신과
# https://openapi.gg.go.kr/Hosptlevaltnpsychs?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100
# 천식
# https://openapi.gg.go.kr/Hosptlevaltnast?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100
# 폐렴
# https://openapi.gg.go.kr/Hosptlevaltnpen?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100
# 혈액투석
# https://openapi.gg.go.kr/Hosptlevaltnboldi?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100
# 폐암
# https://openapi.gg.go.kr/Hosptlevaltnlunc?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100
# 관상동맥우회술
# https://openapi.gg.go.kr/Hosptlevaltncorarby?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100
# 대장암
# https://openapi.gg.go.kr/Hosptlevaltnlgsnc?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100

# 약처방비용
# https://openapi.gg.go.kr/Hosptlevaltnmcex?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100

def go_start():
    game_framework.change_state(start_state)

def go_pharmacy():
    game_framework.change_state(pharmacy_data)


def exit():
    window.destroy()
    pass


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
    window.geometry('400x600')

    button1 = Button(window, text="메인 화면", command=go_start)
    button1.place(x=0, y=0)

    button2 = Button(window, text="약국 정보", command=go_pharmacy)
    button2.place(x=70, y=0)

