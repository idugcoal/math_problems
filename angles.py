import math
import random
import subprocess
import sys
from config import latex_jinja_env

coterminalD = latex_jinja_env.get_template('templates/angles/coterminalD.tex')
coterminalR = latex_jinja_env.get_template('templates/angles/coterminalR.tex')
convertDtoR = latex_jinja_env.get_template('templates/angles/convertDtoR.tex')
convertRtoD = latex_jinja_env.get_template('templates/angles/convertRtoD.tex')
referenceD = latex_jinja_env.get_template('templates/angles/referenceD.tex')
referenceR = latex_jinja_env.get_template('templates/angles/referenceR.tex')

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

# answer_expressions = {
  # 1: '$sin$$\frac{\VAR{a}}{\VAR{b}}$',
  # 2: '$\\frac{\VAR{a}}{\VAR{b}}$',
  # 2: '\\sin\\frac{\\VAR{a}}{\\VAR{c}}',
  # 3: '\\sin\\frac{\\VAR{b}}{\\VAR{a}}',
  # 4: '\\sin\\frac{\\VAR{b}}{\\VAR{c}}',
  # 5: '\\sin\\frac{\\VAR{c}}{\\VAR{a}}',
  # 6: '\\sin\\frac{\\VAR{c}}{\\VAR{b}}',
  # 7: '\\arcsin\\frac{\\VAR{a}}{\\VAR{b}}',
  # 8: '\\arcsin\\frac{\\VAR{a}}{\\VAR{c}}',
  # 9: '\\arcsin\\frac{\\VAR{b}}{\\VAR{a}}',
  # 10: '\\arcsin\\frac{\\VAR{b}}{\\VAR{c}}',
  # 11: '\\arcsin\\frac{\\VAR{c}}{\\VAR{a}}',
  # 12: '\\arcsin\\frac{\\VAR{c}}{\\VAR{b}}',
  # 13: 'a\\frac{}{} \\sin\\VAR{o1}',
  # 14: 'a\\frac{}{} \\cos\\VAR{o1}',
  # 15: 'a\\frac{}{} \\tan\\VAR{o1}',
  # 16: 'a\\frac{}{} \\sin\\VAR{o2}',
  # 17: 'a\\frac{}{} \\cos\\VAR{o2}',
  # 18: 'a\\frac{}{} \\tan\\VAR{o2}',
  # 19: '\\cos\\frac{\\VAR{a}}{\\VAR{b}}',
  # 20: '\\cos\\frac{\\VAR{a}}{\\VAR{c}}',
  # 21: '\\cos\\frac{\\VAR{b}}{\\VAR{a}}',
  # 22: '\\cos\\frac{\\VAR{b}}{\\VAR{c}}',
  # 23: '\\cos\\frac{\\VAR{c}}{\\VAR{a}}',
  # 24: '\\cos\\frac{\\VAR{c}}{\\VAR{b}}',
  # 25: '\\arccos\\frac{\\VAR{a}}{\\VAR{b}}',
  # 26: '\\arccos\\frac{\\VAR{a}}{\\VAR{c}}',
  # 27: '\\arccos\\frac{\\VAR{b}}{\\VAR{a}}',
  # 28: '\\arccos\\frac{\\VAR{b}}{\\VAR{c}}',
  # 29: '\\arccos\\frac{\\VAR{c}}{\\VAR{a}}',
  # 30: '\\arccos\\frac{\\VAR{c}}{\\VAR{b}}',
  # 31: '\\frac{\\VAR{b}}{\\sin\\VAR{o1}}',
  # 32: '\\frac{\\VAR{b}}{\\cos\\VAR{o1}}',
  # 33: '\\frac{\\VAR{b}}{\\tan\\VAR{o1}}',
  # 34: '\\frac{\\VAR{b}}{\\sin\\VAR{o2}}',
  # 35: '\\frac{\\VAR{b}}{\\cos\\VAR{o2}}',
  # 36: '\\frac{\\VAR{b}}{\\tan\\VAR{o2}}',
  # 37: '\\tan\\frac{\\VAR{a}}{\\VAR{b}}',
  # 38: '\\tan\\frac{\\VAR{a}}{\\VAR{c}}',
  # 39: '\\tan\\frac{\\VAR{b}}{\\VAR{a}}',
  # 40: '\\tan\\frac{\\VAR{b}}{\\VAR{c}}',
  # 41: '\\tan\\frac{\\VAR{c}}{\\VAR{a}}',
  # 42: '\\tan\\frac{\\VAR{c}}{\\VAR{b}}',
  # 43: '\\arctan\\frac{\\VAR{a}}{\\VAR{b}}',
  # 44: '\\arctan\\frac{\\VAR{a}}{\\VAR{c}}',
  # 45: '\\arctan\\frac{\\VAR{b}}{\\VAR{a}}',
  # 46: '\\arctan\\frac{\\VAR{b}}{\\VAR{c}}',
  # 47: '\\arctan\\frac{\\VAR{c}}{\\VAR{a}}',
  # 48: '\\arctan\\frac{\\VAR{c}}{\\VAR{b}}',
  # 49: '\\frac{\\VAR{c}}{\\sin\\VAR{o1}}',
  # 50: '\\frac{\\VAR{c}}{\\cos\\VAR{o1}}',
  # 51: '\\frac{\\VAR{c}}{\\tan\\VAR{o1}}',
  # 52: '\\frac{\\VAR{c}}{\\sin\\VAR{o2}}',
  # 53: '\\frac{\\VAR{c}}{\\cos\\VAR{o2}}',
  # 54: '\\frac{\\VAR{c}}{\\tan\\VAR{o2}}',
  # 55: 'math.sqrt(math.pow(c, 2) - math.pow(b, 2))',
  # 56: 'math.sqrt(math.pow(c, 2) - math.pow(a, 2))',
  # 57: 'a * \\sin\\VAR{o1}',
  # 58: 'a * \\cos\\VAR{o1}',
  # 59: 'a * \\tan\\VAR{o1}',
  # 60: 'b * \\sin\\VAR{o1}',
  # 61: 'b * \\cos\\VAR{o1}',
  # 62: 'b * \\tan\\VAR{o1}',
  # 63: 'c * \\sin\\VAR{o1}',
  # 64: 'c * \\cos\\VAR{o1}',
  # 65: 'c * \\tan\\VAR{o1}',
  # 66: 'a * \\sin\\VAR{o2}',
  # 67: 'a * \\cos\\VAR{o2}',
  # 68: 'a * \\tan\\VAR{o2}',
  # 69: 'b * \\sin\\VAR{o2}',
  # 70: 'b * \\cos\\VAR{o2}',
  # 71: 'b * \\tan\\VAR{o2}',
  # 72: 'c * \\sin\\VAR{o2}',
  # 73: 'c * \\cos\\VAR{o2}',
  # 74: 'c * \\tan\\VAR{o2}',
  # 75: 'math.sqrt(math.pow(a, 2) + math.pow(b, 2))',
  # 76: 'math.sqrt(math.pow(c, 2) - math.pow(b, 2))',
  # 77: 'math.sqrt(math.pow(c, 2) - math.pow(a, 2))',
  # 78: '90 - o1',
  # 79: '90 - o2',
  # 80: 'math.sqrt(math.fabs(math.pow(a, 2) - math.pow(b, 2)))',
  # 81: 'a + b',
  # 82: 'math.pow(a, 2) + math.pow(b, 2)',
  # 83: 'math.sqrt(math.pow(a, 2)) + math.sqrt(math.pow(b, 2))',
  # 84: 'math.sqrt(math.pow(c, 2) + math.pow(b, 2))',
  # 85: 'math.pow(c, 2) - math.pow(b, 2)',
  # 86: 'math.sqrt(math.pow(c, 2) + math.pow(a, 2))',
  # 87: 'math.pow(c, 2) - math.pow(a, 2)',
  # 88: '90 - o1',
  # 89: '90 + o1',
  # 90: '45',
  # 91: '180 - o1',
  # 92: '90 - o2',
  # 93: '90 + o2',
  # 94: '180 - o2'
