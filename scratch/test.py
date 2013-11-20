from ghost import Ghost

ghost = Ghost()
page, resources = ghost.open('http://www.eecs.berkeley.edu/~mangpo/www/home.html')
print "----------- PAGE -------------"
print page
print "----------- RESOURCE -----------"
print resources

result, resources = ghost.evaluate ('document.URL')
print "----------- RESULT -------------"
print result
result, resources = ghost.evaluate ('document.title')
print "----------- RESULT -------------"
print result
# result, resources = ghost.evaluate ('document.getElementById(\'main\').children[0]') 
result, resources = ghost.evaluate ('document.getElementsByClassName(\'subscribe\')[0].textContent')
print "----------- RESULT -------------"
print result

# print "=========================================="

# page, resources = ghost.open('http://www.google.com/')
# print "----------- PAGE -------------"
# print page
# print "----------- RESOURCE -----------"
# print resources

# result, resources = ghost.evaluate ('document.URL')
# print "----------- RESULT -------------"
# print result
# result, resources = ghost.evaluate ('document.title')
# print "----------- RESULT -------------"
# print result
# result, resources = ghost.evaluate ('document.getElementById(\'gbqfq\')')
# print "----------- RESULT -------------"
# print result


