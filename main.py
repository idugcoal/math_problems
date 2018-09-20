import jinja2
import os
import subprocess
from jinja2 import Template
from config import latex_jinja_env

import rtt
import angles
import arcs
import quadrants

questions_input_file = 'math-template.tex'
answers_input_file = 'answer-template.tex'
math_test = 'math_test'
answer_key = 'answer_key'

# questions = {
  # 30 : rtt.get_tb(),
  # 31 : angles.get_coterminalD(),
  # 33 : angles.get_convertDtoR(),
  # 43 : angles.get_referenceD(),
  # 44 : angles.get_referenceR(),
  # 45 : angles.get_convertDtoR(),
  # 46 : angles.get_convertRtoD(),
# }

questions = []
answers = []

question_set = [
  rtt.get_tABx(),     
  # rtt.get_tABo1(),
  # rtt.get_tABo2(),
  # rtt.get_tBCx(),
  # rtt.get_tBCo1(),
  # rtt.get_tBCo2(),
  # rtt.get_tACx(),
  # rtt.get_tACo1(),
  # rtt.get_tACo2(),
  # rtt.get_tAo1x(),
  # rtt.get_tAo1B(),
  # rtt.get_tAo1o2(),  #extra info
  # rtt.get_tAo2x(),
  # rtt.get_tAo2B(),
  # rtt.get_tAo2o1(),  #extra info
  # rtt.get_tBo1x(),
  # rtt.get_tBo1A(),
  # rtt.get_tBo1o2(),  #extra info
  # rtt.get_tBo2x(),
  # rtt.get_tBo2A(),
  # rtt.get_tBo2o1(),  #extra info
  # rtt.get_tCo1A(),
  # rtt.get_tCo1B(),
  # rtt.get_tCo1o2(),  #extra info
  # rtt.get_tCo2A(),
  # rtt.get_tCo2B(),
  # rtt.get_tCo2o1(),  #extra info
  # rtt.get_gb(),
  quadrants.get_q_sign(),
  rtt.get_rdb(),
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

with open(math_test + '.tex', 'w') as f:
    f.write(renderedQuestions)

cmd = ['pdflatex', '-interaction', 'batchmode', math_test + '.tex']
proc = subprocess.Popen(cmd)
proc.communicate()

retcode = proc.returncode
if not retcode == 0:
    os.unlink(math_test + '.pdf')
    raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd))) 

answer_template = latex_jinja_env.get_template(answers_input_file)
renderedAnswers = answer_template.render(answers=answers)

with open(answer_key + '.tex', 'w') as f:
    f.write(renderedAnswers)

cmd = ['pdflatex', '-interaction', 'batchmode', answer_key + '.tex']
proc = subprocess.Popen(cmd)
proc.communicate()

retcode = proc.returncode
if not retcode == 0:
    os.unlink(answer_key + '.pdf')
    raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd))) 

# os.unlink(math_test + '.tex')
os.unlink(math_test + '.log')
os.unlink(math_test + '.aux')
os.unlink(answer_key + '.tex')
os.unlink(answer_key + '.log')
os.unlink(answer_key + '.aux')
