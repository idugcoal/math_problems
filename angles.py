import math
import random
import subprocess
import sys
from config import latex_jinja_env
# from config import formulas_a

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

def get_random_unit_circle_angle(): 
  return random.choice([30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330])

def get_random_angle():
  allowed_values = list(range(1, 361))
  return random.choice(allowed_values)

def get_multiplier(min, max):
  allowed_values = list(range(min, max + 1))
  allowed_values.remove(0)
  return random.choice(allowed_values)

def get_coterminalD():
  angle = get_random_angle() * get_multiplier(-1, 1)
  multiplier = get_multiplier(1, 3)
  answers = [
    (angle * math.pi) / 180,
    180 / (angle * math.pi),
    angle * math.pi,
    math.radians(get_random_unit_circle_angle())
  ]
  answer = answers[0]
  random.shuffle(answers)
  return coterminalD.render(angle=angle, answers=answers, a=a,b=b,c=c,o1=o1,o2=o2)

def get_convertDtoR():
  angle = get_random_angle()
  prompts = [
    'Convert ' + str(angle) + 'º into radians.',
    'What is ' + str(angle) +' º, expressed into radians?'
  ]
  # answers = [
  #   math.radians(angle),
  #   angle + 360,
  #   360 * math.radians(angle),
  #   math.radians(360)
  # ]
  answers = [
    (angle * math.pi) / 180,
    180 / (angle * math.pi),
    angle * math.pi,
    5/6
  ]
  answer = answers[0]
  random.shuffle(prompts)
  return {
  'q': convertDtoR.render(angle=angle, answers=answers, prompt=prompts[0]),
  'a': answer
  }

def get_convertRtoD():
  angle = get_random_angle()
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
  angle = get_random_unit_circle_angle()
  multiplier = get_multiplier(-3, 3)
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