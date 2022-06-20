
from Parser import parser
import os 
import glob
import csv
from configuration import getConfigBySection

dop = []
pathdirectory = getConfigBySection('SECTION1','pathSource')   #### reference a ce fichier excel particulier
pathresultFile = getConfigBySection('SECTION1','pathResult')
os.chdir(pathdirectory)
files = os.listdir(pathdirectory)
for file in files:
    if file in glob.glob("*.pdf") :
        data = parser(file) 
        d = data.values()
        dop.append(d)
for my_data in data :
    header = data.keys() 
    rows = data.values()
with open('scheneider.csv', 'w') as f:
    writer = csv.writer(f)

        
    writer.writerow(header) # write the header

        
    writer.writerows(dop)


