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
  return random.randint(1, 750)
def get_random_diameter():
  return random.randint(1, 1500)
def get_random_length():
  return random.randint(1, 500)

# def get_c(l=None, m=None, d=None, r=None):
#   if l is not None and m is not None:
#     return l * 360 / m
#   if r is not None:
#     return math.pi * r * 2
#   else:
#     return math.pi * d

# def get_l(c, m):
#   return (c * m) / 360

# def get_m(c, l):
#   return (l * 360) / c

# def get_d(c):
#   return c / math.pi

# def get_r(c):
#   return c / (2 * math.pi)

# def get_answer(l=None, m=None, c=None, d=None, r=None):
#   if c is None:
#     c = get_c(l=l, m=m, d=d, r=r)
#   if l is None:
#     l = get_l(c, m)
#   if m is None:
#     m = get_m(c, l)
#   if d is None:
#     d = get_d(c)
#   if r is None:
#     r = get_r(c)

#   return {
#     'c': c,
#     'l': l,
#     'm': m,
#     'd': d,
#     'r': r
#   }

def get_options(f, c=None, l=None, m=None, d=None, r=None):
  options = []
  for formula in formulas_al[f]:
    options.append(
      round(eval(formulas_al[f][formula], {'c':c, 'l':l, 'm':m, 'd':d, 'r':r }, {'math': math}), 2)
    )
  return options

def get_al_cml():
  c = get_random_circumference()
  m = get_random_unit_circle_angle()
  answers = get_options('cml', c=c, m=m)
  # answers.append(get_answer(c=c, m=m)['l'])
  # random.shuffle(answers)
  return al_cma.render(c=c, m=m, answers=answers)

def get_al_rml():
  r = get_random_radius()
  m = get_random_unit_circle_angle()
  answers = get_options('rml', r=r, m=m)
  # answers.append(get_answer(r=r, m=m)['l'])
  # random.shuffle(answers)
  return al_rma.render(r=r, m=m, answers=answers)

def get_al_dml():
  d = get_random_diameter()
  m = get_random_unit_circle_angle()
  answers = get_options('dml', d=d, m=m)
  # answers.append(get_answer(d=d, m=m)['l'])
  # random.shuffle(answers)
  return al_dma.render(d=d, m=m, answers=answers)

def get_al_lcm():
  l = get_random_length()
  c = get_random_circumference()
  answers = get_options('lcm', l=l, c=c)
  # answers.append(get_answer(l=l, c=c)['m'])
  # random.shuffle(answers)
  return al_lcm.render(l=l, c=c, answers=answers)

def get_al_lrm():
  l = get_random_length()
  r = get_random_radius()
  answers = get_options('lrm', l=l, r=r)
  # answers.append(get_answer(l=l, r=r)['m'])
  # random.shuffle(answers)
  return al_lrm.render(l=l, r=r, answers=answers)

def get_al_ldm():
  l = get_random_length()
  d = get_random_diameter()
  answers = get_options('ldm', l=l, d=d)
  # answers.append(get_answer(l=l, d=d)['m'])
  # random.shuffle(answers)
  return al_ldm.render(l=l, d=d, answers=answers)

def get_al_lmc():
  l = get_random_length()
  m = get_random_unit_circle_angle()
  answers = get_options('lmc', l=l, m=m)
  # answers.append(get_answer(l=l, m=m)['c'])
  # random.shuffle(answers)
  return al_lmc.render(l=l, m=m, answers=answers)

def get_al_lmr():
  l = get_random_length()
  m = get_random_unit_circle_angle()
  answers = get_options('lmr', l=l, m=m)
  # answers.append(get_answer(l=l, m=m)['r'])
  # random.shuffle(answers)
  return al_lmr.render(l=l, m=m, answers=answers)

def get_al_lmd():
  l = get_random_length()
  m = get_random_unit_circle_angle()
  answers = get_options('lmd', l=l, m=m)
  # answers.append(get_answer(l=l, m=m)['d'])
  # random.shuffle(answers)
  return al_lmd.render(l=l, m=m, answers=answers)