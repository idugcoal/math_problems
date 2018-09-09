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

coterminal = latex_jinja_env.get_template('templates/angles/coterminal.tex')
convert = latex_jinja_env.get_template('templates/angles/convert.tex')

def get_coterminal():
  angle = random.randint(-360, 360)
  multiplier = random.randint(1, 3)
  answers = [
    angle + (360 * multiplier),
    360,
    angle - 300,
    320 + angle
  ]
  answer = answers[0]
  random.shuffle(answers)
  return coterminal.render(angle=angle, answers=answers)
def get_convert():
  angle = random.choice([30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330])
  multiplier = random.randint(1, 3)
  angle = angle * multiplier
  answers = [
    math.radians(angle),
    angle + 360,
    360 * math.radians(angle),
    math.radians(360)
  ]
  answer = answers[0]
  random.shuffle(answers)
  return convert.render(angle = angle, answers=answers)
