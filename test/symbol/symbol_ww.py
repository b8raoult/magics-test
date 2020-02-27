# (C) Copyright 1996-2016 ECMWF.
# 
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0. 
# In applying this licence, ECMWF does not waive the privileges and immunities 
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.

# importing Magics module

from Magics.macro import *

ref = 'symbol_ww'

# Setting of the output file name

output = output(output_formats=['png', "ps"],
                output_name_first_page_number='off',
                output_name=ref)

# Setting the coordinates of the geographical area
# Here we use Europe

area = mmap(subpage_map_projection='cartesian',
		subpage_frame='off', 
        subpage_x_max=100.,
        subpage_x_min=0.,
        subpage_y_max=120.,
        subpage_y_min=0.,
        page_y_length= 21.,
        subpage_y_length= 21.)
        
lines = ['Symbol List', "<font size='0.5'> Present Weather symbols</font>", ""]

text = mtext(text_lines=  lines,
    text_html= 'true',
    text_justification= 'centre',
    text_font_size= 1.,
    text_colour= 'charcoal',
    )

lines2 = ['Symbol List', "<font size='0.5'> Cloud symbols</font>", ""]

text2 = mtext(text_lines=  lines2,
    text_html= 'true',
    text_justification= 'centre',
    text_font_size= 1.,
    text_colour= 'charcoal',
    )
    
out = []

for p in range(0,9,2) :
	out.append(area)
	#list.append(title)
	y = 100.
	x = 30.
	sizes = [1.,]

	for i in range(0,20) :
		
		if (i % 10) == 0:
			y = 100.
			x += 45.
			
		if (i % 20) == 0:
			y = 100.
			x = 30.
			out.append(page())
			out.append(area)  
			out.append(text)     
			
			
		name = "ww_%02d" % ( i + p*10)
		#print name			
		#symbol = "symbol = %s"% name

		xx = x
		for size in sizes:
			title = "symbol = %s"% name
		# Import the input data
			out.append(minput(input_x_values=[xx],
					input_y_values=[y],
				))

		# Define the symbol plotting
			out.append(msymb(
				legend='off',
				symbol_type='marker',
				symbol_colour='evergreen',
				symbol_height=size,
				symbol_marker_mode = "name",
				symbol_marker_name = name,
				symbol_text_position='left',
				symbol_text_font_size=0.5,
				symbol_text_font_colour='black',
				symbol_text_list=[title],
				symbol_outline="off",
				symbol_outline_colour="navy",
				symbol_outline_thickness=3,
				))
			xx+=15
		y -= 10. 
	out.append(page())

#
#
#   C L O U D S   ...
#
out.append(page())
out.append(area)  
out.append(text2)     

xxx=15.
clouds = ['N','W','CL','CM','CH','C','a','DS']
for c in clouds:
	for i in range(0,10):
		name = c+"_%d" % i

		out.append(minput(input_x_values=[xxx],
					input_y_values=[115.-(i*10.)],
				))
		# Define the symbol plotting
		out.append(msymb(
			legend='off',
			symbol_type='marker',
			symbol_colour='evergreen',
			symbol_height=size,
			symbol_marker_mode = "name",
			symbol_marker_name = name,
			symbol_text_position='left',
			symbol_text_font_size=0.5,
			symbol_text_font_colour='black',
			symbol_text_list=[name],
			symbol_outline="off",
			symbol_outline_colour="navy",
			symbol_outline_thickness=3,
			))
	xxx+=10.

		
# To the plot

plot( output,  out)

