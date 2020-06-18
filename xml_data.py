import urllib
from urllib.request import Request
from urllib.request import urlopen
from urllib.parse import quote_plus
from urllib.parse import urlencode
import json
from xml.etree import ElementTree
from tkinter import Tk, ttk, StringVar,messagebox
from tkinter import *
from tkinter import ttk

from pprint import pprint
import smtplib

def Infromation(window, text):
    global message

    SIGUN_NM = []
    SIGUN_CD = []
    INST_NM = []
    DIV_NM = []
    GRAD = []
    LOTTION_ADDR = []
    ROADNM_ADDR = []
    ZIP_CD = []
    LOGT = []
    LAT = []

    tree = ElementTree.parse("hospital_inform.xml")
    root = tree.getroot()

    for i in root.findall('.//row'):
        SIGUN_NM.append(i.findtext("SIGUN_NM"))
        SIGUN_CD.append(i.findtext("SIGUN_CD"))
        INST_NM.append(i.findtext("INST_NM"))
        DIV_NM.append(i.findtext("DIV_NM"))
        GRAD.append(i.findtext("GRAD"))
        LOTTION_ADDR.append(i.findtext("REFINE_LOTNO_ADDR"))
        ROADNM_ADDR.append(i.findtext("REFINE_ROADNM_ADDR"))
        ZIP_CD.append(i.findtext("REFINE_ZIP_CD"))
        LOGT.append(i.findtext("REFINE_WGS84_LOGT"))
        LAT.append(i.findtext("REFINE_WGS84_LAT"))

    count = len(SIGUN_NM)
    print(count)
    index = 0
    num = 1
    hosInfo = Listbox(window)
    hosInfo.place(x=20, y=200, width=360, height=380)


    for i in range(0, count):
        print(SIGUN_NM[i])
        if SIGUN_NM[i] == text:
            hosInfo.insert(index, '[ ' + str(num) + ' ]')
            index += 1
            hosInfo.insert(index, '등급: ' + GRAD[i])
            index += 1
            hosInfo.insert(index, '병원이름: ' + INST_NM[i])
            index += 1
            hosInfo.insert(index, '평가내역: ' + DIV_NM[i])
            index += 1
            hosInfo.insert(index, '주소:' + LOTTION_ADDR[i])
            index += 1
            hosInfo.insert(index, '우편번호: ' + ZIP_CD[i])
            index += 1
            hosInfo.insert(index, '===========================================================')
            index += 1
            num += 1


    pass

def Grade(window, text):
    url = "https://openapi.gg.go.kr/Hosptlevaltnpsychs?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100"
    response = urllib.request.urlopen(url)
    str(response.read().decode("utf-8"))

    xmldata = urllib.request.urlopen(url).read()
    file = open("hospital_inform.xml", "wb")
    file.write(xmldata)
    file.close()
    Infromation(window, text)
    pass

def Paeream(window, text):
    url = "https://openapi.gg.go.kr/Hosptlevaltnpen?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100"
    response = urllib.request.urlopen(url)
    str(response.read().decode("utf-8"))

    xmldata = urllib.request.urlopen(url).read()
    file = open("hospital_inform.xml", "wb")
    file.write(xmldata)
    file.close()
    Infromation(window, text)

    pass

def Chensick(window, text):
    url = "https://openapi.gg.go.kr/Hosptlevaltnast?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100"
    response = urllib.request.urlopen(url)
    str(response.read().decode("utf-8"))

    xmldata = urllib.request.urlopen(url).read()
    file = open("hospital_inform.xml", "wb")
    file.write(xmldata)
    file.close()
    Infromation(window, text)

    pass

def Blood(window, text):
    url = "https://openapi.gg.go.kr/Hosptlevaltnboldi?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100"
    response = urllib.request.urlopen(url)
    str(response.read().decode("utf-8"))

    xmldata = urllib.request.urlopen(url).read()
    file = open("hospital_inform.xml", "wb")
    file.write(xmldata)
    file.close()
    Infromation(window,text)

    pass

def PaeCancer(window, text):
    url = "https://openapi.gg.go.kr/Hosptlevaltnlunc?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100"
    response = urllib.request.urlopen(url)
    str(response.read().decode("utf-8"))

    xmldata = urllib.request.urlopen(url).read()
    file = open("hospital_inform.xml", "wb")
    file.write(xmldata)
    file.close()
    Infromation(window,text)

    pass

def GwansangDongmak(window, text):
    url = "https://openapi.gg.go.kr/Hosptlevaltncorarby?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100"
    response = urllib.request.urlopen(url)
    str(response.read().decode("utf-8"))

    xmldata = urllib.request.urlopen(url).read()
    file = open("hospital_inform.xml", "wb")
    file.write(xmldata)
    file.close()
    Infromation(window, text)

    pass

def DaejangCancer(window, text):
    url = "https://openapi.gg.go.kr/Hosptlevaltnlgsnc?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100"
    response = urllib.request.urlopen(url)
    str(response.read().decode("utf-8"))

    xmldata = urllib.request.urlopen(url).read()
    file = open("hospital_inform.xml", "wb")
    file.write(xmldata)
    file.close()
    Infromation(window, text)

    pass

def Price(window, text):
    url = "https://openapi.gg.go.kr/Hosptlevaltnmcex?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100"
    response = urllib.request.urlopen(url)
    str(response.read().decode("utf-8"))

    xmldata = urllib.request.urlopen(url).read()
    file = open("hospital_inform.xml", "wb")
    file.write(xmldata)
    file.close()
    Infromation(window, text)

    pass