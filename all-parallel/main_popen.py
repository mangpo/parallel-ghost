import csv, subprocess, os
from multiprocessing import Process, Queue
from datetime import datetime
from datetime import timedelta

input_file = "../input.csv"
output_file = "output.csv"
js_func = "foo"
threads = 4

def run_js(qin):
  print "PID=", os.getpid(), "start."

  try:
    while not qin.empty():
      task = qin.get(block=False)
      print "PID=", os.getpid(), "GET:", task
      p = subprocess.Popen(["python", "onesite.py", js_func, output_file] + task)
      p.wait()
  except:
    print "PID=", os.getpid(), "ERROR"

  print "PID=", os.getpid(), "finish."


if __name__ == '__main__':
  inputs = csv.reader(open(input_file, 'rb'), delimiter=';')

  f = open(output_file, 'w')
  f.write(';'.join(["title", "start-up", "load", "read-js-file", "execuate"]) + '\n')
  f.close()

  qin = Queue()
  for row in inputs:
    qin.put(row)

  procs = []
  for t in xrange(threads):
    p = Process(target=run_js, args=(qin,))
    p.start()
    procs.append(p)
    print "PID=", p.pid

  for p in procs:
    p.join()