# }

def get_coterminalD():
  angle = random.randint(-360, 360)
  multiplier = random.randint(1, 3)
  answers = [
    (angle * math.pi) / 180,
    180 / (angle * math.pi),
    angle * math.pi,
    math.radians(random.choice([30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330]))
  ]
  answer = answers[0]
  random.shuffle(answers)
  return coterminalD.render(angle=angle, answers=answers, a=a,b=b,c=c,o1=o1,o2=o2)

def get_convertDtoR():
  angle = random.randint(1, 359)
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
  return convertDtoR.render(angle=angle, answers=answers, prompt=prompts[0])

def get_convertRtoD():
  angle = random.randint(1, 360)
  answers = [
    math.radians(angle),
    angle + 360,
    360 * math.radians(angle),
    math.radians(360)
  ]
  return convertRtoD.render(angle=angle, answers=answers)

# TODO: if answer appears twice, add 15 to it
def get_referenceD():
  # angle = random.randint(1, 360)
  angle = 315
  multiplier = random.choice([-3, -2, -1, 1, 2, 3])
  prompt = angle + (360 * multiplier)
  print(angle, multiplier)
  if(prompt > 1 + (360 * multiplier) and prompt < 89 + (360 * multiplier) ):
    answers = [
      prompt - (360 * multiplier),
      random.choice([180, 360]),
      abs(angle),
    ]
  elif(prompt > 91 + (360 * multiplier) and prompt < 179 + (360 * multiplier)):
    answers = [
      180 - (prompt - (360 * multiplier)),
      90 + (prompt - (360 * multiplier)),
      random.choice([180, 360]),
      abs(angle),
    ]
  elif(prompt > 181 + (360 * multiplier) and prompt < 269 + (360 * multiplier)):
    answers = [
      prompt - (360 * multiplier) - 180,
      270 - (prompt - (360 * multiplier)),
      random.choice([180, 360]),
      abs(angle),
    ]
  else:
    answers = [
      360 - (prompt - (360 * multiplier)),
      (prompt - (360 * multiplier)) - 270,
      random.choice([180, 360]),
      abs(angle),
    ] 
  random.shuffle(answers)
  return referenceD.render(prompt=prompt, answers=answers)