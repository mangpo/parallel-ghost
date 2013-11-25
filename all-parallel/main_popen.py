import csv, subprocess, os, sys
from multiprocessing import Process, Queue
from datetime import datetime
from datetime import timedelta

input_file = "../input.csv"
js_func = "foo"

def run_js(qin):
  print "PID=", os.getpid(), "start."
  sys.stdout.flush()

  try:
    while not qin.empty():
      task = qin.get(timeout=1)
      print "PID=", os.getpid(), "GET:", task
      sys.stdout.flush()
      p = subprocess.Popen(["python", "onesite.py", js_func, output_file] + task)
      p.wait()
  except:
    print "PID=", os.getpid(), "ERROR"
    sys.stdout.flush()

  print "PID=", os.getpid(), "finish."
  sys.stdout.flush()


if __name__ == '__main__':
  # output_file = "output.csv"
  # threads = 4
  output_file = sys.argv[1]
  threads = int(sys.argv[2])

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
    sys.stdout.flush()

  for p in procs:
    p.join()

