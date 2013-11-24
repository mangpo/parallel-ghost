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

  f = open(output_file, 'a')
  def wrap():
    t = []
    t.append(datetime.now())
    ghost = Ghost(wait_timeout=10)
    t.append(datetime.now())
    page, resources = ghost.open(url)
    t.append(datetime.now())
    code = open(js_func + '.js','r').read()
    mycode = code + js_func + '(\"' + '\",\"'.join(inputs) + '\")'
    t.append(datetime.now())
    result, resources = ghost.evaluate(mycode)
    t.append(datetime.now())
    
    t = [str(diff_millis(t[i],t[i+1])) for i in xrange(len(t)-1)]

    f.write(result + ';' + ';'.join(t) + '\n')
    print result

  def run():
    #wrap()
    try:
      wrap()
    except:
      print "TIMEOUT", url
      f.write(url + ';timeout\n')
      run()
  
  run()
  f.close()
  

if __name__ == "__main__":
  main(sys.argv[1:])
