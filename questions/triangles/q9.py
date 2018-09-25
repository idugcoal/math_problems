import random
from config import latex_jinja_env

r_db = latex_jinja_env.get_template('templates/rectangles/r_db.tex')

def get_q9():
  answers = {1: 67, 2: 68, 3: 69, 4: 70}
  name = ['Doug', 'Dustin',]
  name_action = ['is starting', 'is beginning', 'is following', 'has started', 'is commencing', 'commences']
  program = ['training program', 'training regimen', 'workout program', 'workout regimen', 'exercise program', 'exercise regimen', 'running regimen', 'running program', 'fitness program', 'fitness regimen', 'cardio training program', 'cardio training regimen', 'cardio workout program', 'cardio workout regimen', 'cardio exercise program', 'cardio exercise regimen', 'cardio running regimen', 'cardio running program', 'cardio fitness program', 'cardio fitness regimen']
  frequency = ['Every Monday', 'Every Tuesday', 'Every Wednesday', 'Every Thursday', 'Every Friday', 'Every Saturday', 'Every Sunday']
  move = ['runs', 'sprints', 'jogs']
  location = ['court', 'field', 'track']
  length = random.randint(68, 100)
  unit = ['feet', 'yards', 'meters']
  width = random.randint(28, 56)
  start = ['starts', 'begins']
  point = ['corner', 'point', 'spot']
  path = ['pattern', 'path', 'combination', 'route']
  end = ['completes', 'finishes', 'runs']
  num = random.randint(3, 20)
  total = ['cover', 'run', 'travel']
  final = ['in total', 'altogether', 'overall']
  return {
    'q': r_db.render(w=8.6, h=5.2, t=3, 
      answers= answers,
      name = random.choice(name),
      name_action = random.choice(name_action),
      program = random.choice(program),
      frequency = random.choice(frequency),
      move = random.choice(move),
      location = random.choice(location),
      length = length,
      unit = random.choice(unit),
      width = width,
      start = random.choice(start),
      point = random.choice(point),
      path = random.choice(path),
      end = random.choice(end),
      num = num,
      total = random.choice(total),
      final = random.choice(final),
      ),
    'a': answers
  }