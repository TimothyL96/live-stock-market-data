from urllib.request import urlopen
#from yahoo_quote_download import yqd
import json
import dicttoxml
from xml.dom.minidom import parseString

#this function will obtain the api_url and get the data(in JSON file)
#JSON in string will be returned.
def getapidata(api_url):
    #API token = "J3Q2DC5XWYELA6G5"
    #url = api_url
    symbol = options[0]
    interval = options[1]
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_" + interval + "&symbol=" + symbol + "&interval=15min&outputsize=full&apikey=J3Q2DC5XWYELA6G5"
    page = urlopen(url)
    data = page.read()  #API problem, data come in bytes instead of String
    data = bytes.decode(data)
    content = json.loads(data)
    return content
    # print(content)
    
   
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
