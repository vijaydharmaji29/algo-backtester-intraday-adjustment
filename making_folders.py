import os
import shutil

months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

if __name__ == '__main__':

    for i in months:
        os.mkdir('./data/' + i + '/')

    # ffs = os.listdir('data/df_csv/')
    # print(ffs)

    # for f in ffs:
    #     month = f[7:10]
    #     print(f)