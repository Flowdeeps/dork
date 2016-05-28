#! env /bin/python
import os
import json

gamefile = "data.json"

# stage variables
width = 40
# get the main json file
data = json.loads(open(gamefile).read())
# separate the app data out into a new object
app = data["app"][0]

for line in app["logo"]:
    print(line)["line"]
