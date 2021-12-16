import csv

fields = ['date' , 'time']

with open('fileformain.csv' , 'w' , newline = '') as f:
    csv_w = csv.writer(f , delimiter=',')
    csv_w.writerow(fields)