import sys, time
from ghost import Ghost

def main(args):
  js_func = args[0]
  output_file = args[1]
  url = args[2]
  inputs = args[3:]

  print "start ..."
  # time.sleep(1)
  ghost = Ghost()
  page, resources = ghost.open(url)
  code = open(js_func + '.js','r').read()
  mycode = code + js_func + '(\"' + '\",\"'.join(inputs) + '\")'
  result, resources = ghost.evaluate(mycode)

  f = open(output_file, 'a')
  f.write(result+'\n')
  f.close()
  print result

if __name__ == "__main__":
  main(sys.argv[1:])
