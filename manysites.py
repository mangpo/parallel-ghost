import csv
import subprocess, os

input_file = "input.csv"
output_file = "output.out"
js_func = "foo"

inputs = csv.reader(open(input_file, 'rb'), delimiter=';')
os.system("rm " + output_file)

procs = []
for row in inputs:
  procs.append(subprocess.Popen(["python", "onesite.py", js_func, output_file] + row))

for proc in procs:
  result = proc.wait()
