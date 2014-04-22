from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

second = int(raw_input("What do you like?"))
print "So, you like %r." % second