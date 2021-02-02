# -*- coding:utf-8 -*-

# this one is like your sccript with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r." % (arg1, arg2)

# don't think args is pointless
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r." % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r." % arg1

# this one takes no argument
def print_none():
    print "I got nothing."

print_two("Pale", "Priest")
print_two_again("Pale", "Priest")
print_one("palepriest")
print_none()