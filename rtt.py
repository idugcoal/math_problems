import math
import random
import jinja2
import os
import subprocess
from jinja2 import Template
import sys
sys.path.insert(0, 'triangles/')

# import get_tAB
# import get_tBC
# import get_tAC
import get_tAo1 
import get_tAo2
import get_tBo1
import get_tBo2
import get_tCo1
import get_tCo2

latex_jinja_env = jinja2.Environment(
  block_start_string = '\BLOCK{',
  block_end_string = '}',
  variable_start_string = '\VAR{',
  variable_end_string = '}',
  comment_start_string = '\#{',
  comment_end_string = '}',
  line_statement_prefix = '%%',
  line_comment_prefix = '%#',
  trim_blocks = True,
  autoescape = False,
  loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

t_x = latex_jinja_env.get_template('triangles/t_x.tex')
t_o1 = latex_jinja_env.get_template('triangles/t_o1.tex')
t_o2 = latex_jinja_env.get_template('triangles/t_o2.tex')

def get_tABx():
  h = random.randint(3, 8)
  w = random.randint(3, 8)
  return t_x.render(w=w, h=h, a=w, b=h, c='x', solve='x')
def get_tABo1(): 
  h = random.randint(3, 8)
  w = random.randint(3, 8)
  return t_o1.render(w=w, h=h, a=w, b=h, o1='$\\theta$', solve='$\\theta$')
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
  angle = random.randint(20, 45)
  h = w / math.tan(math.radians(angle))
  return t_o1.render(w=w, h=h, a=w, c='x', o1=angle, angle=angle)
def get_tAo1B():
  w = random.randint(5, 7)
  angle = random.randint(20, 45)
  h = w / math.tan(math.radians(angle))
  return t_o1.render(w=w, h=h, a=w, b='x', o1=angle, angle=angle)
def get_tAo1o2():
  return get_tAo1.get_o2()    ###
def get_tAo2x():
  w = random.randint(5, 7)
  angle = random.randint(20, 45)
  h = w / math.tan(math.radians(angle))
  return t_o2.render(w=w, h=h, a=w, c='x', o2=angle, angle=angle, solve='x')
def get_tAo2B():
  w = random.randint(5, 7)
  angle = random.randint(20, 45)
  h = w / math.tan(math.radians(angle))
  return t_o2.render(w=w, h=h, a=w, b='x', o2=angle, angle=angle, solve='x')
def get_tAo2o1():
  return get_tAo2.get_o1()    ###
def get_tBo1x():
  h = random.randint(5, 7)
  angle = random.randint(20, 45)
  w = h * math.tan(math.radians(angle))
  return t_o1.render(w=w, h=h, b=h, c='x', o1=angle, angle=angle, solve='x')
def get_tBo1A():
  h = random.randint(5, 7)
  angle = random.randint(20, 45)
  w = h * math.tan(math.radians(angle))
  return t_o1.render(w=w, h=h, b=h, a='x', o1=angle, angle=angle, solve='x')
def get_tBo1o2():
  return get_tBo1.get_o2()    ###
def get_tBo2x():
  h = random.randint(5, 7)
  angle = random.randint(20, 45)
  w = h / math.tan(math.radians(angle))
  return t_o2.render(w=w, h=h, b=h, c='x', o2=angle, angle=angle, solve='x')
def get_tBo2A():
  h = random.randint(5, 7)
  angle = random.randint(20, 45)
  w = h / math.tan(math.radians(angle))
  return t_o2.render(w=w, h=h, b=h, a='x', o2=angle, angle=angle, solve='x')
def get_tBo2o1():
  return get_tBo2.get_o1()    ###
def get_tCo1A():
  x = random.randint(5, 7)
  angle = random.randint(20, 45)
  w = x * math.sin(math.radians(angle))
  h = x * math.cos(math.radians(angle))
  return t_o1.render(w=w, h=h, a='x', c=x, o1=angle, angle=angle, solve='x')
def get_tCo1B():
  x = random.randint(5, 7)
  angle = random.randint(20, 45)
  w = x * math.sin(math.radians(angle))
  h = x * math.cos(math.radians(angle))
  return t_o1.render(w=w, h=h, b='x', c=x, o1=angle, angle=angle, solve='x')
def get_tCo1o2():
  return get_tCo1.get_o2()    ###
def get_tCo2A():
  x = random.randint(5, 7)
  angle = random.randint(20, 45)
  w = x * math.cos(math.radians(angle))
  h = x * math.sin(math.radians(angle))
  return t_o2.render(w=w, h=h, a='x', c=x, o2=angle, angle=angle, solve='x')
def get_tCo2B():
  x = random.randint(5, 7)
  angle = random.randint(20, 45)
  w = x * math.cos(math.radians(angle))
  h = x * math.sin(math.radians(angle))
  return t_o2.render(w=w, h=h, b='x', c=x, o2=angle, angle=angle, solve='x')
def get_tCo2o1():
  return get_tCo2.get_o1()





# def getL1():
#   in_file = 'rttL1.tex'
#   template = latex_jinja_env.get_template(in_file)
#   pwidth = random.randint(3, 8)
#   pheight = random.randint(3, 8)
#   angle =  math.degrees(math.atan(pheight / pwidth))
#   return template.render(pwidth=pwidth, pheight=pheight, angle=angle)

# def getL2():
#   in_file = 'rttL2.tex'
#   template = latex_jinja_env.get_template(in_file)
#   pwidth = random.randint(3, 8)
#   pheight = random.randint(3, 8)
#   angle =  math.degrees(math.atan(pheight / pwidth))
#   questions = ['How long is the ladder?', 
#               'How far away from the house is the bottom of the ladder?',
#               'How high above the ground does the ladder touch the house?']
#   answers = [
#     [],[],[]
#   ]
#   qrand = random.randint(0, len(questions) - 1)
  
#   return template.render(pwidth=pwidth, 
#                         pheight=pheight, 
#                         angle=angle, 
#                         question = questions[qrand])
