import csv
from ghost import Ghost

ghost = Ghost()

inputs = csv.reader(open('input.csv', 'rb'), delimiter=';')
code = open('foo.js','r').read()

for row in inputs:
  page, resources = ghost.open(row[0])
  mycode = code + 'foo(\"' + '\",\"'.join(row[1:]) + '\")'
  result, resources = ghost.evaluate(mycode)
  print result
