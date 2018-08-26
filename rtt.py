import math
import random
import jinja2
import os
import subprocess
from jinja2 import Template
import sys
sys.path.insert(0, 'triangles/')

import get_tAB
import get_tBC
import get_tAC
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

def getL1():
  in_file = 'rttL1.tex'
  template = latex_jinja_env.get_template(in_file)
  pwidth = random.randint(3, 8)
  pheight = random.randint(3, 8)
  angle =  math.degrees(math.atan(pheight / pwidth))
  return template.render(pwidth=pwidth, pheight=pheight, angle=angle)

def getL2():
  in_file = 'rttL2.tex'
  template = latex_jinja_env.get_template(in_file)
  pwidth = random.randint(3, 8)
  pheight = random.randint(3, 8)
  angle =  math.degrees(math.atan(pheight / pwidth))
  questions = ['How long is the ladder?', 
              'How far away from the house is the bottom of the ladder?',
              'How high above the ground does the ladder touch the house?']
  answers = [
    [],[],[]
  ]
  qrand = random.randint(0, len(questions) - 1)
  
  return template.render(pwidth=pwidth, 
                        pheight=pheight, 
                        angle=angle, 
                        question = questions[qrand])

def get_tABx(): 
  return get_tAB.get_x()
def get_tABo1(): 
  return get_tAB.get_o1()
def get_tABo2(): 
  return get_tAB.get_o2()
def get_tBCx():
  return get_tBC.get_x()
def get_tBCo1():
  return get_tBC.get_o1()
def get_tBCo2():
  return get_tBC.get_o2()
def get_tACx():
  return get_tAC.get_x()
def get_tACo1():
  return get_tAC.get_o1()
def get_tACo2():
  return get_tAC.get_o2()
def get_tAo1x(): 
  return get_tAo1.get_x()
def get_tAo1B():
  return get_tAo1.get_B()
def get_tAo1o2():
  return get_tAo1.get_o2()
def get_tAo2x():
  return get_tAo2.get_x()
def get_tAo2B():
  return get_tAo2.get_B()
def get_tAo2o1():
  return get_tAo2.get_o1()
def get_tBo1x():
  return get_tBo1.get_x()
def get_tBo1A():
  return get_tBo1.get_A()
def get_tBo1o2():
  return get_tBo1.get_o2()
def get_tBo2x():
  return get_tBo2.get_x()
def get_tBo2A():
  return get_tBo2.get_A()
def get_tBo2o1():
  return get_tBo2.get_o1()
def get_tCo1A():
  return get_tCo1.get_A()
def get_tCo1B():
  return get_tCo1.get_B()
def get_tCo1o2():
  return get_tCo1.get_o2()
def get_tCo2A():
  return get_tCo2.get_A()
def get_tCo2B():
  return get_tCo2.get_B()
def get_tCo2o1():
  return get_tCo2.get_o1()
