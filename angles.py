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

coterminalD = latex_jinja_env.get_template('templates/angles/coterminalD.tex')
coterminalR = latex_jinja_env.get_template('templates/angles/coterminalR.tex')
convertDtoR = latex_jinja_env.get_template('templates/angles/convertDtoR.tex')
convertRtoD = latex_jinja_env.get_template('templates/angles/convertRtoD.tex')

a = 3
b = 4
c = 5
o1 = 36.87
o2 = 53.13
answer_options = {
  1: math.radians(math.sin(a / b)),
  2: math.radians(math.sin(a / c)),
  3: math.radians(math.sin(b / a)),
  4: math.radians(math.sin(b / c)),
  5: math.radians(math.sin(c / a)),
  6: math.radians(math.sin(c / b)),
  7: math.degrees(math.asin(a / b)),
  8: math.degrees(math.asin(a / c)),
  # 9: math.degrees(math.asin(b / a)),
  10: math.degrees(math.asin(b / c)),
  # 11: math.degrees(math.asin(c / a)),
  # 12: math.degrees(math.asin(c / b)),
  13: a / math.sin(math.radians(o1)),
  14: a / math.cos(math.radians(o1)),
  15: a / math.tan(math.radians(o1)),
  16: a / math.sin(math.radians(o2)),
  17: a / math.cos(math.radians(o2)),
  18: a / math.tan(math.radians(o2)),
  19: math.radians(math.cos(a / b)),
  20: math.radians(math.cos(a / c)),
  21: math.radians(math.cos(b / a)),
  22: math.radians(math.cos(b / c)),
  23: math.radians(math.cos(c / a)),
  24: math.radians(math.cos(c / b)),
  25: math.degrees(math.acos(a / b)),
  26: math.degrees(math.acos(a / c)),
  # 27: math.degrees(math.acos(b / a)),
  28: math.degrees(math.acos(b / c)),
  # 29: math.degrees(math.acos(c / a)),
  # 30: math.degrees(math.acos(c / b)),
  31: b / math.sin(math.radians(o1)),
  32: b / math.cos(math.radians(o1)),
  33: b / math.tan(math.radians(o1)),
  34: b / math.sin(math.radians(o2)),
  35: b / math.cos(math.radians(o2)),
  36: b / math.tan(math.radians(o2)),
  37: math.radians(math.tan(a / b)),
  38: math.radians(math.tan(a / c)),
  39: math.radians(math.tan(b / a)),
  40: math.radians(math.tan(b / c)),
  41: math.radians(math.tan(c / a)),
  42: math.radians(math.tan(c / b)),
  43: math.degrees(math.atan(a / b)),
  44: math.degrees(math.atan(a / c)),
  45: math.degrees(math.atan(b / a)),
  46: math.degrees(math.atan(b / c)),
  47: math.degrees(math.atan(c / a)),
  48: math.degrees(math.atan(c / b)),
  49: c / math.sin(math.radians(o1)),
  50: c / math.cos(math.radians(o1)),
  51: c / math.tan(math.radians(o1)),
  52: c / math.sin(math.radians(o2)),
  53: c / math.cos(math.radians(o2)),
  54: c / math.tan(math.radians(o2)),
  55: math.sqrt(math.pow(c, 2) - math.pow(b, 2)),
  56: math.sqrt(math.pow(c, 2) - math.pow(a, 2)),
  57: a * math.radians(math.sin(o1)),
  58: a * math.radians(math.cos(o1)),
  59: a * math.radians(math.tan(o1)),
  60: b * math.radians(math.sin(o1)),
  61: b * math.radians(math.cos(o1)),
  62: b * math.radians(math.tan(o1)),
  63: c * math.radians(math.sin(o1)),
  64: c * math.radians(math.cos(o1)),
  65: c * math.radians(math.tan(o1)),
  66: a * math.radians(math.sin(o2)),
  67: a * math.radians(math.cos(o2)),
  68: a * math.radians(math.tan(o2)),
  69: b * math.radians(math.sin(o2)),
  70: b * math.radians(math.cos(o2)),
  71: b * math.radians(math.tan(o2)),
  72: c * math.radians(math.sin(o2)),
  73: c * math.radians(math.cos(o2)),
  74: c * math.radians(math.tan(o2)),
  75: math.sqrt(math.pow(a, 2) + math.pow(b, 2)),
  76: math.sqrt(math.pow(c, 2) - math.pow(b, 2)),
  77: math.sqrt(math.pow(c, 2) - math.pow(a, 2)),
  78: 90 - o1,
  79: 90 - o2,
  80: math.sqrt(math.fabs(math.pow(a, 2) - math.pow(b, 2))),
  81: a + b,
  82: math.pow(a, 2) + math.pow(b, 2),
  83: math.sqrt(math.pow(a, 2)) + math.sqrt(math.pow(b, 2)),
  84: math.sqrt(math.pow(c, 2) + math.pow(b, 2)),
  85: math.pow(c, 2) - math.pow(b, 2),
  86: math.sqrt(math.pow(c, 2) + math.pow(a, 2)),
  87: math.pow(c, 2) - math.pow(a, 2),
  88: 90 - o1,
  89: 90 + o1,
  90: 45,
  91: 180 - o1,
  92: 90 - o2,
  93: 90 + o2,
  94: 180 - o2

}

def get_coterminalD():
  angle = random.randint(-360, 360)
  multiplier = random.randint(1, 3)
  answers = [
    angle + (360 * multiplier),
    360,
    angle - 180,
    90 + angle
  ]
  answer = answers[0]
  random.shuffle(answers)
  print (answer_options[13])
  return coterminalD.render(angle=angle, answers=answers)

def get_convertDtoR():
  angle = random.choice([30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330])
  multiplier = random.randint(1, 3)
  angle = angle * multiplier
  prompts = [
    'Convert ' + str(angle) + 'º into radians.',
    'What is ' + str(angle) +' º, expressed into radians?'
  ]
  answers = [
    math.radians(angle),
    angle + 360,
    360 * math.radians(angle),
    math.radians(360)
  ]
  answer = answers[0]
  random.shuffle(prompts)
  random.shuffle(answers)
  return convertDtoR.render(angle = angle, prompt=prompts[0], answers=answers)
