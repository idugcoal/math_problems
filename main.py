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
# l1 = rtt.getL1()
# l2 = rtt.getL2()
l1 = rtt.get_tABx()
l2 = rtt.get_tABo1()
l3 = rtt.get_tABo2()
l4 = rtt.get_tBCx()
l5 = rtt.get_tBCo1()
l6 = rtt.get_tBCo2()
l7 = rtt.get_tACx()
l8 = rtt.get_tACo1()
l9 = rtt.get_tACo2()
template = latex_jinja_env.get_template(in_file)
renderedTemplate = template.render(pwidth='5cm', pheight='3cm', l1=l1, l2=l2, l3=l3, l4=l4, l5=l5, l6=l6, l7=l7, l8=l8, l9=l9)

with open(out_file + '.tex', 'w') as f:
    f.write(renderedTemplate)

cmd = ['pdflatex', '-interaction', 'batchmode', out_file + '.tex']
proc = subprocess.Popen(cmd)
proc.communicate()

retcode = proc.returncode
if not retcode == 0:
    os.unlink(out_file + '.pdf')
    raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd))) 

os.unlink(out_file + '.tex')
os.unlink(out_file + '.log')
os.unlink(out_file + '.aux')
