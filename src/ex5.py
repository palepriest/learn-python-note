my_name = 'Palepriest'
my_age = 28 # not a lie
my_height = 178 # cm
my_weight = 60 # kg
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'
my_skin = 'Yellow'

print "Let's talk about %s." % my_name
print "He's %d centimeters tall." % my_height
print "He's %d kilograms heavy." % my_weight
print "Actually that's not heavy."
print "He's got %s eyes and %s hair with %s skin." % (my_eyes, my_hair, my_skin)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "IF I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)