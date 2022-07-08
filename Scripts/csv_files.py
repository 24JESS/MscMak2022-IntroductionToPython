import csv
import sys

filename = sys.argv[1]
f = open(filename,'r')
lis2 = [] 
lis3 = []
for row in csv.reader(f):
    print(str(row[0] + " " + row[1] + " " + row[2]))