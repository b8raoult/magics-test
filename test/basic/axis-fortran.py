import Magics as mpp
from numpy import *

mpp.init()
mpp.setc("output_format", "png")
mpp.setc("output_ps_colour_model", "rgb")
mpp.setc("output_ps_split", "off")
mpp.setc("output_name_first_page_number", "off")
mpp.setc("output_name", "axis-fortran")
mpp.setc("subpage_map_projection", "none")
mpp.setc("axis_orientation", "horizontal")
mpp.setc("axis_type", "date")
mpp.setc("axis_date_min_value", "2019-11-01 00:00:00")
mpp.setc("axis_date_max_value", "2019-11-03 00:00:00")
mpp.setc("axis_date_type", "automatic")
mpp.axis()
mpp.setc("axis_orientation", "vertical")
mpp.setr("axis_tick_interval", 0.01)
mpp.setr("axis_min_value", 0.05)
mpp.setr("axis_max_value", 0.35)
mpp.axis()
mpp.set1c(
    "graph_curve_date_x_values",
    ["2019-11-01 00:00:00", "2019-11-02 00:00:00", "2019-11-03 00:00:00"],
)
mpp.setc("graph_missing_data_mode", "ignore")
mpp.setr("y_missing_value", 1.7e38)
mpp.set1r("graph_curve_y_values", array([0.1, 0.2, 0.3]))  # 3
mpp.setc("graph_type", "curve")
mpp.graph()
mpp.finalize()
