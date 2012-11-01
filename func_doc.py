#!/usr/bin/python
#Filename:func_doc.py

def printMax(x, y):
	'''prints the maximum of two numbers
	The two values must be integers.'''
	x = int(x)
	y = int(y)

	if x>y:
		print x,'is muximum'
	else:
		print y, 'is muximum'

printMax(3, 5)
print printMax.__doc__
help(printMax)
