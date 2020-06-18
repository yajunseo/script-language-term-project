import game_framework
import start_state
import hospital_data
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


def go_start():
    game_framework.change_state(start_state)

def go_hodpital():
    game_framework.change_state(hospital_data)

def exit():
    window.destroy()
    pass

def run():

    global window
    window = Tk()
    window.title('즐겨찾기')
    window.geometry('400x600')

    button1 = Button(window, text="메인 화면", command=go_start)
    button1.place(x=0, y=0)

    button2 = Button(window, text="병원 정보", command=go_hodpital)
    button2.place(x=70, y=0)


    pass