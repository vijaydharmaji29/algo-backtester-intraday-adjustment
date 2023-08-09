import os
import csv
from datetime import datetime, timedelta

#getting all datetimes possible
all_datetimes = []
with open('data/BANKNIFTY.csv', mode ='r')as file:
        # reading the CSV file
        csvFile = csv.reader(file)
        # displaying the contents of the CSV file
        for lines in csvFile:
            dateformated = lines[1][6:10] + '-' + lines[1][3:5] + '-' + lines[1][0:2] + ' ' + lines[1][-5:] + ':59'
            all_datetimes.append(dateformated)
all_datetimes.pop(0)

def add_before(curr_rows):
    new_rows = []
    ctr = 0

    months = ['HEY', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    all_datetime_modified = []
    datetime_max = datetime(int(curr_rows[0][1][5:7]) + 2000, months.index(curr_rows[0][1][2:5]), int(curr_rows[0][1][:2])) + timedelta(days=1)
    datetime_min = datetime_max - timedelta(days=7)

    for i in all_datetimes:
        datetime_obj = datetime.strptime(i, '%Y-%m-%d %H:%M:%S')
        if datetime_obj >= datetime_min and datetime_obj <= datetime_max:
            all_datetime_modified.append(i)

    for i in all_datetime_modified:
        if i != (curr_rows[0][4] + ' ' + curr_rows[0][5]):
            new_rows.append((curr_rows[ctr][0], curr_rows[ctr][1], curr_rows[ctr][2], curr_rows[ctr][3], i[:10], i[11:], curr_rows[ctr][6], curr_rows[ctr][7], curr_rows[ctr][8], curr_rows[ctr][9], 0, 0))
        else:
            break

    return new_rows

def add_middle(curr_rows, start):
    new_rows = []

    ctr = 0
    flag = True


    months = ['HEY', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    all_datetime_modified = []
    datetime_max = datetime(int(curr_rows[0][1][5:7]) + 2000, months.index(curr_rows[0][1][2:5]), int(curr_rows[0][1][:2])) + timedelta(days=1)
    datetime_min = datetime_max - timedelta(days=7)

    for i in all_datetimes:
        datetime_obj = datetime.strptime(i, '%Y-%m-%d %H:%M:%S')
        if datetime_obj >= datetime_min and datetime_obj <= datetime_max:
            all_datetime_modified.append(i)
    
    flag = True

    for i in all_datetime_modified[start: ]:
        new_rows.append((curr_rows[ctr][0], curr_rows[ctr][1], curr_rows[ctr][2], curr_rows[ctr][3], i[:10], i[11:], curr_rows[ctr][6], curr_rows[ctr][7], curr_rows[ctr][8], curr_rows[ctr][9], 0, 0))
        if i == (curr_rows[ctr][4] + ' ' + curr_rows[ctr][5]) or i[11:] == '15:29:59':
            ctr += 1
            if ctr == len(curr_rows):
                ctr -= 1


    return new_rows

def add_data(filename):
    #adding before
    curr_rows = []
    with open('data/niftymodoptions/' + filename) as file:
        csvfile = csv.reader(file)
        for row in file:
            curr_rows.append(row.split(','))

    header = curr_rows.pop(0)
    header[-1] = 'OI'

    new = add_before(curr_rows)

    new += add_middle(curr_rows, len(new))

    with open('data/niftymodopts/' + filename, 'w') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(header)
        for i in new:
            csvwriter.writerow(i)


    print('DONE -', filename)

if __name__ == '__main__':
    # f = 'NIFTY21MAY15250CE.csv'
    # add_data(f)
    files = os.listdir('data/niftymodoptions/')
    files.remove('.DS_Store')
    errors = []
    ctr = 0
    for f in files:
        ctr += 1
        try:
            print('DOING - ', ctr, 'OF', len(files))
            add_data(f)
        except:
            errors.append(f)
    
    print(errors)