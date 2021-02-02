# -*- coding:utf-8 -*-

from sys import argv

script, user_name = argv
prompt = '> '

print "Hello %s, I'm %s script." % (user_name, script)
print "I'd ask you same questoins."
print "which role do you paly in wow, %s?" % user_name
role = raw_input(prompt)

print "which race do you select, %s?" % user_name
race = raw_input(prompt)

print "Last question, what kind of pc do you have?"
computer = raw_input(prompt)

print '''
Alright, we know that you use %r computer to 
play the role of %r in the World of Warcraft.
And the \'%r\' character looks realy beautiful.
''' % (computer, role, race)