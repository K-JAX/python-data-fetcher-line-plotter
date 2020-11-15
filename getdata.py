import fnmatch
import os
import time
from time import sleep

from fetchbot import FetchBot


for file in os.listdir('./Datasets'):
	if fnmatch.fnmatch(file, '*.xlsx'):
		# global fileName
		fileName = file

if not 'fileName' in globals():
	fileName = ''


dir_path = os.path.dirname(os.path.realpath(__file__))
data_dir = dir_path + '/Datasets/'
dataFile = data_dir + fileName
fileExists = os.path.isfile(dataFile)
halfMonth = 30 * 24 * 60 * 60 / 2

def get_file_age(file):
	return time.time() - os.path.getmtime(file)

if not fileExists:
	print("File doesn't exist, go fetch!")
	goGet = FetchBot()
elif get_file_age(dataFile) > halfMonth:
	print("File is too old, go fetch!")
	os.remove(dataFile)
	goGet = FetchBot()
else:
	print("File is there and up to date. Don't fetch")

import csv
import xlrd

def csv_from_excel():
    wb = xlrd.open_workbook(dataFile)
    sh = wb.sheet_by_name('BLS Data Series')
    your_csv_file = open(data_dir + 'unemployment-data.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()

# runs the csv_from_excel function:
if fileExists:
	csv_from_excel()
