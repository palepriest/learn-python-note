# -*- coding:utf-8 -*-

from sys import argv
# from os.path import exists

# script, from_file, to_file = argv

# print "Copy from %s to % s." % (from_file, to_file)

# indata = open(from_file).read()

# print "The input file is %d bytes long." % len(indata)

# print "Does to_file exists? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input("(Continue/Abort)")

# out_file = open(to_file, 'w').write(indata)

# print "Alright, all done."

# simplify code

script, from_file, to_file = argv

print "Copy from %s to % s." % (from_file, to_file)
open(to_file, 'w').write(open(from_file).read())
print "Alright, all done."

