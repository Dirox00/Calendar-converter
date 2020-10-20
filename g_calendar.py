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

def add_event(summary, start, end):
    TIMEZONE = 'Europe/Madrid'

    EVENT = {
        'summary': summary,
        'start': {'dateTime': '{}'.format(start), 'timeZone': TIMEZONE},
        'end': {'dateTime': '{}'.format(end), 'timeZone': TIMEZONE}
    }
    e = CAL.events().insert(calendarId='g8vlb8nhes1amq2ujpv4t8n8ho@group.calendar.google.com', body=EVENT).execute()

    with open('Data/log.json', 'r+') as f:
        data = json.load(f)

        data[e['id']] = EVENT
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

    print(e['id'])
    # ------------------------------------------
