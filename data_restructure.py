#goes through all niftyoptions, and keeps only 1 week data from expiry
''''
get list of all files
check for rows which are within 1 week
    keep those rows
'''

import os
import csv
from datetime import datetime

#deletes all rows not in 1 week data
def one_week(f):
    flag = False
    months = ['HEY', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    new_lines = []
    with open('data/niftyoptions/' + f) as file:
        csvFile = csv.reader(file)
        for row in csvFile:
            #convert date column and expiry column to date time format
            if flag:
                expiry_date = datetime(int(row[1][5:7]) + 2000, months.index(row[1][2:5]), int(row[1][:2]))
                current_date = datetime.strptime(row[4], '%Y-%m-%d')
                #check if date within a week
                if (expiry_date - current_date).days < 7:
                    new_lines.append(row)
            else:
                new_lines.append(row)
                flag = True

    return new_lines

if __name__ == '__main__':
    files = os.listdir('data/niftyoptions/')
    files.remove('.DS_Store')
    ctr = 0
    none_files = []
    for f in files:
        print('Writing: ' + f + ' ' + str(ctr) + ' of ' + str(len(files)))
        new_rows = one_week(f)
        ctr += 1    
        if new_rows:
            #writing to modopts
            with open('data/niftymodoptions/' + f, 'w') as file:
                csvwriter = csv.writer(file)
                csvwriter.writerows(new_rows)
        else:
            none_files.append(f)
    

    print(none_files)