from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = "https://www.googleapis.com/auth/calendar"
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
    creds = tools.run_flow(flow, store, flags) if flags else tools.run(flow, store)

CAL = build('calendar', 'v3', http=creds.authorize(Http()))

GMT_OFF = '+02:00'

# This for adding an event to Horario ------
EVENT = {
    'summary': 'Hii',
    'start': {'dateTime': '2020-09-15T13:00:00%s' % GMT_OFF},
    'end': {'dateTime': '2020-09-15T15:00:00%s' % GMT_OFF}
}

e = CAL.events().insert(calendarId='2pvs3q69rh877ba8kvtl7o8tf8@group.calendar.google.com', body=EVENT).execute()
# ------------------------------------------
