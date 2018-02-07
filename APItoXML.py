from urllib.request import urlopen
#from yahoo_quote_download import yqd
import xmltodict
import json
from src.json2xml import Json2xml
import dicttoxml
from xml.dom.minidom import parseString

#this function will obtain the api_url and get the data(in JSON file)
#JSON in string will be returned.
def getapidata(options):
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
#Data type is string
def json2xml(json_data):
    #took others libraries to help:
    #Library link:  https://github.com/vinitkumar/json2xml
    data_object = Json2xml(json_data)
    xml_output = data_object.json2xml()
    return xml_output

#This functino will write the data into xml file
#input parameter is a string
#output is a xml file, which named example.xml for this case
def writexmltofile(xml_data):
    filename = "example.xml"
    fileobj = open(filename, "w")
    fileobj.write("<?xml version=\"1.0\"?>\n")
    fileobj.write(xml_data)
    fileobj.close()

def start(options):
    data = getapidata(options)
    test = json2xml(data)
    writexmltofile(test)
