# -*- coding:utf-8 -*-

# create a mapping of status to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL':'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print some cities
print '-' * 10
print "NY State has cities: ", cities['NY']
print "FL State has cities: ", cities['FL']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Oregon's abbreviation is: ", states['Oregon']

# print cities in state.
print '-' * 10
print "Michigan has cities: ", cities[states['Michigan']]
print "Oregon has cities: ", cities[states['Oregon']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreniated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for state, city in cities.items():
    print "%s has the city %s" % (state, city)

# now do both at same time
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s and has the city %s" % (
        state, abbrev, cities[abbrev])

# safely get a abbreviation by state that might not be there
print '-' * 10
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX')
print "The city in state 'TX' is: %s" % city
