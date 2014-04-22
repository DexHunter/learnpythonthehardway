from sys import argv # import argument variable

script, filename = argv # unpack the argument variable

txt = open(filename) 

print "Here's your file %r:" % filename # use formatter to replace its value with variable the right
print txt.read()
txt.close()

print "Type the filename again:"
file_again = filename

txt_again = open(file_again)


print txt_again.read()

txt_again.close()