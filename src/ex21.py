# -*- coding:utf-8 -*-

def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b

def substract(a, b):
    print "Substract %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Multiply %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "Divide %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

result1 = add(30, 5)
result2 = substract(78, 4)
result3 = multiply(90, 2)
result4 = divide(100, 2)

print '''
30 + 5 = %d
78 - 4 = %d
90 * 2 = %d
100 / 2 = %d
''' % (result1, result2, result3, result4)

# A puzzle for extra credit, type it in anyway
print "Here's puzzle."

puzzle = add(result1, substract(result2, multiply(result3, divide(result4, 2)))) 

print "Result of puzzle is", puzzle, ". Can you do it by hand?"

raw_input("Of course!")

puzzle1 = divide(result4, 2)
puzzle2 = multiply(result3, puzzle1)
puzzle3 = substract(result2, puzzle2)
puzzle4 = add(result1, puzzle3)

print "That becomes:", puzzle4