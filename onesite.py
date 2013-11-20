import sys, time
from ghost import Ghost
from datetime import datetime
from datetime import timedelta

def diff_millis(t0,t1):
  dt = t1 - t0
  ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
  return ms

def main(args):
  js_func = args[0]
  output_file = args[1]
  url = args[2]
  inputs = args[3:]
  print args

  t = []
  t.append(datetime.now())
  ghost = Ghost()
  t.append(datetime.now())
  page, resources = ghost.open(url)
  t.append(datetime.now())
  code = open(js_func + '.js','r').read()
  mycode = code + js_func + '(\"' + '\",\"'.join(inputs) + '\")'
  t.append(datetime.now())
  result, resources = ghost.evaluate(mycode)
  t.append(datetime.now())
  
  print "before", t
  t = [str(diff_millis(t[i],t[i+1])) for i in xrange(len(t)-1)]
  print "after", t

  f = open(output_file, 'a')
  f.write(result + ';' + ';'.join(t) + '\n')
  f.close()
  print result

if __name__ == "__main__":
  main(sys.argv[1:])
