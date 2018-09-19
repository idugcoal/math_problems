import math
import random
import subprocess
import sys
from config import latex_jinja_env
from config import formulas_q

q_s = latex_jinja_env.get_template('templates/quadrants/q_sign.tex')

def get_q_sign():
  r_answer = random.randint(0, len(formulas_q))
  r_quadrant = formulas_q[r_answer]
  r_question = random.choice(r_quadrant)
  answers = ['Quadrant I', 'Quadrant II', 'Quadrant III', 'Quadrant IV',]
  answer = answers[r_answer]
  random.shuffle(answers)
  print(r_quadrant)
  return {
    'q': q_s.render(term1=r_question[0], sign1=r_question[1], term2=r_question[2], sign2=r_question[3], answers=answers),
    'a': answer
  }

