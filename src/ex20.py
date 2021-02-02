# -*- coding:utf-8 -*-

from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)
total_line = len(current_file.readlines())
current_line = 1

print "First, print all the file:\n"
rewind(current_file)
print_all(current_file)

print "Then, print every line:\n"
rewind(current_file)
while current_line <= total_line:
    print_a_line(current_line, current_file)
    current_line += 1