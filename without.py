from urllib import response
import mechanize
import os
import datetime
import sys
import requests
import json,time
from time import sleep
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]
browser.set_handle_refresh(False)

url = 'https://m.facebook.com/login.php'

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def sp(stri):
    for letter in stri:
        print(letter, end = "")
        sys.stdout.flush()
        sleep(0.03)

ah="--M4FIY4--"
imt="-M9FIY497384=="
ak=" M4FIY4 KING-"
try:
	key1 = open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'r').read()
except:
	kok=open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'w')
	kok.write(myid+imt)
	kok.close()

logo =  """\033[1;35;40m     

\033[1;35;40m| ███╗░░░███╗░█████╗░███████╗██╗██╗░░░██╗░█████╗░ 
\033[1;35;40m| ████╗░████║██╔══██╗██╔════╝██║╚██╗░██╔╝██╔══██╗
\033[1;35;40m| ██╔████╔██║███████║█████╗░░██║░╚████╔╝░███████║  
\033[1;35;40m| ██║╚██╔╝██║██╔══██║██╔══╝░░██║░░╚██╔╝░░██╔══██║
\033[1;35;40m| ██║░╚═╝░██║██║░░██║██║░░░░░██║░░░██║░░░██║░░██║
\033[1;35;40m| ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝ 
                                                   
                                                   
                                                   
__________________________________________  
\033[1;34;40m[+]============================================== 
\033[1;34;40m[+] CREATED BY   :  M9FIY9 TH3 L09D3R KING
\033[1;34;40m[+] ON GITHUB    :  M9FIY9-D0N H3R3    
\033[1;34;40m[+] TOOL STATUS  :  INB0X L09D3R 
 \033[1;34;40m[+] TOOL VIRSION :  2.0  
\033[1;34;40m[+]============================================== """

def Subscraption():
	key1=open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'r').read()
	clear()
	print(logo)
	r1=requests.get("https://github.com/Mafiyahunter/convo/blob/main/approval.txt").text
	if key1 in r1:
		os.system('clear')
		print(logo)
		logo
	else:
		os.system("clear")
		print(logo)
		print("\t \033[1;32m First Get Approvel\033[1;37m ")
		time.sleep(1)
		os.system("clear")
		print(logo)
		print ("")
		print(" \033[1;32m M4FIY4 K4 T00L T3R4 B44P FR33 M3 L3N3 4Y4 TH4 KI T3RI M44\033[1;37m\n")
		print(" \033[1;32m Note : L4WRD3 KH4RID L3 T3R3 B44P K4 T00L N4HI H4I FR33 M3 MILEG4   \033[1;37m")
		print ("")
		print("4PPR0V4L L3L3 L4WRD3 ")
		print("")
		print("4PN3 B44P K3 P4SS K3Y BH3J CH4L ")
		print ("")
		print (" Your Key : "+ak+ah+key1 )
		print ("")
		name = input(" T3R3 B44P K4 N4M3 B4T4 : ")
		print ("")
		gf = input(" T3RI 3K L0TI R4NDI K4 N4M3 B4T4 : ")
		print ("")
		lol = input(" T3R3 JH4T BH4R K3 T4T3 K4 N44M B4T4 : ")
		print ("")
		input(" Press Enter To Send Key")
		time.sleep(3.5)
		tks = 'Mafiya%20Papa,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Email%20:%20'+lol+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+ak+ah+key1
		os.system('am start https://wa.me/+919971945685?text=' + tks)
		Subscraption()
Subscraption()

