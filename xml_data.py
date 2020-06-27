import urllib
from urllib.request import Request
from xml.etree import ElementTree
import tkinter
from tkinter import *
from tkinter import ttk
import hospital_data
import bookmark


def Infromation(window, text):

    def marking():
        bookmarklist = bookmark.booklist()
        for i in range(0, count):
            print(SIGUN_NM[i])
            if SIGUN_NM[i] == text:
                bookmarklist.insert(index, '병원이름: ' + INST_NM[i])
                index += 1
                bookmarklist.insert(index, '도로명주소: ' + LOTTION_ADDR[i])
                index += 1
                bookmarklist.insert(index, '지번주소: ' + ROADNM_ADDR[i])
                index += 1
                bookmarklist.insert(index, '우편번호: ' + ZIP_CD[i])
                index += 1
                bookmarklist.insert(index,
                               '--------------------------------------------------------------------------------------')
                index += 1
                num += 1
        pass



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
        INST_NM.append(i.findtext("INST_NM"))
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
    hosInfo.place(x=20, y=200, width=360, height=340)

    print(hospital_data.check)

    for i in range(0, count):
        print(SIGUN_NM[i])
        if SIGUN_NM[i] == text:
            hosInfo.insert(index, '병원이름: ' + INST_NM[i])
            index += 1
            hosInfo.insert(index, '도로명주소: ' + LOTTION_ADDR[i])
            index += 1
            hosInfo.insert(index, '지번주소: ' + ROADNM_ADDR[i])
            index += 1
            hosInfo.insert(index, '우편번호: ' + ZIP_CD[i])
            index += 1
            hosInfo.insert(index, '--------------------------------------------------------------------------------------')
            index += 1
            num += 1


    label5 = Label(window, text='즐겨찾기', relief='ridge', width=9, height=1)
    label5.place(x=20, y=560)

    edit = tkinter.Entry(window, width = 25)
    edit.place(x= 100,y = 560)


    action3 = ttk.Button(window, text="등록", command = marking)
    action3.place(x=290, y=560)


    window.mainloop()
    pass

def Mental(window, text):
    url = "https://openapi.gg.go.kr/Hosptlevaltnpsychs?Key=87b45899e7ae4c1abd87299b4ef3ce04&pIndex=1&pSize=100"
    response = urllib.request.urlopen(url)
    str(response.read().decode("utf-8"))

    xmldata = urllib.request.urlopen(url).read()
    file = open("hospital_inform.xml", "wb")
    file.write(xmldata)
    file.close()
    Infromation(window, text)
    pass

def Paeream(window, text,check):
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