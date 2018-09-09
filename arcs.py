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

coterminal = latex_jinja_env.get_template('templates/arcs/arclength.tex')

def get_arclength():
  radius = random.randint(2, 15)
  angle = random.choice([30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330])
  answers = [
    radius * math.radians(angle),
    360 * math.radians(angle),
    360 * radius,
    angle * radius
  ]
  answer = answers[0]
  random.shuffle(answers)
  return coterminal.render(angle=angle, radius=radius, answers=answers)

