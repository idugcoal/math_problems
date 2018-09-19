import math
import random
import subprocess
import sys
from config import latex_jinja_env
from config import formulas_q

q_s = latex_jinja_env.get_template('templates/quadrants/q_sign.tex')



def get_q_sign():
  r_quadrant = random.choice(formulas_q)
  print(r_quadrant)
  return {
    'q': q_s.render(term1=r_quadrant[0], sign1=r_quadrant[1], term2=r_quadrant[2], sign2=r_quadrant[3]),
    'a': 2
  }

