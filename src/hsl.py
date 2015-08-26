import urllib2
import json
import datetime
import csv
import os

def processData(file):
    username = 'admin'
    password = ''

    sourceID = 1
    variableID = 1
    siteID = 4
    methodID = 1

    values=[]
    with open(file, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            values.append((row[0],row[1]))

    values = values[1:]


    #STEP 1: prepare the uploaded data in JSON format
    data = {
        "user": username,
        "password": password,
        "SiteID": siteID,
        "VariableID": variableID,
        "MethodID": methodID,
        "SourceID": sourceID,
        "values": values
    }

    postdata = json.dumps(data)
    uploadURL = 'http://worldwater.byu.edu/app/index.php/hydroinfo/services/api/values'
    req = urllib2.Request(uploadURL)
    req.add_header('Content-Type', 'application/json')

    try:
        response = urllib2.urlopen(req, postdata)
        print response.read()

    except urllib2.HTTPError, e:
        print e.code
        print e.msg
        print e.headers
        print e.fp.read()