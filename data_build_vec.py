#!/usr/bin/python
import math
fd = open("plot_data", "r")
lines = fd.readlines()

lines = lines[1:]
fd.close()
xpoints = []
ypoints = []
x = [0]
y = [0]
cur = xpoints
skip = x
i = -1
for line in lines:
	#reached end of x points
	if "max.print" in line:
		if cur == ypoints:
			print("breaking :3")
			break;
		print ("didnt break")
		cur = ypoints
		skip = y
	else:
		line = line.split()
		line = line[1:]
		for points in line:
    			if points != "-Inf" and points != "NA":
				try:
					cur.append((float(points)))
				except:
					pass
fd = open("raw_data","w")
sharelist = []
for i in range(len(xpoints)):
	sharelist.append(str(xpoints[i]) + " " + str(ypoints[i]))
sharelist.sort() 
if ( len(xpoints) != len(ypoints)):
	print "warning x and y do not match"
	print len(xpoints), len(ypoints)
for i in range(len(xpoints)):
	fd.write(str(xpoints[i]) + " " + str(ypoints[i]) + "\n")
	#print sharelist[i]
print ypoints[-10:]
fd.close()
