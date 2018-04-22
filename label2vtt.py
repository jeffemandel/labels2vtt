#!/opt/local/bin/python

import datetime
import fileinput


d0=datetime.datetime.fromtimestamp(0)

print "WEBVTT\n"
for my_line in fileinput.input():
	my_strings = my_line.split('\t')
	d=d0 + datetime.timedelta(seconds=float(my_strings[0]))
	d1=d0 + datetime.timedelta(seconds=float(my_strings[1]))
	print d.strftime('%M:%S.%f')[:-3] + " --> " + d1.strftime('%M:%S.%f')[:-3]
	print my_strings[2]
