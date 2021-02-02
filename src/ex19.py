# -*- coding:utf-8 -*-

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheese." %cheese_count
    print "You have %d boxes of crackers." % boxes_of_crackers
    print "Man, that's enough for a party！"
    print "Get a blanket.\n"

# We can directy give value
cheese_and_crackers(20, 30)

# Or, use variables
cheese_count = 20
boxes_of_crackers = 30
cheese_and_crackers(cheese_count, boxes_of_crackers)

# do some math is ok
cheese_and_crackers(20 + 10, 30 + 10)

# combine variables with some math
cheese_and_crackers(cheese_count + 100, boxes_of_crackers + 1000)