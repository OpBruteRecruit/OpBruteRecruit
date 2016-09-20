from Tkinter import *
root = Tk()
root.title("opbruterecruit BETA (V=1.1)")
app = Frame(root)
app.grid


GIT = "git clone "
LINK = "https://github.com/OpBruteRecruit/OpBruteRecruit.git"
DEFAULT = "python "
NEW = "cd ~"
print"[-] Do not close this terminal, or the programm will crash"

label1 = Label(root,text = "welcome to #opbruterecruit")
label1.grid(row = 1, column = 1, sticky = W)

empty1 = Label(root,text = " ")
empty1.grid(row = 2, column = 1, sticky = W)

label2= Label(root,text = "FOR UPDATES GO TO DEFAULT -> UPDATE: ")
label2.grid(row = 3, column = 1, sticky = W)

output1 = Text(root,width = 47, height = 1,wrap = NONE)
output1.grid(row = 4, column = 0, columnspan = 15, sticky = W)
output1.insert(0.0,GIT + LINK)

empty2 = Label(root,text = " ")
empty2.grid(row = 5, column = 1, sticky = W)

label3 = Label(root,text = "before every new app command copy & paste:")
label3.grid(row = 6, column = 1, sticky = W)

output2 = Text(root,width = 47, height = 1,wrap = NONE)
output2.grid(row = 7, column = 0, columnspan = 15, sticky = W)
output2.insert(0.0,NEW)

empty2 = Label(root,text = " ")
empty2.grid(row = 8, column = 1, sticky = W)

label3 = Label(root,text = "copy & paste to new terminal")
label3.grid(row = 9, column = 1, sticky = W)

output3 = Text(root,width = 47, height = 1,wrap = NONE)
output3.grid(row = 10, column = 0, columnspan = 15, sticky = W)

empty3 = Label(root,text = " ")
empty3.grid(row = 11, column = 1, sticky = W)


def EXIT():
 print"[-] killing main proccess"
 print"[-] quiting main programm"
 quit()


quitbutton = Button(root, text = "EXIT",command=EXIT)
quitbutton.grid(row =  12,column = 1)


def CAT():
 print"[-] Generating cat.py route"
 print"[-] NOTE: all files must be in  right directory"
 print"[-] for more help go to HELP -> APPS"
 ROUTEcat = (DEFAULT) + "/root/OpBruteRecruit/cat.py"
 output3.delete(0.0,END)
 output3.insert(0.0,ROUTEcat)

def CRUNCHnonselectivenongeneratic():
 print"[-] Generating crunchnonselnongen.py route"
 print"[-] NOTE: all files must be in  right directory"
 print"[-] for more help go to HELP -> APPS"
 ROUTEcrunchnonselectivenongeneratic = (DEFAULT) + "/root/OpBruteRecruit/crunchnonselectivenongeneratic.py"
 output3.delete(0.0,END)
 output3.insert(0.0,ROUTEcrunchnonselectivenongeneratic)


def CRUNCHnonselectivegeneratic():
 print"[-] Generating crunchnonselgen.py route"
 print"[-] NOTE: all files must be in  right directory"
 print"[-] for more help go to HELP -> APPS"
 ROUTEcrunchnonselectivegeneratic = (DEFAULT) + "/root/OpBruteRecruit/crunchnonselectivegeneratic.py"
 output3.delete(0.0,END)
 output3.insert(0.0,ROUTEcrunchnonselectivegeneratic)


def CRUNCHselectivenongeneratic():
 print"[-] Generating crunchselnongen.py route"
 print"[-] NOTE: all files must be in  right directory"
 print"[-] for more help go to HELP -> APPS"
 ROUTEcrunchselectivenongeneratic = (DEFAULT) + "/root/OpBruteRecruit/crunchselectivenongeneratic.py"
 output3.delete(0.0,END)
 output3.insert(0.0,ROUTEcrunchselectivenongeneratic)

def CRUNCHselectivegeneratic():
 print"[-] Generating crunchnonselgen.py route"
 print"[-] NOTE: all files must be in  right directory"
 print"[-] for more help go to HELP -> APPS"
 ROUTEcrunchselectivegeneratic = (DEFAULT) + "/root/OpBruteRecruit/crunchselectivegeneratic.py"
 output3.delete(0.0,END)
 output3.insert(0.0,ROUTEcrunchselectivegeneratic)

def SpartaBF():
 print"[-] Generating sparta.py route"
 print"[-] NOTE: this is a thirt party product"
 SPartaBF = "sparta"
 output3.delete(0.0,END)
 output3.insert(0.0,SPartaBF)

def TorsHelper():
 print"[-] Generating torshelper.py route"
 print"[-] NOTE: all files must be in  right directory"
 Torshelper = (DEFAULT) + "/root/OpBruteRecruit/torshelper.py"
 output3.delete(0.0,END)
 output3.insert(0.0,Torshelper)

def TorsHammer():
 print"[-] Generating torshammer.py route"
 print"[-] NOTE: this is a thirt party product"
 print"[-] NOTE: torshelper is adviced for un expirienced users"
 print"[-] NOTE: all files must be in  right directory"
 Torshammer = (DEFAULT) + "/root/OpBruteRecruit/torshammer.py"
 output3.delete(0.0,END)
 output3.insert(0.0,Torshammer)

