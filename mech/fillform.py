#!/usr/bin/env python

import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.open('https://palazzo.parkingattendant.com/')

#response = br.response()

#print response.geturl() # URL of the page we just opened
#print response.info()   # headers
#print response.read()   # body

forms =  br.forms()
for form in forms:
    print "forms",form
