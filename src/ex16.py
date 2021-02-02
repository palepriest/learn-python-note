# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print "We're goig erase %r." % filename
print "If you don't that, hit CTR:-C(^C)"
print "If you want that, RETURN"

raw_input("?")

print "Opening the file..."
target  = open(filename, 'w')

print "Trubcating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for 3 lines."

line1 = raw_input("line1: ")
line2 = raw_input("line1: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "And finally, we close it."
target.close()

# cannnot write and read target at the same time.
target  = open(filename, 'r')
print "Here's the content of %r:" % filename
print target.read()
target.close()