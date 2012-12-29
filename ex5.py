my_name = 'Renyu Liu'
my_age = 18 # it is a lie
my_height = 181 # cm
my_weight = 60 # kg
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "He's %d cm tall." % my_height
print "He's %d kg heavy." % my_weight
print "Actually that's underweight."
print "He's got %s eys and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffe." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)