def Login():
    browser.open(url)
    browser.select_form(nr = 0)
    browser.form['email'] = USERNAME
    browser.form['pass'] = PASSWORD  	
    r = browser.submit()
    f = open("login.html", "wb")
    f.write(r.read())
    f.close()
    browser.select_form(nr = 0)
    print("\033[1m\033[36m", end = "")
    print(47*'\033[1;35;40m-')
    sp("\033[1;37;1m[?] Enter the 2 factor code by google authenticator\n")
    print(47*'\033[1;37;1m-')
    apr = str(input('\033[1;37;1m[?] Enter Code : '))        
    try:
        browser.form['approvals_code'] = apr
    except mechanize._form_controls.ControlNotFoundError:
        print("Wrong password or some shit, check generated file")
        f = open("epage_" + str(USERNAME) + ".html", "wb")
        f.write(r.read())
        f.close()
        exit(1)
    r = browser.submit()
    browser.select_form(nr = 0)
    try:
        browser.form['name_action_selected'] = ['save_device']
    except mechanize._form_controls.ControlNotFoundError:
        print("Some shit gone down, check generated file")
        f = open("epage_" + str(USERNAME) + ".html", "wb")
        f.write(r.read())
        f.close()
        exit(1)
    r = browser.submit()
    f = open("full_login_" + str(USERNAME) + ".html", "wb")
    f.write(r.read())
    f.close()

    
def findtextchat(curl):
    r = browser.open(curl)
    x = browser.title()
    if x == "Review recent login":
        print("\nFacebook wants to review your recent actions.\nPlease fix that and then re run the program.")
        exit(1)
    if x == "Login approval needed":
        print("\nYour account is stuck on verification\nPlease do it and then re run the program.")
        exit(1)
    if x == "Epsilon":
        print("\nYour account got locked, recover it kindly and re run the script.")
        exit(1)

def sendtextconvo(comment):
    try:
        browser.select_form(nr = 1)
    except mechanize._mechanize.FormNotFoundError:
        print("Some error occured while finding text area, please check your account")
        exit(1)
    try:
        browser.form['body'] = comment
    except mechanize._form_controls.ControlNotFoundError:
        print("Some error occured while filling text, please check your account")
        exit(1)
    r = browser.submit()
    e = datetime.datetime.now()
    print("\033[1;32;40m", end = "")
    print (e.strftime("%d/%m/%Y   %I:%M:%S %p"))
    print(">>", line, "\n")

print("\033[1;33;40m", end = "")
os.system('clear')
print(logo)
sp("\033[1m\033[36m[+] Login With Email/Number \n")
print(47*'\033[1;35;40m-')
USERNAME = str(input('[?] Enter Email/Number : '))
print("\033[1;33;40m", end = "")
print(47*'\033[1;35;40m-')
sp("\033[1m\033[36m[+] Enter Your Facebook Password\n")
print(47*'\033[1;35;40m-')
PASSWORD = str(input('[?] Enter your password : '))
Login()
print("\033[1;33;40m", end="")
cid = str(input("➣Enter your convo or inbox I'd link: "))
curl = 'https://mbasic.facebook.com/messages/t/' + str(cid)
np1 = str(input("➣Enter Tatta Name: "))
np = str(input("➣Enter notepad file name: "))
t = int(input("➣Enter TIME: "))
print('\n')
print("\033[1;34;40m", end = "")
print(logo)
while True:
    try:
        f = open(np, 'r')
        lines = f.readlines()
        f.close()
        count = 0
        flag = False

        for i, line in enumerate(lines):
            if i < count:
                continue  # Skip lines that have already been sent
            if len(line) > 3:
                if count != 0:
                    sleep(t)
                findtextchat(curl)
                sendtextconvo(str(np1) + line)
                e = datetime.datetime.now()
                print("\033[1;32;40m", end="")
                print(" T4T4 CH0MD LINK  :--", cid)
                print(" 4CC0UNT N4M3 :--", USERNAME)
                print(e.strftime("--> Y0UR D4D M4FIY4 XD D0N T00L P00L H3R3 :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
                print("☛︎☛︎M4FIY4 XD H3R3 CH4L4 GY4 M3SS4G3 T3R4 :D ::-->> ", np1, line, "\n")
                count += 1
                if count % 10 == 0:
                    sleep(10)
            if i == len(lines) - 1:
                flag = True
        if flag:
            count = 0
            flag = False
    except Exception as e:
        d = datetime.datetime.now()
        print("\033[1;31;40m", end="")
        print(d.strftime("☛︎☛︎Y0UR D4D M4FIY4 XD C0NV0 KING H3R3 :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
        print("▶︎L4WRD3 N3T 0N K4R D3KH KY4 R4H4 H4I... V4RN4 T4T4 T3RI M4 CH0D  D3G4...", e, "\n")
        sleep(10)
        
