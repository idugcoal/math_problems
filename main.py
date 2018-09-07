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
q1 = rtt.get_rdb()
# q1 = rtt.get_tABx()
q2 = rtt.get_tABo1()
q3 = rtt.get_tABo2()
q4 = rtt.get_tBCx()
q5 = rtt.get_tBCo1()
q6 = rtt.get_tBCo2()
q7 = rtt.get_tACx()
q8 = rtt.get_tACo1()
q9 = rtt.get_tACo2()
q10 = rtt.get_tAo1x()
q11 = rtt.get_tAo1B()
q12 = rtt.get_tAo1o2()
q13 = rtt.get_tAo2x()
q14 = rtt.get_tAo2B()
q15 = rtt.get_tAo2o1()
q16 = rtt.get_tBo1x()
q17 = rtt.get_tBo1A()
q18 = rtt.get_tBo1o2()
q19 = rtt.get_tBo2x()
q20 = rtt.get_tBo2A()
q21 = rtt.get_tBo2o1()
q22 = rtt.get_tCo1A()
q23 = rtt.get_tCo1B()
q24 = rtt.get_tCo1o2()
q25 = rtt.get_tCo2A()
q26 = rtt.get_tCo2B()
q27 = rtt.get_tCo2o1()
template = latex_jinja_env.get_template(in_file)
renderedTemplate = template.render(
  q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, q7=q7, q8=q8, q9=q9,
  q10=q10, q11=q11, q12=q12, q13=q13, q14=q14, q15=q15, q16=q16, 
  q17=q17, q18=q18, q19=q19, q20=q20, q21=q21, q22=q22, q23=q23, 
  q24=q24, q25=q25, q26=q26, q27=q27)

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
