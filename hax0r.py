import time
loginCorrect = True
cursor = "> "

#What happens when user runs hack.exe
def hackexe():
    print "USERS ONLINE: xXPutinXx, Drumpf, Hillory_Clitorus, Alley Jhones"
    hack = raw_input(cursor)
    if hack == "hack xXPutinXx" or hack == "hack xxputinxx":
        print "RUSSIA TRACKING DEVICE ACTIVATED"
        time.sleep(1)
        print "IP FOUND. PREPARE TO BE SMITED NERD"
        quit()

    if hack == "hack Drumpf" or hack == "hack drumpf":
        print "Hello Mr President you have 1 new email"
        time.sleep(.5)
        print "FROM xXPutinXx"
        time.sleep(.5)
        print """Money should be deposited into your account tommorrow. Thanks for helping me with the election. Much harder than manipulating your
 election."""
        quit()

    if hack == "hack Hillory_Clitorus" or hack == "hack hillory_clitorus":
        print "You have 1 new email"
        time.sleep(.5)
        print "FROM Mr Clinton"
        time.sleep(.5)
        print "lol u cuck im having sex with monica again tonight"
        quit()

    if hack == "hack Alley Jhones" or hack == "hack alley jhones":
        print "BOOTING GOVERNMENT TRUTHER OS"
        time.sleep(1)
        print "MESSAGE OF THE DAY:"
        time.sleep(1)
        print """REMEMBER, THE PYRAMIDS WERE CREATED BY HILLARY CLINTON, OBAMA IS A DEMON, WILL SMITH IS
PART OF A SPECIES OF GENETICALLY ENGINEERED ALIENS AND TRUMP IS JESUS RESURRECTED"""
        time.sleep(1)
        print "You have 1 new email"
        time.sleep(1)
        print "FROM Drumpf"
        time.sleep(1)
        print """Thank you Alex for helping me secure my spot in the US Government. In return, I will help
your show prove the hard truths of the world out there, and you get to be my right hand man in
heaven."""
        quit()

#When user logins successfully
def hacking():
    programCorrect = True
    print "\n"
    print "WELCOME MASTER HAX0R ANONYMOOSE"
    time.sleep(.5)
    print "We do not forgive, we do not forget. Expectro patronum."
    while programCorrect == True:
        program = raw_input("anonym00se@GoogleServer: ")
        if program == "hack.exe":
            programCorrect = False
            hackexe()
        else:
            print "PROGRAM NOT FOUND"                               

print "BOOTING KALI GANUU/LINOOX"
time.sleep(1)
while loginCorrect == True:
    username = raw_input("LOGIN: ")
    if username == "Anonym00se":
        loginCorrect = False
        hacking()
    else:
        print "USER NOT FOUND"