def KALIdefaults():
 rootkali = Tk()
 rootkali.title("Kali/defaults")
 appkali = Frame(rootkali)
 appkali.grid

 print"[-] starting kali/defaults"

 labelkali1 = Label(rootkali,text = "default usrname & passwords\n \nusername: root\n \npassword: toor")
 labelkali1.grid(row = 1, column = 1, sticky = W)
 
 rootkali.mainloop()

def UPDATE():
 rootupdate= Tk()
 rootupdate.title("Kali/update")
 appupdate = Frame(rootupdate)
 appupdate.grid

 print"[-] starting kali/update"

 labelkali1 = Label(rootupdate,text = "to update follow stepss:\n \n1. COPY the update link at start screen of the main menu\n \n2.open folders move the folder OpBruteRecruit to Desktop\n \n3. PASTE update link into terminal & press ENTER\n \nsystem update:\n \ntype into terminal:\n \napt-get update && apt-get upgrade")
 labelkali1.grid(row = 1, column = 1, sticky = W)
 
 rootupdate.mainloop()
'''
helpmenu commands
'''

def HELPterminal():
 roothelpterminal = Tk()
 roothelpterminal.title("HELP/terminal")
 apphelpterminal = Frame(roothelpterminal)
 apphelpterminal.grid

 print"[-] starting HELP/terminal"

 labelhelpterminal1 = Label(roothelpterminal,text = "for new terminal press:\n \nRIGHT mouse -> Open Terminal")
 labelhelpterminal1.grid(row = 1, column = 1, sticky = W)
 
 apphelpterminal.mainloop()
 
def HELPcopypaste():
 roothelpcopypaste = Tk()
 roothelpcopypaste.title("HELP/Copy & Paste")

 apphelpcopypaste = Frame(roothelpcopypaste)
 apphelpcopypaste.grid

 print"[-] starting HELP/copy&paste"

 labelhelpcopypaste1 = Label(roothelpcopypaste,text = "to copy & paste go's a bit difrent than usual\nto copy you have to make the whole line light grey and then use:\n \n CNTRL + C\n \n to paste you have to press:\n \n RIGHT MOUSE -> PASTE\n \n Note: this is ONLY the way for the #opbruterecruit programs")
 labelhelpcopypaste1.grid(row = 1, column = 1, sticky = W)
 
 roothelpcopypaste.mainloop()  


def crunchsmall():
 print"[-] for help go to help-> crunch "

def HELPcrunch():
 roothelpcrunch = Tk()
 roothelpcrunch.title("HELP/crunch")

 apphelpcrunch = Frame(roothelpcrunch)
 apphelpcrunch.grid

 print"[-] starting HELP/copy&paste"

 labelhelpcrunch1 = Label(roothelpcrunch,text = "DIFRENCE:\nselective mode{SEL.} \nthis means that you can select some aspects of youre wordlist\nfor example if: \nminimal input = 6 && maximal input = 6\ncaracters = 0123456789 \nand selective mode = 16@@@@\nthe output would be every number from 160000 thill 169999\nwith this way you can create almost every selective wordlist\nevery @ = every chngeble caracter that will be changed by every\nkind of number or letter or symbol you set inside caracters\nthe other caracters than @ won't be changed\n \nthe generatic mode {GEN.}\n this is just if it will be safed inside a file or not if non generatic it wil be\n safed inside a file if generatic it will be displayed\n \n \nWHAT TO DO WITH CRUNCH\n \nyou may ask yourself:\nwhat does crunch?, well crunch generates wordlists \nwordlists are used for Brute force attacks, that means all the possible passwords will be tryed out on a device or site, use sparta as a easy use for HYDRA, with is used for brute force attacks.... suc6 ;) ")
 labelhelpcrunch1.grid(row = 1, column = 0, sticky = W)
 
 roothelpcrunch.mainloop()



mainmenu = Menu(root)
root.config(menu=mainmenu)

submenu = Menu(mainmenu)
defaultsmenu = Menu(mainmenu)
helpmenu = Menu(mainmenu)

mainmenu.add_cascade(label="apps",menu = submenu)
mainmenu.add_cascade(label="defaults",menu = defaultsmenu)
mainmenu.add_cascade(label="help",menu = helpmenu)

submenu.add_command(label = "cat (create files)",command=CAT)

submenu.add_separator()

submenu.add_command(label = "Crunch(non sel. non gen.)",command=CRUNCHnonselectivenongeneratic)
submenu.add_command(label = "Crunch(non sel. gen.)",command=CRUNCHnonselectivegeneratic)
submenu.add_command(label = "Crunch(sel. non gen.)",command=CRUNCHselectivenongeneratic)
submenu.add_command(label = "Crunch(sel. gen.)",command=CRUNCHselectivegeneratic)
submenu.add_command(label = "help=HELP->crunch",command=crunchsmall)
submenu.add_separator()

submenu.add_command(label = "SPARTA brute force 3ps",command=SpartaBF)

submenu.add_separator()

submenu.add_command(label = "Torshelper: easy tool for Torshammer",command=TorsHelper)
submenu.add_command(label = "Torshammer: DDOS ATTACKS 3ps)",command=TorsHammer)


defaultsmenu.add_command(label = "kali linux",command=KALIdefaults)
defaultsmenu.add_command(label = "update",command=UPDATE)

helpmenu.add_command(label = "terminal",command=HELPterminal)
helpmenu.add_command(label = "Copy & Paste",command=HELPcopypaste)
helpmenu.add_command(label = "crunch",command=HELPcrunch)




root.mainloop()
