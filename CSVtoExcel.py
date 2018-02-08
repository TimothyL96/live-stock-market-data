import sys
import csv
import xlsxwriter

# if we read f.csv we will write f.xlsx


def start():
	#Insert your csv file name here
	csvfilename = "example.csv"

	#change csv file to xlsx file


	wb = xlsxwriter.Workbook(csvfilename.replace(".csv",".xlsx"))
	ws = wb.add_worksheet("WS1")    # your worksheet title here
	with open(csvfilename,'r') as csvfile:
	    table = csv.reader(csvfile)
	    i = 0
	    # write each row from the csv file as text into the excel file
	    # this may be adjusted to use 'excel types' explicitly (see xlsxwriter doc)
	    for row in table:
	        ws.write_row(i, 0, row)
	        i += 1
	wb.close()
