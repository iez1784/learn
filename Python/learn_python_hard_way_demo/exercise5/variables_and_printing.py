#!/usr/bin/ python
# -*-coding:utf-8 -*-

my_name = 'Zed A. Shaw'
my_age = 35  # not a lie
my_height = 74  # inches
my_weight = 180  # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)

print " "
###############################################################################
# Study Drills

# Change all the variables so there is no my_ in front of each one.
# Make sure you change the name everywhere, not just where you used = to set them.
name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print " "
# Try to write some variables that convert the inches and pounds to centimeters
# and kilograms. Do not just type in the measurements. Work out the math in Python.
name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

height_trans = height * 2.54  # trans to cm
weight_trans = weight * 0.4536  # trans to kg

print "Let's talk about %s." % name
print "He's %d cm tall." % height_trans
print "He's %d kg heavy." % weight_trans
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %d." % (age, height_trans, weight_trans, age + height_trans + weight_trans)

print " "

# Search online for all of the Python format characters.
# Try more format characters. %r is a very useful one. It's like saying "print this no matter what."
name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

height_trans = height * 2.54  # trans to cm
weight_trans = weight * 0.4536  # trans to kg

print "Let's talk about %r." % name
print "He's %r cm tall." % height_trans
print "He's %r kg heavy." % weight_trans
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right

print "If I add %r, %r, and %r I get %r." % (age, height_trans, weight_trans, age + height_trans + weight_trans)

# 个人理解，%r，是对所替换的值的原味体现，如果是字符串会加上''，如果是数字，float型的，也会保留
