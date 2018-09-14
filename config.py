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
  1: '(c * m) / 360',
  2: 'c * m - 360',
  3: 'm / (360 * c)',
  4: '360 / (c * m)',
  5: '(2 * math.pi * r * m) / 360',
  6: '(r * m) / 360',
  7: '360 / (2 * math.pi * r * m)',
  8: '(2 * math.pi * r * m) - 360',
  9: '(math.pi * d * m) / 360',
  10: '360 / (math.pi * d * m)',
  11: '(math.pi * d * m) - 360',
  12: '(d * m) / 360',
  13: '(l * 360) / c',
  14: 'c / (l *360)',
  15: '(l * 360) - c',
  16: '(c * 360) / l',
  17: '(l * 360) / (2 * math.pi * r)',
  18: '(2 * math.pi * r) / (l * 360)',
  19: '(l * 360) - (2 * math.pi * r)',
  20: '(l * 360) / r',
  21: '(l * 360) / (math.pi * d)',
  22: '(math.pi * d) / (l * 360)',
  23: '(l * 360) - (math.pi * d)',
  24: '(l * 360) / d',
  25: '(l * 360) / m',
  26: 'm / (l * 360)',
  27: '(l * 360) - m',
  28: '(m * 360) / l',
  29: '(l * 360) / (2 * math.pi * m)',
  30: '(2 * math.pi * m) / (l * 360)',
  31: '(l * 360) - (2 * math.pi * m)',
  32: '(m * 360) / (2 * math.pi * l)',
  33: '(l * 360) / (math.pi * m)',
  35: '(math.pi * m) / (l * 360)',
  35: '(l * 360) - (math.pi * m)',
  36: '(m * 360) / (math.pi * l)'
}