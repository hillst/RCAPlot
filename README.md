RCAPlot
=======

This RCAPlot plots the points in 3 dimensions, where fpkm is the x axis, CV is the y axis, and the sample name is the z axis.

To build the plot, it requires data from the RPlotter tool. You can run this by executing RPlotter with the -3d argument. Once built, it will attempt to build the graphics visualization.

Once the visualization is built (compiled), you may execute it by calling ./plot


GL Dependencies
===============
For a CentOS6 install, make sure you have the latest NVidia drivers and then install these packages via yum:

yum install mesa-libGL mesa-libGLU-devel freeglut-devel bullet-extras-devel libXmu-dev libXmu6 libXi-devel

On a Fedora install, you will need
yum install libXmu-dev libXmu6

If these don't work, I recommend continuing to work on getting the correct packages installed, or use a different tool for plotting. 
