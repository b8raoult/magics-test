# (C) Copyright 1996-2016 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.


# importing Magics module
from Magics.macro import *


ref = "frame"
# Setting of the output file name
output = output(
    output_formats=["png"], output_name_first_page_number="off", output_name=ref
)

# Setting the cartesian view
projection = mmap(
    subpage_map_projection="cartesian",
    page_frame="on",
    page_frame_colour="navy",
    page_frame_line_style="dash",
    page_frame_thickness=6,
    page_id_line="off",
    super_page_frame="on",
    super_page_frame_colour="red",
    super_page_frame_line_style="chain_dash",
    super_page_frame_thickness=7,
    layout="positional",
    page_x_position=2.0,
    page_y_position=2.0,
    page_x_length=25.0,
    page_y_length=18.0,
    subpage_frame_colour="evergreen",
    subpage_frame_line_style="dot",
    subpage_frame_thickness=5,
    subpage_x_axis_type="regular",
    subpage_y_axis_type="regular",
    subpage_x_min=-20.0,
    subpage_x_max=20.0,
    subpage_y_min=25.0,
    subpage_y_max=75.0,
)

# Vertical axis
vertical = maxis(
    axis_orientation="vertical",
    axis_grid="on",
    axis_grid_colour="grey",
    axis_grid_thickness=1,
    axis_grid_line_style="dot",
)

# Horizontal axis
horizontal = maxis(
    axis_orientation="horizontal",
    axis_grid="on",
    axis_grid_colour="grey",
    axis_grid_thickness=1,
    axis_grid_line_style="dot",
)


# define  the  data
x = numpy.array([-15.0, 0.0, 15.0])
y = numpy.array([50.0, 30.0, 50.0])

# define the input data
input = minput(input_x_values=x, input_y_values=y)

# Define the graph
graph = mgraph(
    graph_line_colour="red",
    graph_line_thickness=8,
    graph_symbol="on",
    legend="on",
    legend_user_text="<font colour='red'> My red curve </font>",
    graph_symbol_marker_index=15,
    graph_symbol_colour="black",
    graph_symbol_height=1.0,
)


title = mtext(
    text_lines=["Simple Graph with legend"],
    text_justification="left",
    text_font_size=1.0,
    text_colour="charcoal",
)


# To the plot
plot(output, projection, vertical, horizontal, input, graph, title)
