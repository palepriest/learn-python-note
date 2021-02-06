# -*- coding:utf-8 -*-

t_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'bananas', 'Blueberries', 'oranges']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# print a integer list
for number in t_count:
    print "The number is %d." % number

# print a string list
for fruit in fruits:
    print "The fruit type is %s." % fruit

# print a multi-type list
for i in change:
    print "I got %r." % i

elements = []
# use the range function to construcr a list
for i in range(0, 6):
    print "Add %d into elements list." % i
    elements.append(i)

# the print them out
for element in elements:
    print "The element is %d." % element