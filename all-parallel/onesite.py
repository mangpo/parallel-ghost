import sys, time, os, sys
from ghost import Ghost
from datetime import datetime
from datetime import timedelta

## Unomment out print & sys.stdout.flush() to log activities

def diff_millis(t0,t1):
  dt = t1 - t0
  ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
  return ms

def main(args):
  js_func = args[0]
  output_file = args[1]
  url = args[2]
  inputs = args[3:]
  # print args, "id=", os.getpid()
  # sys.stdout.flush()

  def wrap():
    t = []
    t.append(datetime.now())
    ghost = Ghost(wait_timeout=60)
    t.append(datetime.now())
    page, resources = ghost.open(url)
    t.append(datetime.now())
    code = open(js_func + '.js','r').read()
    mycode = code + js_func + '(\"' + '\",\"'.join(inputs) + '\")'
    t.append(datetime.now())
    result, resources = ghost.evaluate(mycode)
    t.append(datetime.now())
    
    t = [str(diff_millis(t[i],t[i+1])) for i in xrange(len(t)-1)]
    # print "TITLE:", result, "[", url, "]"
    # sys.stdout.flush()
    return result + ';' + ';'.join(t) + '\n'

  def run():
    try:
      return wrap()
    except Exception as e:
      if len(e.args) > 0 and e.args[0] == "Unable to load requested page":
        # print "TIMEOUT:", url
        # sys.stdout.flush()
        return url + ';timeout\n'
      else:
        # print "ERROR:", url
        # sys.stdout.flush()
        return url + ';error\n'
        
  row = run()
  f = open(output_file, 'a')
  f.write(row)
  f.close()
  # print "id=", os.getpid(), "finish (onesite)."
  # sys.stdout.flush()
  

if __name__ == "__main__":
  main(sys.argv[1:])
