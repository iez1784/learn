#!/usr/bin/ python
# -*-coding:utf-8 -*-

# 10 instead the bit of %d, use numbers
x = "There are %d types of people." % 10
# let binary's value equal "binary"
binary = "binary"

# let do_not 's value equal "don't"
do_not = "don't"

# use binary, do_not instead the bits %s, %s
y = "Those who know %s and those who %s." % (binary, do_not)

# print x's value
print x

# print y's value
print y

# print , and use x's value instead bit of %r
print "I said: %r." % x

# print , and use y's value instead bit of %r
print "I also said: '%s'." % y

# let hilarious's value equal False
hilarious = False

# let joke_evaluation's value equal Isn't that joke so funny?! %r
joke_evaluation = "Isn't that joke so funny?! %r"

# print, and use hilarious instead of bit of %r in joke_evaluation's %r
print joke_evaluation % hilarious

# let w's value equal This is the left side of ...
w = "This is the left side of..."

# let e's value equal a string with a right side.
e = "a string with a right side."

# print w and e, this can use w.join(e)
print w + e

