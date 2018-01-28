#!/usr/bin/python 
# script to find the optimal threshold
import pandas as pd
from sys import argv
log_file = argv[1]
a = 1.2
df = pd.read_csv(log_file, sep=' ').values
best = df[-1][0]
maxt = 0
for i in df:
	if i[0] > best and i[1] > maxt:
		maxt = i[1]
print int(a * maxt)
