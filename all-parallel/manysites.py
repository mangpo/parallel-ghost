import csv, subprocess, os
import onesite

parallel = True
input_file = "input.csv"
output_file = "output.csv"
js_func = "foo"

inputs = csv.reader(open(input_file, 'rb'), delimiter=';')

f = open(output_file, 'w')
f.write(';'.join(["title", "start-up", "load", "read-js-file", "execuate"]) + '\n')
f.close()

if parallel:
  procs = []
  for row in inputs:
    procs.append(subprocess.Popen(["python", "onesite.py", js_func, output_file] + row))

  for proc in procs:
    result = proc.wait()

else:
  for row in inputs:
    onesite.main([js_func, output_file] + row)
