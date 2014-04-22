from sys import argv

script, user_name, user_gender = argv
prompt = ' So your decision is: '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "You are a %s, and do you like girls?" % user_gender
girls = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
Yo live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)