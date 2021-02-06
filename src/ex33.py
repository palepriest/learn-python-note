# -*- coding:utf-8 -*-

i = 0
numbers = []

while i < 6:
    print "Add %d to numbers," % i
    numbers.append(i)
    
    print "Number now is ", numbers
    i = i + 1

print "numbers: "
for num in numbers:
    print num