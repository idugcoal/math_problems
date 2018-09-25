import math
import random
import subprocess
import sys
from config import latex_jinja_env
from config import formulas_a
from config import pythag_triples
from config import formulas_ftr
from config import questions_ftr


g_b = latex_jinja_env.get_template('templates/graphs/blank.tex')
t_b = latex_jinja_env.get_template('templates/tables/blank.tex')

# def get_tb():
#   return t_b.render(i1=1,i2=2,i3=3,i4=4,i5=5,i6=6,o1=-2,o2=0,o3=4,o4=10,o5=18,o6=28)
# def get_gb():
#   return {
#   'q': g_b.render(n=-5, d=3),
#   'a': 20
#   }



def get_finding_trig_ratio():
  p_triple = random.choice(pythag_triples)
  multiplier = random.randint(p_triple['multi_range']['min'], p_triple['multi_range']['max'])
  a = p_triple['a'] * multiplier 
  b = p_triple['b'] * multiplier
  c = p_triple['c'] * multiplier
  formula = formulas_ftr[1]
  question = random.choice(questions_ftr)
  answer_options = question['answer_options']
  prompt = question['prompt']
  # answers = get_options(formulas=formulas_ftr,)
  print(answer_options)
  answers = [

  ]
  return {
    'q': t_x.render(a=a, b=b, c=c, answers=answers, w=a, h=b, scale=0.2, prompt=prompt),
    'a': answers
  }




