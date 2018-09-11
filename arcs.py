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
al_cma = latex_jinja_env.get_template('templates/arcs/al_cma.tex')
al_rma = latex_jinja_env.get_template('templates/arcs/al_rma.tex')
al_dma = latex_jinja_env.get_template('templates/arcs/al_dma.tex')
al_lcm = latex_jinja_env.get_template('templates/arcs/al_lcm.tex')
al_ldm = latex_jinja_env.get_template('templates/arcs/al_ldm.tex')
al_lrm = latex_jinja_env.get_template('templates/arcs/al_lrm.tex')
al_lmc = latex_jinja_env.get_template('templates/arcs/al_lmc.tex')
al_lmr = latex_jinja_env.get_template('templates/arcs/al_lmr.tex')
al_lmd = latex_jinja_env.get_template('templates/arcs/al_lmd.tex')


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

def get_al_cma():
  c = random.randint(1, 1500)
  m = random.choice([30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330])
  answers = [
    (c * m) / 360,
    360,
    180,
    90
  ]
  random.shuffle(answers)
  return al_cma.render(c=c, m=m, answers=answers)
def get_al_rma():
  r = random.randint(1, 1500)
  m = random.choice([30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330])
  answers = [
    (2 * math.pi * r * m) / 360,
    360,
    180,
    90
  ]
  return al_rma.render(r=r, m=m, answers=answers)
def get_al_dma():
  d = random.randint(1, 1500)
  m = random.choice([30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330])
  answers = [
    (math.pi * d * m) / 360,
    360,
    180,
    90
  ]
  return al_dma.render(d=d, m=m, answers=answers)
def get_al_lcm():
  l = random.randint(1, 500)
  c = random.randint(1, 500)
  answers = [
    (l * 360) / c,
    360,
    180,
    90
  ]
  return al_lcm.render(l=l, c=c, answers=answers)
def get_al_lrm():
  l = random.randint(1, 500)
  r = random.randint(1, 300)
  answers = [
    (l * 360) / (2 * math.pi * r),
    360,
    180,
    90
  ]
  return al_lrm.render(l=l, r=r, answers=answers)
def get_al_ldm():
  l = random.randint(1, 500)
  d = random.randint(1, 300)
  answers = [
    (l * 360) / (math.pi * d),
    360,
    180,
    90
  ]
  return al_ldm.render(l=l, d=d, answers=answers)
def get_al_lmc():
  l = random.randint(1, 500)
  m = random.choice([30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330])
  answers = [
    (l * 360) / m,
    360,
    180,
    90
  ]
  return al_lmc.render(l=l, m=m, answers=answers)
def get_al_lmr():
  l = random.randint(1, 500)
  m = random.choice([30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330])
  answers = [
    (l * 360) / (2 * math.pi * m),
    360,
    180,
    90
  ]
  return al_lmr.render(l=l, m=m, answers=answers)
def get_al_lmd():
  l = random.randint(1, 500)
  m = random.choice([30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330])
  answers = [
    (l * 360) / (math.pi * m),
    360,
    180,
    90
  ]
  return al_lmd.render(l=l, m=m, answers=answers)