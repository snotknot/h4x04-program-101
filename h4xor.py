###
## IF YOU RUN THIS, MAKE SURE YOU RUN THE .py IN A CMD, NOT YOUR IDE. COLOR CODES AND OVERALL VISUALS MAY DIFFER WITH AN IDE
###

###
## A program I made to "mock", per se, "9 y/o's"
###

###
## idk why i made this send me help
###

from time import sleep
import time
import os

haxorMode = False

e1 = "                      :::!~!!!!!:."
e2 = "                  .xUHWH!! !!?M88WHX:."
e3 = "                .X*#M@$!!  !X!M$$$$$$WWx:."
e4 = "               :!!!!!!?H! :!$!$$$$$$$$$$8X:"
e5 = "              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:"
e6 = "             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!"
e7 = "             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!"
e8 = "               !:~~~ .:!M#$$$$WX??#MRRMMM!"
e9 = "               ~?WuxiW*`   `#$$$$8!!!!??!!!"
e10 = "             :X- M$$$$       `#$T~!8$WUXU~"
e11 = "            :%`  ~#$$$m:        ~!~ ?$$$$$$"
e12 = "          :!`.-   ~T$$$$8xx.  .xWW- ~##*"
e13 = ".....   -~~:<` !    ~?T#$$@@W@*?$$      /`"
e14 = "W$@@M!!! .!~~ !!     .:XUW$W!~ `~:    :"
e15 = "#~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`"
e16 = ":::~:!!`:X~ .: ?H.!u $$$B$$$!W:U!T$$M~"
e17 = ".~~   :X@!.-~   ?@WTWo(*$$$W$TH$! `"
e18 = "Wi.~!X$?!-~    : ?$$$B$Wu(**$RM!"
e19 = "$R@i.~~ !     :   ~$$$$$B$$en:``"
e20 = "?MXT@Wx.~    :     ~##*$$$$M~"

s1 = "| |              | |            "
s2 = "| |__   __ _  ___| | _____ _ __ "
s3 = "| '_ \ / _` |/ __| |/ / _ \ '__|"
s4 = "| | | | (_| | (__|   <  __/ |   "
s5 = "|_| |_|\__,_|\___|_|\_\___|_|       "    

r1 = "   _                   _"
r2 = " _( )                 ( )_"
r3 = "(_, |      __ __      | ,_)"
r4 = "   \.'\    /  ^  \    /'/"
r5 = "    '\.'\,/\      \,/'/'"
r6 = "      '\| []   [] |/'"
r7 = "        (_  /^\  _)"
r8 = "          \  ~  /"
r9 = "          /HHHHH\."
r10 = "        /'/{^^^}\."
r11 = "    _,/'/'  ^^^  '\.'\,_"
r12 = "   (_, |           | ,_)"
r13 = "     (_)           (_)"


haxArt = [s1, s2, s3, s4, s5]

skull = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20]

skull2 = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13]

inputs = ["Y", "N", "y", "n"]

def matrix101(num):
    n = num
    while n > 0: 
        n -= 1
        print(n)
    print("psycho is 4 ft tall")

def loadArt():
    haxorMode = True
    while haxorMode == True:
        print(*haxArt,sep='\n')
        time.sleep(0.1)
        print(*skull,sep='\n')
        time.sleep(0.1)
        print(*skull2,sep='\n')
        time.sleep(0.1)
        print(*haxArt,sep='\n')
        time.sleep(0.1)
        print(*skull,sep='\n')
        time.sleep(0.1)
        print(*skull2,sep='\n')
        time.sleep(0.1)
        print(*haxArt,sep='\n')
        time.sleep(0.1)
        print(*skull,sep='\n')
        time.sleep(0.1)
        print(*skull2,sep='\n')
        time.sleep(0.1)
        break
    
    matrix101(10000)
 
def loadTask(loadingTask):
    print(loadingTask) ; sleep(0.5) ; print(".") ; sleep(0.5) ; print("."*2) ; sleep(0.5) ; print("."*3)

def onOff():
    os.system('color 0a')
    answer = input("Enable haxer mode? [Y/N]: ")
    usrInput = answer[0]
    
    if usrInput == inputs[0] or usrInput == inputs[2]:
        loadArt()
                # print(*skull,sep='\n')
    if usrInput == inputs[1] or usrInput == inputs[3]:
        loadTask("Exiting")
        quit()
    if usrInput not in inputs:
        print("'" + answer + "'" + " is not a valid answer.")
        
    input()

onOff()
