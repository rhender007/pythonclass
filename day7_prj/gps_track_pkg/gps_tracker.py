'''
Created on Dec 1, 2016

@author: Student
'''
import csv

gpsTrack = open("gps_track.txt", "r")

csvReader = csv.reader(gpsTrack)
header = csvReader.__next__()
latIndex = header.index("lat")
longIndex = header.index("long")

coordList = []

# Loop through the lines in the file and get each coords
for row in csvReader:
    lat = row[latIndex]
    lon = row[longIndex]
    coordList.append([lat, lon])
    
print(coordList)
