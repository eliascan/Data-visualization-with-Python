# Data-visualization-with-Python

# DESCRIPTION

Included is a python file called classify.py with 2 numpy arrays containing simplified geospatial data:

- LANDCOVER: the type of landcover at a given x,y pixel coordinate
- CARBON: carbon stocks in the soil, covering an area within the coordinates described by LANDCOVER

Write a command-line program that does a "classification" operation with the data: calculate the average (mean) for each type of landcover in our given carbon area. That is, the average carbon values grouped by landcover type. The print out the result (ideally nicely formatted).

Additionally, the program should accept two optional arguments:

- "landcover": If present, only do the calculation for that given type of landcover. An appropriate error message should be displayed if the given value is not a valid landcover type.
- "stddev": If present, also calculate the standard deviation (in addition to the average).
