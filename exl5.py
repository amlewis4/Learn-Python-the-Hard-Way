her_name = 'Ari Lewis'
her_age = 19
her_height = 74
her_weight = 172
her_eyes = 'Brown'
her_teeth = 'White'
her_hair = 'Black'

print "Let's talk about %s."  % her_name
print "He's %d inches tall." % her_height
print "He's %d pounds heavy." % her_weight
print "Actually that's not too heavy." 
print "He's got %s eyes and %s hair." % (her_eyes, her_hair)
print "His teeth are usually %s depending on the coffee." % her_teeth

# this line is tricky, try to get it exactly right

print "If I  add %d, %d, and %d I get %d." % (
	her_age, her_height, her_weight, her_age + her_height + her_weight)