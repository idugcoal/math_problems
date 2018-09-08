import rtt
import jinja2
import os
import subprocess
from jinja2 import Template
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

in_file = 'math-template.tex'
out_file = 'jinjatest'

answers = {1: "cat", 2: "dog", 3: "kitty", 4: "puppy"}
questions = {
  1 : rtt.get_tABx(),
  2 : rtt.get_tABo1(),
  3 : rtt.get_tABo2(),
  4 : rtt.get_tBCx(),
  5 : rtt.get_tBCo1(),
  6 : rtt.get_tBCo2(),
  7 : rtt.get_tACx(),
  8 : rtt.get_tACo1(),
  9 : rtt.get_tACo2(),
  10 : rtt.get_tAo1x(),
  11 : rtt.get_tAo1B(),
  12 : rtt.get_tAo1o2(),
  13 : rtt.get_tAo2x(),
  14 : rtt.get_tAo2B(),
  15 : rtt.get_tAo2o1(),
  16 : rtt.get_tBo1x(),
  17 : rtt.get_tBo1A(),
  18 : rtt.get_tBo1o2(),
  19 : rtt.get_tBo2x(),
  20 : rtt.get_tBo2A(),
  21 : rtt.get_tBo2o1(),
  22 : rtt.get_tCo1A(),
  23 : rtt.get_tCo1B(),
  24 : rtt.get_tCo1o2(),
  25 : rtt.get_tCo2A(),
  26 : rtt.get_tCo2B(),
  27 : rtt.get_tCo2o1(),
  28 : rtt.get_rdb(),
  29 : rtt.get_gb(),
  30 : rtt.get_tb(),
}
lenny = len(answers) - 1
template = latex_jinja_env.get_template(in_file)
renderedTemplate = template.render(
  # q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, q7=q7, q8=q8, q9=q9,
  # q10=q10, q11=q11, q12=q12, q13=q13, q14=q14, q15=q15, q16=q16, 
  # q17=q17, q18=q18, q19=q19, q20=q20, q21=q21, q22=q22, q23=q23, 
  # q24=q24, q25=q25, q26=q26, q27=q27, q28=q28, q29=q29, q30=q30,
  answers=answers, lenny=lenny, questions=questions)

with open(out_file + '.tex', 'w') as f:
    f.write(renderedTemplate)

cmd = ['pdflatex', '-interaction', 'batchmode', out_file + '.tex']
proc = subprocess.Popen(cmd)
proc.communicate()

retcode = proc.returncode
if not retcode == 0:
    os.unlink(out_file + '.pdf')
    raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd))) 

# os.unlink(out_file + '.tex')
# os.unlink(out_file + '.log')
# os.unlink(out_file + '.aux')
