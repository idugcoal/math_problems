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
  x = random.randint(6, 8)
  h = random.randint(3, 5)
  w = math.sqrt(math.pow(x, 2) - math.pow(h, 2))
  return template.render(pwidth=w, pheight=h, hyp=x)

def get_x():
  in_file = 'triangles/tBCx.tex'
  return generate_problem(in_file)

def get_o1(): 
  in_file = 'triangles/tBCo1.tex'
  return generate_problem(in_file)

def get_o2(): 
  in_file = 'triangles/tBCo2.tex'
  return generate_problem(in_file)