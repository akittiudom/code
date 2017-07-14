#!/usr/bin/env python

import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.open('https://palazzo.parkingattendant.com/8sO6QCksIkiQnh51a_0bkw/permits/temporary/new')

#response = br.response()

#print response.geturl() # URL of the page we just opened
#print response.info()   # headers
#print response.read()   # body

forms =  br.forms()
for form in forms:
    print "FORM:",form
    controls = form.controls
    for control in controls:
        print "CONTROL:",control
        print "   type:",control.type
    print
    print

duration = form[1].find_control("duration value")
print "duration control:",duration

#def select_form(form):
#    return form.attrs.get('class',None) == 'new permit ready'

#br.select_form(predicate=select_form)
#print br.form

#form = select_form()
#print form

# form0 = forms[0]
# form1 = forms[1]
# form2 = forms[2]
# form3 = forms[3]

# formx=form1

# vehicle = formx.find_control('vehicle')
# print "Vehicle:",vehicle,"is from form:",formx
# print 
# print
# formx['tenant']='765 GARDEN ST'
# formx['vehicle']='THIS VEHICLE'
# formx['email']='EMAIL YO'
# formx['tel']='235352235'
# print formx
# print 
# print
# print 
# for control in formx.controls:
#     print "CONTROL:",control
