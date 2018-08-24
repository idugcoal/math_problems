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