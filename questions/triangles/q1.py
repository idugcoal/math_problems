import math
import random
import subprocess
import sys
from config import latex_jinja_env
from config import formulas_a

t_x = latex_jinja_env.get_template('templates/triangles/t_x.tex')
t_o1 = latex_jinja_env.get_template('templates/triangles/t_o1.tex')
t_o2 = latex_jinja_env.get_template('templates/triangles/t_o2.tex')
t_o1o2 = latex_jinja_env.get_template('templates/triangles/t_o1o2.tex')

def get_a(b=None, c=None, o1=None, o2=None):
  if b is not None and c is not None:
    return math.sqrt((math.pow(c, 2) - math.pow(b, 2)))
def get_b(a=None, c=None, o1=None, o2=None):
  if a is not None and c is not None:
    return math.sqrt((math.pow(c, 2) - math.pow(a, 2)))
def get_c(a=None, b=None, o1=None, o2=None):
  if a is not None and b is not None:
    return math.pow(a, 2) + math.pow(b, 2)
def get_o1(a=None, b=None, c=None, o2=None):
  if o2 is not None:
    return 90 - o2
def get_o2(a=None, b=None, c=None, o1=None):
  if o1 is not None:
    return 90 - o2

def get_answers(a=None, b=None, c=None, o1=None, o2=None):
  if o1 is None:
    o1 = get_o1(a=None, b=None, c=None, o2=None)
  if o2 is None:
    o2 = get_o2(a=None, b=None, c=None, o1=None)
  if a is None:
    a = get_a(b=None, c=None, o1=None, o2=None)
  if b is None:
    b = get_b(a=None, c=None, o1=None, o2=None)
  if c is None:
    c = get_c(a=None, b=None, o1=None, o2=None)

  return {
    'a': a,
    'b': b,
    'c': c,
    'o1': o1,
    'o2': o2
  }

def get_options(formulas, list, a=1, b=1, c=1, o1=1, o2=1):
  options = []
  for formula in list:
    # print('formula', formulas_a[formula], a, b, c)
    options.append(
      round(eval(formulas_a[formula], {'a':a, 'b':b, 'c':c, 'o1':o1, 'o2':o2 }, {'math': math}), 2)
    )
  print(options)
  return options

def get_tABx():
  h = random.randint(3, 8)
  w = random.randint(3, 8)
  answers = get_options(formulas=formulas_a, list=[73,78,79,81], a=w, b=h)
  answer = answers[0]
  print('answer', answer)
  return {
    'q': t_x.render(w=w, h=h, a=w, b=h, c='x', solve='x', answers=answers),
    'a': answer
  }
def get_tABo1(): 
  h = random.randint(3, 8)
  w = random.randint(3, 8)
  o1=2
  answers = get_options(formulas=formulas_a, list=[43,45,9,27], a=w, o1=o1)
  answer = answers[0]
  return {
    'q': t_o1.render(w=w, h=h, a=w, b=h, o1='$\\theta$', solve='$\\theta$', answers=answers),
    'a': answer
  }
def get_tABo2():
  h = random.randint(3, 8)
  w = random.randint(3, 8) 
  return t_o2.render(w=w, h=h, a=w, b=h, o2='$\\theta$', solve='$\\theta$')
def get_tBCx():
  h = random.randint(3, 5)
  c = random.randint(6, 8)
  w = math.sqrt(math.pow(c, 2) - math.pow(h, 2))
  return t_x.render(w=w, h=h, a='x', b=h, c=c, solve='x')
def get_tBCo1():
  h = random.randint(3, 5)
  c = random.randint(6, 8)
  w = math.sqrt(math.pow(c, 2) - math.pow(h, 2))
  return t_o1.render(w=w, h=h, b=h, c=c, o1='$\\theta$', solve='$\\theta$')
def get_tBCo2():
  h = random.randint(3, 5)
  c = random.randint(6, 8)
  w = math.sqrt(math.pow(c, 2) - math.pow(h, 2))
  return t_o2.render(w=w, h=h, b=h, c=c, o2='$\\theta$', solve='$\\theta$')
def get_tACx():
  w = random.randint(3, 5)
  x = random.randint(6, 8)
  h = math.sqrt(math.pow(x, 2) - math.pow(w, 2))
  return t_x.render(w=w, h=h, a=w, b='x', c=x, solve='x')
def get_tACo1():
  w = random.randint(3, 5)
  x = random.randint(6, 8)
  h = math.sqrt(math.pow(x, 2) - math.pow(w, 2))
  return t_o1.render(w=w, h=h, a=w, c=x, o1='$\\theta$', solve='$\\theta$')
def get_tACo2():
  w = random.randint(3, 5)
  x = random.randint(6, 8)
  h = math.sqrt(math.pow(x, 2) - math.pow(w, 2))
  return t_o2.render(w=w, h=h, a=w, c=x, o2='$\\theta$', solve='$\\theta$')
