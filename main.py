#############################################################
# Icon made by Freepik from www.flaticon.com
# Copyright 2020 Scott Little
# By the way, the "Real programmers use Emcas" in the about box is just a clue to the easter egg. I use Vim, and this app was made in Vim
############################################################


from tkinter import *
import os.path as usr
from os import system
from tkinter import filedialog
from tkinter.messagebox import showinfo
from playsound import playsound as play
from gtts import gTTS
import sys, os
filename =None
t = None
cmd = None
saved = False
def select_all(event=None):
  global text  
  text.tag_add('sel', '1.0', 'end')
  return "break"
def save_state(b):
  assert type(b) is bool
  global saved
  saved = b 
def kill(Toplevel):
    Toplevel.destroy()
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
def runprog(*args):
  while filename == None:
    openfile()
  
  #while cmd == None:
   # runconfig()
  saveas(sound=False)
  f1 = filename.split('.')
  system("xterm -hold -e '{} {} && bash'".format(cmd, filename))
def runcmd(*args):
  def process():
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
    else:
      play('assets/error.wav')
      showinfo("ERROR", "Not a valid command")
  popup = Toplevel()
  popup.wm_title("Commands")
  ee = Label(popup,text="FYI: This is an Easter Egg. (Think XKCD...)")
  ee.pack()
  In = Entry(popup)
  In.pack()
  button = Button(popup, text="Evaluate Command", command=process)
  button.pack()
def aboutbox():
  showinfo('About','This is editor.\nThe only editor you\'ll need.\n\n(By the way, REAL programmers use emacs...)')
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
root = Tk()
program_directory=sys.path[0]
root.iconphoto(True, PhotoImage(file=os.path.join(program_directory, "icon.gif")))
menu = Menu(root)
filemenu = Menu(menu, tearoff=0)
filemenu.add_command(label='Open', command=openfile)
filemenu.add_command(label="Save", command=saveas)
filemenu.add_command(label="New", command=editnew)
runmenu = Menu(menu, tearoff=0)
runmenu.add_command(label="Run", command=runprog)
runmenu.add_command(label="Configure", command=runconfig)
helpmenu = Menu(menu, tearoff=0)
helpmenu.add_command(label="About", command=aboutbox)

menu.add_cascade(label="File", menu=filemenu)
menu.add_cascade(label="Run", menu=runmenu)
menu.add_cascade(label="Help", menu=helpmenu)

text=Text(root) #Make the main text entry box
S = Scrollbar(root)
S.pack(side=RIGHT, fill=Y)
text.pack(expand=True, fill=BOTH)
S.config(command=text.yview)

root.bind("<Control-o>", openfile) # Bind Ctrl-O to open a file
root.bind("<Control-s>", saveas) # and Ctrl-s to save
root.bind("<Control-n>", editnew)  #Plus, Ctrl-n to make a new one
root.bind("<Control-a>", select_all)
root.bind("<Control-A>", select_all)
root.bind("<Control-x><Alt-c>", runcmd) 
root.bind("<F5>",runprog)
root.config(menu=menu)
root.title("Editor")
root.geometry("500x400")
root.mainloop()



