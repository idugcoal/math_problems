import math
import random
import jinja2
import os
import subprocess
from jinja2 import Template

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

def generate_problem(f):
  template = latex_jinja_env.get_template(f)
  x = random.randint(5, 10)
  angle = random.randint(10, 50)
  w = x * math.cos(math.radians(angle))
  h = x * math.sin(math.radians(angle))
  return template.render(pwidth=w, pheight=h, angle=angle, hyp=x)

def get_A():
  in_file = 'triangles/tCo2A.tex'
  return generate_problem(in_file)

def get_B(): 
  in_file = 'triangles/tCo2B.tex'
  return generate_problem(in_file)

def get_o1(): 
  in_file = 'triangles/tCo2o1.tex'
  return generate_problem(in_file)