def get_tAo1x(): 
  w = random.randint(5, 7)
  o1 = random.randint(20, 45)
  h = w / math.tan(math.radians(o1))
  return t_o1.render(w=w, h=h, a=w, c='x', o1=o1, solve='x')
def get_tAo1B():
  w = random.randint(5, 7)
  o1 = random.randint(20, 45)
  h = w / math.tan(math.radians(o1))
  return t_o1.render(w=w, h=h, a=w, b='x', o1=o1, solve='x')
def get_tAo1o2():
  w = random.randint(5, 7)
  o1 = random.randint(20, 45)
  h = w / math.tan(math.radians(o1))
  return t_o1o2.render(w=w, h=h, a=w, o1=o1, o2='$\\theta$', solve='$\\theta$')
def get_tAo2x():
  w = random.randint(5, 7)
  o2 = random.randint(20, 45)
  h = w / math.tan(math.radians(o2))
  return t_o2.render(w=w, h=h, a=w, c='x', o2=o2, solve='x')
def get_tAo2B():
  w = random.randint(5, 7)
  o2 = random.randint(20, 45)
  h = w / math.tan(math.radians(o2))
  return t_o2.render(w=w, h=h, a=w, b='x', o2=o2, solve='x')
def get_tAo2o1():
  w = random.randint(5, 7)
  o2 = random.randint(20, 45)
  h = w / math.tan(math.radians(o2))
  return t_o1o2.render(w=w, h=h, a=w, o1='$\\theta$', o2=o2, solve='$\\theta$')
def get_tBo1x():
  h = random.randint(5, 7)
  o1 = random.randint(20, 45)
  w = h * math.tan(math.radians(o1))
  return t_o1.render(w=w, h=h, b=h, c='x', o1=o1, solve='x')
def get_tBo1A():
  h = random.randint(5, 7)
  o1 = random.randint(20, 45)
  w = h * math.tan(math.radians(o1))
  return t_o1.render(w=w, h=h, b=h, a='x', o1=o1, solve='x')
def get_tBo1o2():
  h = random.randint(5, 7)
  o1 = random.randint(20, 45)
  w = h * math.tan(math.radians(o1))
  return t_o1o2.render(w=w, h=h, b=h, o1=o1, o2='$\\theta$', solve='$\\theta$')
def get_tBo2x():
  h = random.randint(5, 7)
  o2 = random.randint(20, 45)
  w = h / math.tan(math.radians(o2))
  return t_o2.render(w=w, h=h, b=h, c='x', o2=o2, solve='x')
def get_tBo2A():
  h = random.randint(5, 7)
  o2 = random.randint(20, 45)
  w = h / math.tan(math.radians(o2))
  return t_o2.render(w=w, h=h, b=h, a='x', o2=o2, solve='x')
def get_tBo2o1():
  h = random.randint(5, 7)
  o2 = random.randint(20, 45)
  w = h / math.tan(math.radians(o2))
  return t_o1o2.render(w=w, h=h, b=h, o1='$\\theta$', o2=o2, solve='$\\theta$')
def get_tCo1A():
  x = random.randint(5, 7)
  o1 = random.randint(20, 45)
  w = x * math.sin(math.radians(o1))
  h = x * math.cos(math.radians(o1))
  return t_o1.render(w=w, h=h, a='x', c=x, o1=o1, solve='x')
def get_tCo1B():
  x = random.randint(5, 7)
  o1 = random.randint(20, 45)
  w = x * math.sin(math.radians(o1))
  h = x * math.cos(math.radians(o1))
  return t_o1.render(w=w, h=h, b='x', c=x, o1=o1, solve='x')
def get_tCo1o2():
  x = random.randint(5, 7)
  o1 = random.randint(20, 45)
  w = x * math.sin(math.radians(o1))
  h = x * math.cos(math.radians(o1))
  return t_o1o2.render(w=w, h=h, c=x, o1=o1, o2='$\\theta$', solve='$\\theta$')
def get_tCo2A():
  x = random.randint(5, 7)
  o2 = random.randint(20, 45)
  w = x * math.cos(math.radians(o2))
  h = x * math.sin(math.radians(o2))
  return t_o2.render(w=w, h=h, a='x', c=x, o2=o2, solve='x')
def get_tCo2B():
  x = random.randint(5, 7)
  o2 = random.randint(20, 45)
  w = x * math.cos(math.radians(o2))
  h = x * math.sin(math.radians(o2))
  return t_o2.render(w=w, h=h, b='x', c=x, o2=o2, solve='x')
def get_tCo2o1():
  x = random.randint(5, 7)
  o2 = random.randint(20, 45)
  w = x * math.cos(math.radians(o2))
  h = x * math.sin(math.radians(o2))
  return t_o1o2.render(w=w, h=h, c=x, o1='$\\theta$', o2=o2, solve='$\\theta$')