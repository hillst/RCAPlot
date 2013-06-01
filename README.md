RCAPlot
=======

This RCAPlot plots the points in 3 dimensions, where fpkm is the x axis, CV is the y axis, and the sample name is the z axis.

To build the plot, it requires data from the RPlotter tool. You can run this by executing RPlotter with the -3d argument. Once the data is gathered in the file plot_data, call make all. It will build the binaries for the RCAPlot. Be sure that you have the required dependencies (See below)

You may execute the tool by calling ./plot.


Example
=========

If you would like to use the data provided, you can build the sample files with ./data_build.py
This sample includes about 8000 data points on 4 different samples. Red indicates a very poor standard deviation, and green indicates a very good standard deviation. 


GL Dependencies
===============
For a CentOS6 install, make sure you have the latest NVidia drivers and then install these packages via yum:

yum install mesa-libGL mesa-libGLU-devel freeglut-devel bullet-extras-devel libXmu-dev libXmu6 libXi-devel

On a Fedora install, you will need
yum install libXmu-dev libXmu6

If these don't work, I recommend continuing to work on getting the correct packages installed, or use a different tool for plotting. 
