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
