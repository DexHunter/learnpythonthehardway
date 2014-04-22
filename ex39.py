states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)