#!/usr/bin/env python

import requests
import cred
import sys
import json

#device_id = str(input("which serial?: "))
device_id = sys.argv[1]

#custom variables for the program imported from the cred.py file located in the same directory
key = cred.key

#Main URL for the Meraki Platform
dashboard = "https://api.meraki.com/api/v0/networks/(network_id)/sm/devices/tags"
#api token and other data that needs to be uploaded in the header
headers = {'X-Cisco-Meraki-API-Key': (key), 'Content-Type': 'application/json'}


TAGS_REMOVE = {}
TAGS_REMOVE["serials"] = device_id
TAGS_REMOVE["updateAction"] = "delete"
TAGS_REMOVE["tags"] = "DM,EMAIL"

#remote the tags:
tags_remove = requests.put(dashboard, data=json.dumps(TAGS_REMOVE), headers=headers)

TAGS_ADD = {}
TAGS_ADD["serials"] = device_id
TAGS_ADD["updateAction"] = "add"
TAGS_ADD["tags"] = "DM_IPAD,EMAIL"

tags_add = requests.put(dashboard, data=json.dumps(TAGS_ADD), headers=headers)
