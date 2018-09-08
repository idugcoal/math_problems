import math
import random
import jinja2
import os
import subprocess
from jinja2 import Template
import sys

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

t_x = latex_jinja_env.get_template('templates/triangles/t_x.tex')
t_o1 = latex_jinja_env.get_template('templates/triangles/t_o1.tex')
t_o2 = latex_jinja_env.get_template('templates/triangles/t_o2.tex')
t_o1o2 = latex_jinja_env.get_template('templates/triangles/t_o1o2.tex')
r_db = latex_jinja_env.get_template('templates/rectangles/r_db.tex')
g_b = latex_jinja_env.get_template('templates/graphs/blank.tex')
t_b = latex_jinja_env.get_template('templates/tables/blank.tex')

def get_tb():
  return t_b.render(i1=1,i2=2,i3=3,i4=4,i5=5,i6=6,o1=-2,o2=0,o3=4,o4=10,o5=18,o6=28)
def get_gb():
  return g_b.render(n=-5, d=3)
def get_rdb():
  answers = {1: 67, 2: 68, 3: 69, 4: 70}
  return r_db.render(w=8.6, h=5.2, t=3, answers=answers)
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
