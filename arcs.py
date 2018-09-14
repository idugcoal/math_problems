import math
import random
import subprocess
import sys
from config import latex_jinja_env
from config import formulas_al

al_cma = latex_jinja_env.get_template('templates/arcs/al_cma.tex')
al_rma = latex_jinja_env.get_template('templates/arcs/al_rma.tex')
al_dma = latex_jinja_env.get_template('templates/arcs/al_dma.tex')
al_lcm = latex_jinja_env.get_template('templates/arcs/al_lcm.tex')
al_ldm = latex_jinja_env.get_template('templates/arcs/al_ldm.tex')
al_lrm = latex_jinja_env.get_template('templates/arcs/al_lrm.tex')
al_lmc = latex_jinja_env.get_template('templates/arcs/al_lmc.tex')
al_lmr = latex_jinja_env.get_template('templates/arcs/al_lmr.tex')
al_lmd = latex_jinja_env.get_template('templates/arcs/al_lmd.tex')

def get_c(d=None, r=None):
  if d is None:
    return math.pi * r * 2
  else:
    return math.pi * d

def get_l(c, m):
  return (c * m) / 360

def get_m(c, l):
  return (l * 360) / c

def get_answer(l=None, m=None, c=None, d=None, r=None):
  if c is None:
    c = get_c(r, d)
  else:
    if l is None:
      l = get_l(c, m)
    else:
      m = get_m(c, l)
  print(l, m, c)

def get_random_unit_circle_angle(): 
  return random.choice([30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330])

def get_random_circumference():
  return random.randint(1, 1500)

def get_al_cml():
  c = get_random_circumference()
  m = get_random_unit_circle_angle()
  answers=[1,2,3,4]
  answer = get_answer(c=c, m=m)
  # answer = answers[0]
  print(eval(formulas_al[2], {'c': c, 'm': m}))
  random.shuffle(answers)
  return al_cma.render(c=c, m=m, answers=answers)

def get_al_rml():
  r = random.randint(1, 1500)
  m = get_random_unit_circle_angle()
  answers = [
    (2 * math.pi * r * m) / 360,
    (r * m) / 360,
    360 / (2 * math.pi * r * m),
    (2 * math.pi * r * m) - 360
  ]
  answer = answers[0]
  random.shuffle(answers)
  return al_rma.render(r=r, m=m, answers=answers)

def get_al_dml():
  d = random.randint(1, 1500)
  m = get_random_unit_circle_angle()
  answers = [
    (math.pi * d * m) / 360,
    360 / (math.pi * d * m),
    (math.pi * d * m) - 360,
    (d * m) / 360
  ]
  answer = answers[0]
  random.shuffle(answers)
  return al_dma.render(d=d, m=m, answers=answers)

def get_al_lcm():
  l = random.randint(1, 500)
  c = get_random_circumference()
  answers = [
    (l * 360) / c,
    c / (l *360),
    (l * 360) - c,
    (c * 360) / l
  ]
  answer = answers[0]
  random.shuffle(answers)
  return al_lcm.render(l=l, c=c, answers=answers)

def get_al_lrm():
  l = random.randint(1, 500)
  r = random.randint(1, 300)
  answers = [
    (l * 360) / (2 * math.pi * r),
    (2 * math.pi * r) / (l * 360),
    (l * 360) - (2 * math.pi * r),
    (l * 360) / r
  ]
  answer = answers[0]
  random.shuffle(answers)
  return al_lrm.render(l=l, r=r, answers=answers)

def get_al_ldm():
  l = random.randint(1, 500)
  d = random.randint(1, 300)
  answers = [
    (l * 360) / (math.pi * d),
    (math.pi * d) / (l * 360),
    (l * 360) - (math.pi * d),
    (l * 360) / d
  ]
  answer = answers[0]
  random.shuffle(answers)
  return al_ldm.render(l=l, d=d, answers=answers)

def get_al_lmc():
  l = random.randint(1, 500)
  m = get_random_unit_circle_angle()
  answers = [
    (l * 360) / m,
    m / (l * 360),
    (l * 360) - m,
    (m * 360) / l 
  ]
  answer = answers[0]
  random.shuffle(answers)
  return al_lmc.render(l=l, m=m, answers=answers)

def get_al_lmr():
  l = random.randint(1, 500)
  m = get_random_unit_circle_angle()
  answers = [
    (l * 360) / (2 * math.pi * m),
    (2 * math.pi * m) / (l * 360),
    (l * 360) - (2 * math.pi * m),
    (m * 360) / (2 * math.pi * l)
  ]
  answer = answers[0]
  random.shuffle(answers)
  return al_lmr.render(l=l, m=m, answers=answers)

def get_al_lmd():
  l = random.randint(1, 500)
  m = get_random_unit_circle_angle()
  answers = [
    (l * 360) / (math.pi * m),
    (math.pi * m) / (l * 360),
    (l * 360) - (math.pi * m),
    (m * 360) / (math.pi * l)
  ]
  answer = answers[0]
  random.shuffle(answers)
  return al_lmd.render(l=l, m=m, answers=answers)