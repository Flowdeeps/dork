#! env /bin/python
import os
import json

gamefile = "data.json"

# stage variables
width = 40
# get the main json file
data = json.loads(open(gamefile).read())
# separate the data out into a new objects
app = data["app"]
logo = app[0]
info = app[1]
rooms = data["rooms"][0]

for line in logo["logo"]:
    print(line)["line"]

for appinfo in info["meta"]:
    if appinfo.keys()[0] == "version":
        print "Version: " + appinfo.values()[0]
    if appinfo.keys()[0] == "author":
        print "Author: " + appinfo.values()[0]
