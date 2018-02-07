import xml.etree.ElementTree as ET
import csv

def start(dates, share_name):
    tree = ET.parse("example.xml")
    root = tree.getroot()
    # open a file for writing
    stock_data = open('example.csv', 'w')
    # create the csv writer object
    csvwriter = csv.writer(stock_data)
    #The first row of CSV file.
    csvwriter.writerow(share_name)
    resident_head = ["Date", "Open value", "Highest value", "Lowest value", "Close value", "Total Volume"]
    csvwriter.writerow(resident_head)
    datasets = len(root[1].getchildren())
    for set in range(0, datasets):
        datalist = []
        datalist.append(dates[set])
        datalist.append(root[1][set][0].text) #Open Value
        datalist.append(root[1][set][1].text) #Highest Value
        datalist.append(root[1][set][2].text) #Lowest Value
        datalist.append(root[1][set][3].text) #Close Value
        datalist.append(root[1][set][4].text) #Total vloume
        csvwriter.writerow(datalist)
    stock_data.close()
