# (C) Copyright 1996-2019 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.

import xarray as xr
import numpy as np

from Magics import macro as magics

ref = "xarray4"
ds = xr.open_dataset('z_500.nc')

png = magics.output(output_name_first_page_number = "off", output_name = ref)
data = magics.mxarray(xarray_dataset = ds, xarray_variable_name = "z")
contour = magics.mcont(contour_automatic_setting = "ecmwf")

magics.plot(png, data, contour, magics.mcoast())
