#!/usr/bin/python2.7
#Filename: break.py

while True:
	s = raw_input('Enter something : ')
	if s == 'quit':
		break
	print 'Length of the string is ', len(s)
else:
	print 'This is in else!'
print 'Done'
