from urllib.request import urlopen
#from yahoo_quote_download import yqd
import json
import dicttoxml
from xml.dom.minidom import parseString

#this function will obtain the api_url and get the data(in JSON file)
#JSON in string will be returned.
def getapidata(api_url):
    #url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=15min&outputsize=full&apikey=demo" #sample API link
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_" + interval + "&symbol=" + symbol + "&interval=15min&outputsize=full&apikey=J3Q2DC5XWYELA6G5"
    page = urlopen(url)
    data = page.read() 
    data = bytes.decode(data)
    content = json.loads(data)
    return content

#This function will convert the JSON data into XML file
#Returned data type is string
#The data is XML in string.
def json2xml(json_data):
    xml_content = dicttoxml.dicttoxml(json_data)
    xml_content = bytes.decode(xml_content)
    xml_content = parseString(xml_content)
    xml_data = xml_content.toprettyxml()
    return xml_data

#This function will open file and write the XML code into the file
def writexmltofile(xml_data):
    filename = "example.xml"
    fileobj = open(filename, "w")
    fileobj.write(xml_data)
    fileobj.close()

#Code run here:
data = getapidata("test") #in proper case, please replace the test to your API_link, and comment out line 11
test = json2xml(data)
writexmltofile(test)
