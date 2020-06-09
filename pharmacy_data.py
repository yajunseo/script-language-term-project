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
    window.title('약국정보')
    window.geometry('400x600')

    button1 = Button(window, text="메인 화면", command=go_start)
    button1.place(x=0, y=0)

    button2 = Button(window, text="병원 정보", command=go_hodpital)
    button2.place(x=70, y=0)

    label3 = Label(window, text='질병선택', relief='ridge', width=8, height=1)
    label3.place(x=20, y=100)

    # 콤보박스
    str2 = StringVar()
    combo = ttk.Combobox(window, width=20, textvariable=str2)
    combo['values'] = ('정신질환', '천식', '폐렴', '폐암', '대장암', '혈액투석', '동맥우회술')
    combo.place(x=100, y=100)
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
            action2 = ttk.Button(window, text="확인", command=lambda: pharmacyPosition(combo2.get()))
            action2.place(x=135, y=260)
            labelMail = Label(window, text='메일전송', relief='ridge', width=8, height=1)
            labelMail.place(x=20, y=320)
            entry = Entry(window)
            entry.place(x= 100, y=320)
            send = ttk.Button(window, text="전송", command=lambda: sendMail(entry.get(), msg=infoMsg))
            send.place(x=260, y=318)

        elif combo.get() == '천식':
            action2 = ttk.Button(window, text="확인", command=lambda: HospitalInfoCehnsick(combo2.get()))
            action2.place(x=135, y=260)
            labelMail = Label(window, text='메일전송', relief='ridge', width=8, height=1)
            labelMail.place(x=20, y=320)
            entry = Entry(window)
            entry.place(x=100, y=320)
            send = ttk.Button(window, text="전송", command=lambda: sendMail(entry.get(), msg=chenMsg))
            send.place(x=260, y=318)

        elif combo.get() == '폐렴':
            action2 = ttk.Button(window, text="확인", command=lambda: HospitalInfoPaeryeom(combo2.get()))
            action2.place(x=135, y=260)
            labelMail = Label(window, text='메일전송', relief='ridge', width=8, height=1)
            labelMail.place(x=20, y=320)
            entry = Entry(window)
            entry.place(x=100, y=320)
            send = ttk.Button(window, text="전송", command=lambda: sendMail(entry.get(), msg=paeRyeomMsg))
            send.place(x=260, y=318)

        elif combo.get() == '폐암':
            action2 = ttk.Button(window, text="확인", command=lambda: HospitalInfopaecancer(combo2.get()))
            action2.place(x=135, y=260)
            labelMail = Label(window, text='메일전송', relief='ridge', width=8, height=1)
            labelMail.place(x=20, y=320)
            entry = Entry(window)
            entry.place(x=100, y=320)
            send = ttk.Button(window, text="전송", command=lambda: sendMail(entry.get(), msg=paecancerMsg))
            send.place(x=260, y=318)

        elif combo.get() == '대장암':
            action2 = ttk.Button(window, text="확인", command=lambda: HospitalInfoDaejangcanser(combo2.get()))
            action2.place(x=135, y=260)
            labelMail = Label(window, text='메일전송', relief='ridge', width=8, height=1)
            labelMail.place(x=20, y=320)
            entry = Entry(window)
            entry.place(x=100, y=320)
            send = ttk.Button(window, text="전송", command=lambda: sendMail(entry.get(), msg=DaecancerMsg))
            send.place(x=260, y=318)

        elif combo.get() == '혈액투석':
            action2 = ttk.Button(window, text="확인", command=lambda: HospitalInfoBlood(combo2.get()))
            action2.place(x=135, y=260)
            labelMail = Label(window, text='메일전송', relief='ridge', width=8, height=1)
            labelMail.place(x=20, y=320)
            entry = Entry(window)
            entry.place(x=100, y=320)
            send = ttk.Button(window, text="전송", command=lambda: sendMail(entry.get(), msg=bloodMsg))
            send.place(x=260, y=318)

        elif combo.get() == '동맥우회술':
            action2 = ttk.Button(window, text="확인", command=lambda: HospitalInfoGwansang(combo2.get()))
            action2.place(x=135, y=260)
            labelMail = Label(window, text='메일전송', relief='ridge', width=8, height=1)
            labelMail.place(x=20, y=320)
            entry = Entry(window)
            entry.place(x=100, y=320)
            send = ttk.Button(window, text="전송", command=lambda: sendMail(entry.get(), msg=gwanMsg))
            send.place(x=260, y=318)

    action = ttk.Button(window, text="확인", command=clickMe)
    action.place(x=135, y=130)

    #str3 = combo.get()
    #print(str3)
    #combo.current(0)

    label = Label(window, text='병원정보서비스',relief='ridge',width=30,height=3)
    label.place(x=90, y=20)
def pharmacyPosition(text):
    mentalUrl = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json?address=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%20%EA%B0%95%EB%82%A8%EA%B5%AC%20%EB%85%BC%ED%98%84%EB%8F%99n"
    res = urllib.request.urlopen(mentalUrl)
    decoding = str(res.read().decode("utf-8"))
    # pprint(decoding)

    data = urllib.request.urlopen(mentalUrl).read()
    f = open("pharmacyPos.xml", "wb")
    f.write(data)
    f.close()

    sigun_Name = []
    hos_Name = []
    div_Name = []
    Grade = []
    addr = []
    addr_Num = []

    tree = ElementTree.parse("hospitalGrade.xml")
    root = tree.getroot()

    for a in root.findall('.//row'):
        sigun_Name.append(a.findtext("SIGUN_NM"))
        hos_Name.append(a.findtext("INST_NM"))
        div_Name.append(a.findtext("DIV_NM"))
        Grade.append(a.findtext("GRAD"))
        addr.append(a.findtext("REFINE_ROADNM_ADDR"))
        addr_Num.append(a.findtext("REFINE_ZIP_CD"))

    count = len(sigun_Name)
    index = 0
    num = 1
    #window = Tk()
    hosInfo = Listbox(window)
    hosInfo.place(x=400, y=10, width=380, height=570)

    global infoMsg

    for i in range (0, count):
        if sigun_Name[i] == text:
            hosInfo.insert(index, '[ ' + str(num) + ' ]')
            index += 1
            hosInfo.insert(index, '등급: ' + Grade[i])
            index += 1
            hosInfo.insert(index, '병원이름: '+ hos_Name[i])
            index +=1
            hosInfo.insert(index, '평가내역: ' + div_Name[i])
            index += 1
            hosInfo.insert(index, '주소:' + addr[i])
            index +=1
            hosInfo.insert(index, '우편번호: ' + addr_Num[i])
            index += 1
            hosInfo.insert(index, '===========================================================')
            index += 1
            num += 1
            if Grade[i] == "1등급":
                infoMsg = str('[ 1등급 병원 정보 ]\n' +
                             '병원이름 : ' + hos_Name[i] + '\n' +
                             '평가내역 : ' + div_Name[i] + '\n' +
                             '등급 : ' + Grade[i] + '\n' +
                             '주소 : ' + addr[i] + '\n' +
                             '우편번호 : ' + addr_Num[i] + '\n' +
                             '===========================================================\n'
                             )


    #hosInfo.insert(1, hosNameList[0])
    #hosInfo.insert(2, hosAddrList[0])

    #hosInfo.insert(0, )

    pass