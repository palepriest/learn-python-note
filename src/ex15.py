from sys import argv

# use 'argv' get filename
script, filename = argv
txt = open(filename)
print "Here's your file %r:" % filename
print txt.read()
txt.close()

# use 'raw_input' get filname
file_again = raw_input("Type the filename again:")
txt_again = open(file_again)
print txt_again.read()
txt_again.close()