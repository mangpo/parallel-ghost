import csv, os
from multiprocessing import Process, Queue
from datetime import datetime
from datetime import timedelta

def run_js(qin, qout):
  from ghost import Ghost

  def diff_millis(t0,t1):
    dt = t1 - t0
    ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
    return ms

  print "PID=", os.getpid(), "start."
  js_func = "foo"

  while not qin.empty():
    task = qin.get(block=False)
    print "GET:", task
    url = task[0]
    inputs = task[1:]
    
    print "PID=", os.getpid(), url, datetime.now()
      
    try:
      t = []
      t.append(datetime.now())
      #print "init ghost"
      ghost = Ghost(wait_timeout=10)
      t.append(datetime.now())
      print "PID=", os.getpid(), "load page"
      page, resources = ghost.open(url)
      t.append(datetime.now())
      #print "load js"
      code = open(js_func + '.js','r').read()
      mycode = code + js_func + '(\"' + '\",\"'.join(inputs) + '\")'
      t.append(datetime.now())
      print "PID=", os.getpid(), "run js"
      result, resources = ghost.evaluate(mycode)
      print "PID=", os.getpid(), "done", url, result
      t.append(datetime.now())
      
      t = [str(diff_millis(t[i],t[i+1])) for i in xrange(len(t)-1)]
      
      qout.put(result + ';' + ';'.join(t) + '\n')
    except:
      print "PID=", os.getpid(),url, "TIMEOUT!!!!"
      qout.put(url + ';timeout\n')
      qin.put(task)
      print "PUT:", task
      print "PID=", os.getpid(), "QUEUE", qin.empty()

  print "PID=", os.getpid(), "finish."


if __name__ == '__main__':
  input_file = "input.csv"
  output_file = "output.csv"
  threads = 4

  inputs = csv.reader(open(input_file, 'rb'), delimiter=';')

  qout = Queue()
  qin = Queue()
  for row in inputs:
    qin.put(row)

  procs = []
  for t in xrange(threads):
    p = Process(target=run_js, args=(qin,qout))
    p.start()
    procs.append(p)

  for p in procs:
    p.join()

  f = open(output_file, 'w')
  f.write(';'.join(["title", "start-up", "load", "read-js-file", "execuate"]) + '\n')
  while not qout.empty():
    f.write(qout.get())
  f.close()
