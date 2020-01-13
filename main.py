#############################################################
# Start Icon made by Freepik from www.flaticon.com
# Copyright 2020 Scott Little
# By the way, the "Real programmers use Emacs" in the about box is just a clue to the easter egg. I use Vim, and this app was made in Vim                                                               Line: (266)
# assets/dump.wav made by MIke Koenig, Creative Commons Attribution 3.0
##############################################################


from tkinter import *
import os.path as usr
from os import system
from tkinter import filedialog
from tkinter.messagebox import showinfo
from playsound import playsound as play
import sys, os
import io
from cpy import *
filename =None
t = None
cmd = None
saved = False
version = '0.1.0A'
buff = ''
###############################################
#
# These functions are I/O related
#
##############################################
def write(filename, sound=True):
  global text 
  with open(filename, "w+") as f:
    f.write(text.get('1.0', END))
    if sound:
      play("assets/save.wav")


def load(filename):
  with open(filename, 'r') as f:
    text.insert(END, f.read())


def saveas(sound=True, *args):
  global test
  global filename
  global saved
  if filename == None:
    filename=filedialog.asksaveasfilename() 

  if filename == '' or ():
    pass
  t = text.get("1.0", "end-1c")
  if not t.endswith('\n'):
    t = t + '\n'
  if type(t) is '' or type(t) is  ():
      pass
  write(filename, sound)
  saved = True


def openfile(*args):
  global text
  global filename
  global root
  filename =  filedialog.askopenfilename(initialdir = usr.expanduser("~/documents"),title = "Select file")
  try:
    load(filename)
  except TypeError:
    pass 
  if filename == '':
    root.title("Ready to edit...")
  elif type(filename) is str:
    filenameClean = filename.split('/')
    root.title(filenameClean[-1])


def editnew(*args):
  global filename
  global text
  saveas(sound=False)
  text.delete('1.0', END)
  filename = None


############################
#
# End I/O
#
###########################3

def error(msg):
  play('assets/error.wav')
  showinfo("Error", msg)




def save_state(b):
  assert type(b) is bool
  global saved
  saved = b 


def kill(Toplevel):
    Toplevel.destroy()





def runprog(*args):
  while filename == None:
    openfile()
  
  if cmd == None:
    error("Run is not configured")
  saveas(sound=False)
  f1 = filename.split('.')
  system("xterm -hold -e '{} {} && bash'".format(cmd, filename))


def runcmd(*args):
  def process(*args):
    cmd = In.get()
    cmd1=cmd
    cmd = cmd.split(' ')
    if cmd[0] == 'butterflies':
      play('assets/emacs.wav')
      showinfo("ERROR", "This isn't Emacs...")
    elif cmd[0] == 'play':
      sounds = ['error.wav', 'save.wav', 'emacs.wav']
      if cmd[1] in sounds:
        play('assets/' + cmd[1])
    elif cmd[0] == 'dump':
      uav = ['filename', 'cmd', 'buff']
      if cmd[1] in uav:
        play('assets/dump.wav')
        showinfo("Dump", eval(cmd[1]))
      else:
        error('Not a valid variable')
    else:
      play('assets/error.wav')
      showinfo("ERROR", "Not a valid command")
  popup = Toplevel()
  popup.wm_title("Commander")
  ee = Label(popup,text="FYI: This is an Easter Egg. (Think XKCD...)")
  ee.pack()
  In = Entry(popup)
  In.pack()
  button = Button(popup, text="Evaluate Command", command=process)
  button.pack()
  popup.bind("<Return>", process)


def aboutbox():
  showinfo('About','This is TuxEdit.\nMade by a programmer (Duh!), for Programmers\nVersion: {}\n(By the way, REAL programmers use emacs...)'.format(version))


def runconfig():
  def setcmd():
    global cmd
    command = enter.get()
    cmd = command 
    del command
    kill(popup)
  popup = Toplevel()
  lbl = Label(popup, text="What is the command to run your program? (*.py: python3)")
  enter = Entry(popup)
  button = Button(popup, text="Set command", command=setcmd)
  lbl.pack()
  enter.pack()
  button.pack()

#################################################
#
# These are the text editing related functions
#
################################################

def select_all(event=None):
  global text  
  text.tag_add('sel', '1.0', 'end')
  return "break"

def yank(w):
  global text
  global buff
  try:
    buff =  text.get(SEL_FIRST, SEL_LAST)
  except TclError:
    None
  return "break"


def smash(w):
  global text
  global buff
  text.insert(CURRENT,buff)
  return "break"


def rip(w):
  global text
  global buff
  start = SEL_FIRST
  end = SEL_LAST
  try:
    buff = text.get(start, end)
    text.delete(start, end)
  except TclError:
    None
  return "break"

########################################
#
# End edit functions
#
#######################################
root = Tk()

# Set the app icon
program_directory=sys.path[0]
root.iconphoto(True, PhotoImage(file=os.path.join(program_directory, "icon.gif")))

# Make the root menu
menu = Menu(root)

#Make the menu related to files
filemenu = Menu(menu, tearoff=0)

#And add three commands:
filemenu.add_command(label='Open', command=openfile) #Open a new file
filemenu.add_command(label="Save", command=saveas) # Save the current file
filemenu.add_command(label="New", command=editnew) # Edit a new file

runmenu = Menu(menu, tearoff=0) # Make the menu related to execution

runmenu.add_command(label="Run", command=runprog) # Run the program
runmenu.add_command(label="Configure", command=runconfig) # Configure the run command

helpmenu = Menu(menu, tearoff=0) # Add a help menu

helpmenu.add_command(label="About", command=aboutbox) # Add a about box
helpmenu.add_command(label="I can't find it!", command=lambda: showinfo("HINT", "Look in the source..."))
#Display the menus
menu.add_cascade(label="File", menu=filemenu)

menu.add_cascade(label="Run", menu=runmenu)

menu.add_cascade(label="Help", menu=helpmenu)

text=Text(root) #Make the main text entry box
S = Scrollbar(root) # And add a scrollbar

S.pack(side=RIGHT, fill=Y) # Display them
text.pack(expand=True, fill=BOTH)

S.config(command=text.yview) # Link the scrollbar to the text

root.bind("<Control-o>", openfile) # Bind Ctrl-O to open a file
root.bind("<Control-s>", saveas) # and Ctrl-s to save
root.bind("<Control-n>", editnew)  #Plus, Ctrl-n to make a new one

root.bind("<Control-a>", select_all) # Select all
root.bind("<Control-A>", select_all)

root.bind("<Control-x><Alt-c>", runcmd) #We can't tell you what this does...
root.bind("<F5>",runprog) # run the program

root.bind("<Control-c>", yank) #Copy
root.bind("<Control-x>", rip) # Paste
#NOTE: Ctrl-V is made by default

root.config(menu=menu)
root.title("TuxEditor") #Set the title

root.geometry("500x400")

root.mainloop() # Start


