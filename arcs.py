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

def get_random_unit_circle_angle(): 
  return random.choice([30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330])
def get_random_circumference():
  return random.randint(1, 1500)
def get_random_radius():
  return random.randint(1, 1500)
def get_random_diameter():
  return random.randint(1, 1500)
def get_random_length():
  return random.randint(1, 500)

def get_c(l=None, m=None, d=None, r=None):
  if l is not None and m is not None:
    return l * 360 / m
  if r is not None:
    return math.pi * r * 2
  else:
    return math.pi * d

def get_l(c, m):
  return (c * m) / 360

def get_m(c, l):
  return (l * 360) / c

def get_d(c):
  return c / math.pi

def get_r(c):
  return c / (2 * math.pi)

def get_answer(l=None, m=None, c=None, d=None, r=None):
  if c is None:
    c = get_c(l=l, m=m, d=d, r=r)
  if l is None:
    l = get_l(c, m)
  if m is None:
    m = get_m(c, l)
  if d is None:
    d = get_d(c)
  if r is None:
    r = get_r(c)

  return {
    'c': c,
    'l': l,
    'm': m,
    'd': d,
    'r': r
  }
def get_options(f, c=None, l=None, m=None, d=None, r=None):
  options = []
  for formula in formulas_al[f]:
    options.append(eval(formulas_al[f][formula], {'c':c, 'l':l, 'm':m, 'd':d, 'r':r }))
  return options

def get_al_cml():
  c = get_random_circumference()
  m = get_random_unit_circle_angle()
  answer = get_answer(c=c, m=m)
  answers = get_options('cml', c=c, m=m)
  # for a in formulas_al['cml']:
    # answers.append(eval(formulas_al['cml'][a], {'c': c, 'm': m}))
  answers.append(answer['l'])
  random.shuffle(answers)
  return al_cma.render(c=c, m=m, answers=answers)

def get_al_rml():
  r = get_random_radius()
  m = get_random_unit_circle_angle()
  answers = [
    (2 * math.pi * r * m) / 360,
    (r * m) / 360,
    360 / (2 * math.pi * r * m),
    (2 * math.pi * r * m) - 360
  ]
  answer = get_answer(r=r, m=m)
  print(answers[0], answer['l'])
  random.shuffle(answers)
  return al_rma.render(r=r, m=m, answers=answers)

def get_al_dml():
  d = get_random_diameter()
  m = get_random_unit_circle_angle()
  answers = [
    (math.pi * d * m) / 360,
    360 / (math.pi * d * m),
    (math.pi * d * m) - 360,
    (d * m) / 360
  ]
  answer = get_answer(d=d, m=m)
  print(answers[0], answer['l'])
  random.shuffle(answers)
  return al_dma.render(d=d, m=m, answers=answers)

def get_al_lcm():
  l = get_random_length()
  c = get_random_circumference()
  answers = [
    (l * 360) / c,
    c / (l *360),
    (l * 360) - c,
    (c * 360) / l
  ]
  answer = get_answer(c=c, l=l)
  print(answers[0], answer['m'])
  random.shuffle(answers)
  return al_lcm.render(l=l, c=c, answers=answers)

def get_al_lrm():
  l = get_random_length()
  r = get_random_radius()
  answers = [
    (l * 360) / (2 * math.pi * r),
    (2 * math.pi * r) / (l * 360),
    (l * 360) - (2 * math.pi * r),
    (l * 360) / r
  ]
  answer = get_answer(r=r, l=l)
  print(answers[0], answer['m'])
  random.shuffle(answers)
  return al_lrm.render(l=l, r=r, answers=answers)

def get_al_ldm():
  l = get_random_length()
  d = get_random_diameter()
  answers = [
    (l * 360) / (math.pi * d),
    (math.pi * d) / (l * 360),
    (l * 360) - (math.pi * d),
    (l * 360) / d
  ]
  answer = get_answer(l=l, d=d)
  print(answers[0], answer['m'])
  random.shuffle(answers)
  return al_ldm.render(l=l, d=d, answers=answers)

def get_al_lmc():
  l = get_random_length()
  m = get_random_unit_circle_angle()
  answers = [
    (l * 360) / m,
    m / (l * 360),
    (l * 360) - m,
    (m * 360) / l 
  ]
  answer = get_answer(l=l, m=m)
  print(answers[0], answer['c'])
  random.shuffle(answers)
  return al_lmc.render(l=l, m=m, answers=answers)

def get_al_lmr():
  l = get_random_length()
  m = get_random_unit_circle_angle()
  answers = [
    (l * 360) / (2 * math.pi * m),
    (2 * math.pi * m) / (l * 360),
    (l * 360) - (2 * math.pi * m),
    (m * 360) / (2 * math.pi * l)
  ]
  answer = get_answer(l=l, m=m)
  print(answers[0], answer['r'])
  random.shuffle(answers)
  return al_lmr.render(l=l, m=m, answers=answers)

def get_al_lmd():
  l = get_random_length()
  m = get_random_unit_circle_angle()
  answers = [
    (l * 360) / (math.pi * m),
    (math.pi * m) / (l * 360),
    (l * 360) - (math.pi * m),
    (m * 360) / (math.pi * l)
  ]
  answer = get_answer(l=l, m=m)
  print(answers[0], answer['d'])
  random.shuffle(answers)
  return al_lmd.render(l=l, m=m, answers=answers)