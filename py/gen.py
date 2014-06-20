import random

for i in range(0, 73):
  print '    - set_fact: %s=%d' % (''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(0, 12)]), random.randint(1,100))
