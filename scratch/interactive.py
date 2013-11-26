from ghost import Ghost

js_file = "foo.js"

try:
  ghost = Ghost(wait_timeout=99)
  page1, resources = ghost.open('http://www.eecs.berkeley.edu/~mangpo/www/interest.html')

  code = open(js_file,'r').read()
  result1, resources = ghost.evaluate('document.URL')
  print result1
  page2, resources = ghost.evaluate(code + 'foo()', expect_loading=True)
  result2, resources = ghost.evaluate('document.URL')
  print result2
except UnicodeEncodeError as e2:
  print "Unicode Error"
  print e2.args
except Exception as e:
  print "Other Error"
  print e.args


# Exception(timeout_message)
