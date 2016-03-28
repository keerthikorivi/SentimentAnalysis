__author__ = 'keerthikorvi'

import csv
f = open('UserProficiency.csv');
f2=open('UserProficiencyOutput.csv', 'w')
csv_f = csv.reader(f)
for row in csv_f:
  splitTags=row[1].split('>')
  for i in range(0,len(splitTags)-1):
    f2.write(row[0]+","+splitTags[i].replace('<','')+"\n")
    #print(row[0]+","+splitTags[i].replace('<','')+"\n")