from Parser2 import parser2
import os 
import glob
import csv
from configuration import getConfigBySection
dop = []
pathdirectory = getConfigBySection('SECTION1','pathSource')   
pathresultFile = getConfigBySection('SECTION1','pathResult')
os.chdir(pathdirectory)
#file = 'declaration-of-performance_wall140.pdf'

files = os.listdir(pathdirectory)
#with open('final2.csv', 'w') as f:
#    writer = csv.writer(f)
#    writer.writerow(header)
allData = {}
for file in files:
    if file in glob.glob("*.pdf") :
        allData = parser2(file, allData)

header = allData.keys()
rows = allData.values()
datarows = list(zip(*rows))
with open('schneider2.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(list(header))
    for row in datarows :
        writer.writerow(list(row))


    





