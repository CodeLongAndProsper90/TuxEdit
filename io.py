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
