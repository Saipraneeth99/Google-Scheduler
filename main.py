import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from addEventsToLibrary import AddEventsToLibrary
from backupCalendar import BackUpCalendar
from manageEventsInCalendar import ManageEventsInCalendar
import logging

# Set up logging to file
logging.basicConfig(level=logging.DEBUG, filename='calendar_log.log', filemode='w', format='%(asctime)s %(levelname)s:%(message)s')

SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

if __name__ == '__main__':
    credentials = authenticate_google()
    
    # Uncomment the function calls as needed
    
    # Backup events to a CSV file
    # backup_service = BackUpCalendar(credentials)
    # backup_service.back_up('calendar_backup.csv')

    # Add events to the calendar
    add_service = AddEventsToLibrary(credentials)
    add_service.add_events('updated_weekly_schedule.csv')

    # List all events to check what will be deleted
    # manage_service = ManageEventsInCalendar(credentials)
    # events = manage_service.list_events()
    # for event in events:
    #     logging.debug(event)

    # # Delete all events
    # manage_service.delete_all_events()
