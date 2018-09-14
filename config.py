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
    1: 'c * m - 360',
    2: 'm / (360 * c)',
    3: '360 / (c * m)',
  },
  'rml': {
    1: '(r * m) / 360',
    2: '360 / (2 * math.pi * r * m)',
    3: '(2 * math.pi * r * m) - 360',
  },
  'dml': {
    1: '360 / (math.pi * d * m)',
    2: '(math.pi * d * m) - 360',
    3: '(d * m) / 360',
  },
  'lcm': {
    1: 'c / (l *360)',
    2: '(l * 360) - c',
    3: '(c * 360) / l',
  },
  'lrm': {
    1: '(2 * math.pi * r) / (l * 360)',
    2: '(l * 360) - (2 * math.pi * r)',
    3: '(l * 360) / r',
  },
  'ldm': {
    1: '(math.pi * d) / (l * 360)',
    2: '(l * 360) - (math.pi * d)',
    3: '(l * 360) / d',
  },
  'lmc': {
    1: 'm / (l * 360)',
    2: '(l * 360) - m',
    3: '(m * 360) / l',
  },
  'lmr': {
    1: '(2 * math.pi * m) / (l * 360)',
    2: '(l * 360) - (2 * math.pi * m)',
    3: '(m * 360) / (2 * math.pi * l)',
  },
  'lmd': {
    1: '(math.pi * m) / (l * 360)',
    2: '(l * 360) - (math.pi * m)',
    3: '(m * 360) / (math.pi * l)'
  }
}