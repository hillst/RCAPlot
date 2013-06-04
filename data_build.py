#!/usr/bin/python
# This script transforms the cuff output taken from cummerbund into something we can use  (Our C program). 
# 	Do not run this directly, it should be called when make is called.
import os
import math
fd = open("plot_data");
lines = fd.readlines();
final_list = []
fpkmlines = False
countlines = False
cvlines = False
fpkmlookup = []
i = -1
j = -1
start = False
for line in lines:
	#first few lines
	if line[0:6] == "> res\n":
		start = True
		fpkmlines = True
		i = 0
		#first line found is header
	if start:
		if "count_uncertainty" in line:
			fpkmlines = False
			countlines = True
		
		if fpkmlines and i > 1:
			#number, geneid, samplename, (floats)fpkm, conf_hi, conf_lo
			linespl = line.split(" ")
			linespl = filter(None, linespl)
			#if sample is in dictionary append fpkm, else
			fpkmlookup.append({})
			fpkmlookup[i-2]['fpkm'] = float(linespl[3])
			fpkmlookup[i-2]['samplename'] = str(linespl[2])
			i+=1
		if i == 0 or i == 1:
			i+=1
		#might not be tab :(
		if cvlines and j > 0:
			if "[" in line:
				break
			linespl = line.split(' ')
			linespl = filter(None, linespl)
			if not ("NA" in linespl[3]):
				fpkmlookup[j-1]['CV'] = float(linespl[3])
				fpkmlookup[j-1]['stddev'] = float(linespl[2])
			else:
				fpkmlookup[j-1]['CV'] = "DELETE"
			j+=1
		if countlines:
			#check last character to avoid collision with countline
			#both start with tab, but both will set countline to true so whatever
			if "CV" in line:
				j = 1
				cvlines = True
		
fpkmlookup = sorted(fpkmlookup, key=lambda k: k['samplename']) 
fpkmlookup = sorted(fpkmlookup, key=lambda k: k['CV'])
for line in fpkmlookup:
	try:
		print math.log10(line['CV']) + 1.2
	except:
		pass
fdtable = {}
try:
	os.mkdir(".samples")
except:
	pass
for vals in fpkmlookup:
	if vals["CV"] != "DELETE":
		if not (vals["samplename"] in fdtable):
			#open new handle
			fd = open('.samples/'+vals["samplename"], 'w')
			fdtable[vals["samplename"]] = fd
		fdtable[vals["samplename"]].write(str(vals["fpkm"]) + " " + str(vals["CV"]) + " " + str(vals["stddev"]) +"\n")
for fd in fdtable:
	fdtable[fd].close()

	
