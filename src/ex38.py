# -*- coding:utf-8 -*-

ten_things = "Apple Oranges Crowds Telephone Light Sugar"
print "Wait! There are not 10 things in list. Let's fixx that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Nigh", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print stuff
print "Let's do something with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])