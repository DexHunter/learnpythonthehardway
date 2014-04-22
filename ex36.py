from sys import exit

def girl_room():
	print "This room is full of pretty girls. Which many do you want to take?"

	next = raw_input(">")
	
	if "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to type numbers!")
		
	if how_much <= 1:
		print "Nice, you saved her life. And you can leave with her now"
		exit(0)
	else:
		dead("You greedy bastard!")
		
def bear_room():
	print """
	There is a beer with a buch of honey.
	And the ugly bear is in front of the door.
	How are you going to move the bear?
	"""
	bear_moved = False
	
	while True:
		next = raw_input(">")
		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif next == "call a dragon" and bear_moved:
			dead("Dragon does not appear and bear is pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			girl_room()
		else:
			print "I got no idea what that means."
			
def dragon_room():
	print "Here you see a dragon lying on the ground."
	print "It seems dragon is sleeping"
	print "What are you going to do next?"
	
	next = raw_input(">")
	
	if "flee" in next:
		start()
	elif "wake dragon up" in next:
		dead("Dragon wakes up and swallows your whole poor body.")
	else:
		dragon_room()
		
def dead(why):
	print why, "Nice done!"
	exit(0)
	
def start():
	print "You are in a dark room."
	print "There is a door to your left and right."
	print "Which one do you take?"
	
	next = raw_input(">")
	
	if next == "left":
		dragon_room()
	elif next == "right":
		bear_room()
	else:
		dead("You stumble around the room until you starve.")
		
start()