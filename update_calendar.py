from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

import json

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = "https://www.googleapis.com/auth/calendar"
store = file.Storage('G_files/storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('G_files/client_secrets.json', SCOPES)
    creds = tools.run_flow(flow, store, flags) if flags else tools.run(flow, store)

CAL = build('calendar', 'v3', http=creds.authorize(Http()))

GMT_OFF = '+02:00'

CALENDAR_ID = 'h79uann7ldpngf4hj8e35v1u0c@group.calendar.google.com'

def coloring():
    with open('Data/log.json', 'r') as f:
        data = json.load(f)

        for eventId in data:
            event = CAL.events().get(calendarId=CALENDAR_ID, eventId=eventId).execute()

            # insert coloring here



coloring()