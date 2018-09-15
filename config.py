import os
import jinja2
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

formulas_al = {
  'cml': {
    0: '(c * m) / 360',
    1: 'c * m - 360',
    2: 'm / (360 * c)',
    3: '360 / (c * m)',
  },
  'rml': {  
    0: '(2 * math.pi * r * m) / 360',
    1: '(r * m) / 360',
    2: '360 / (2 * 3.1415 * r * m)',
    3: '(2 * 3.1415 * r * m) - 360',
  },
  'dml': {
    0: '(math.pi * d * m) / 360',
    1: '360 / (3.1415 * d * m)',
    2: '(3.1415 * d * m) - 360',
    3: '(d * m) / 360',
  },
  'lcm': {
    0: '(l * 360) / c',
    1: 'c / (l *360)',
    2: '(l * 360) - c',
    3: '(c * 360) / l',
  },
  'lrm': {
    0: '(l * 360) / (2 * math.pi * r)',
    1: '(2 * 3.1415 * r) / (l * 360)',
    2: '(l * 360) - (2 * 3.1415 * r)',
    3: '(l * 360) / r',
  },
  'ldm': {
    0: '(l * 360) / (math.pi * d)',
    1: '(3.1415 * d) / (l * 360)',
    2: '(l * 360) - (3.1415 * d)',
    3: '(l * 360) / d',
  },
  'lmc': {
    0: '(l * 360) / m',
    1: 'm / (l * 360)',
    2: '(l * 360) - m',
    3: '(m * 360) / l',
  },
  'lmr': {
    0: '(l * 360) / (2 * math.pi * m)',
    1: '(2 * 3.1415 * m) / (l * 360)',
    2: '(l * 360) - (2 * 3.1415 * m)',
    3: '(m * 360) / (2 * 3.1415 * l)',
  },
  'lmd': {
    0: '(l * 360) / (math.pi * m)',
    1: '(3.1415 * m) / (l * 360)',
    2: '(l * 360) - (3.1415 * m)',
    3: '(m * 360) / (3.1415 * l)'
  }
}