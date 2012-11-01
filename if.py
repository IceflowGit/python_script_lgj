#!/usr/bin/python2.7
#Filename:if.py

number = 23
guess = int(raw_input('Enter an integer : '))

if guess == number:
	print 'Congratulations, you gressed it.'
	print '(but you do not win any prizes!)'
elif guess < number:
	print 'No, it is a little higher than that!'
else:
	print 'No, it is a little lower than that'
print 'Done'
