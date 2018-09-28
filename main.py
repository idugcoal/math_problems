import jinja2
import os
import subprocess
import sys
from jinja2 import Template
from config import latex_jinja_env

import rtt
import angles
import arcs
import quadrants
import questions.triangles.q1 as q1
import questions.triangles.q9 as q9
import questions.triangles as triangles
print(triangles)

questions_input_file = '/templates/exam/math-template.tex'
answers_input_file = '/templates/exam/answer-template.tex'
math_test = 'math_test'
answer_key = 'answer_key'

questions = []
answers = []

question_set = [
  # rtt.get_tb(),
  # rtt.get_gb(),
  # q9.get_q9(),
  # rtt.get_finding_trig_ratio(), 
  # angles.get_coterminalD(),
  # angles.get_convertDtoR(),
  # angles.get_referenceD(),
  # angles.get_referenceR(),
  # angles.get_convertRtoD(),
  # angles.get_convertDtoR(),
  # quadrants.get_q_sign(),
  # q1.get_tABx(),    
  # q1.get_tABo1(),
  # q1.get_tABo2(),
  # q1.get_tBCx(),
  # q1.get_tBCo1(),
  # q1.get_tBCo2(),
  # q1.get_tACx(),
  # q1.get_tACo1(),
  # q1.get_tACo2(),
  # q1.get_tAo1x(),
  # q1.get_tAo1B(),
  # q1.get_tAo1o2(),  #extra info
  # q1.get_tAo2x(),
  # q1.get_tAo2B(),
  # q1.get_tAo2o1(),  #extra info
  # q1.get_tBo1x(),
  # q1.get_tBo1A(),
  # q1.get_tBo1o2(),  #extra info
  # q1.get_tBo2x(),
  # q1.get_tBo2A(),
  # q1.get_tBo2o1(),  #extra info
  # q1.get_tCo1A(),
  # q1.get_tCo1B(),
  # q1.get_tCo1o2(),  #extra info
  # q1.get_tCo2A(),
  # q1.get_tCo2B(),
  # q1.get_tCo2o1(),  #extra info
  arcs.get_al_cml(),
  arcs.get_al_rml(),
  arcs.get_al_dml(),
  arcs.get_al_lcm(),
  arcs.get_al_lrm(),
  arcs.get_al_ldm(),
  arcs.get_al_lmc(),
  arcs.get_al_lmr(),
  arcs.get_al_lmd(),
]

for current_question in question_set:
  q = current_question['q']
  a = current_question['a']
  questions.append(q)
  answers.append(a)


question_template = latex_jinja_env.get_template(questions_input_file)
renderedQuestions = question_template.render(questions=questions)
answer_template = latex_jinja_env.get_template(answers_input_file)
renderedAnswers = answer_template.render(answers=answers)

with open(math_test + '.tex', 'w') as f:
    f.write(renderedQuestions)
cmd = ['pdflatex', '-interaction', 'batchmode', math_test + '.tex']
proc = subprocess.Popen(cmd)
proc.communicate()

retcode = proc.returncode
if not retcode == 0:
    os.unlink(math_test + '.pdf')
    raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd))) 

# with open(answer_key + '.tex', 'w') as f:
#     f.write(renderedAnswers)

# cmd = ['pdflatex', '-interaction', 'batchmode', answer_key + '.tex']
# proc = subprocess.Popen(cmd)
# proc.communicate()

# retcode = proc.returncode
# if not retcode == 0:
#     os.unlink(answer_key + '.pdf')
#     raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd))) 

os.unlink(math_test + '.tex')
os.unlink(math_test + '.log')
os.unlink(math_test + '.aux')
# os.unlink(answer_key + '.tex')
# os.unlink(answer_key + '.log')
# os.unlink(answer_key + '.aux')
