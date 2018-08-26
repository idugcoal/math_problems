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
l10 = rtt.get_tAo1x()
l11 = rtt.get_tAo1B()
l12 = rtt.get_tAo1o2()
l13 = rtt.get_tAo2x()
l14 = rtt.get_tAo2B()
l15 = rtt.get_tAo2o1()
l16 = rtt.get_tBo1x()
l17 = rtt.get_tBo1A()
l18 = rtt.get_tBo1o2()
l19 = rtt.get_tBo2x()
l20 = rtt.get_tBo2A()
l21 = rtt.get_tBo2o1()
l22 = rtt.get_tCo1A()
l23 = rtt.get_tCo1B()
l24 = rtt.get_tCo1o2()
l25 = rtt.get_tCo2A()
l26 = rtt.get_tCo2B()
l27 = rtt.get_tCo2o1()
template = latex_jinja_env.get_template(in_file)
renderedTemplate = template.render(pwidth='5cm', pheight='3cm', 
  l1=l1, l2=l2, l3=l3, l4=l4, l5=l5, l6=l6, l7=l7, l8=l8, l9=l9,
  l10=l10,
  l11=l11, 
  l12=l12,
  l13=l13,
  l14=l14,
  l15=l15,
  l16=l16,
  l17=l17,
  l18=l18,
  l19=l19,
  l20=l20,
  l21=l21,
  l22=l22,
  l23=l23,
  l24=l24,
  l25=l25,
  l26=l26, 
  l27=l27
  )

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
