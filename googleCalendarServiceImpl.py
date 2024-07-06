from googleapiclient.discovery import build
from googleCalendarApi import GoogleCalendarAPI
from decorators import log_method_call

class GoogleCalendarService(GoogleCalendarAPI):
    def __init__(self, credentials):
        self.service = build('calendar', 'v3', credentials=credentials)

    @log_method_call
    def authenticate(self) -> None:
        pass

    @log_method_call
    def list_events(self, calendar_id: str = 'primary') -> list:
        events_result = self.service.events().list(calendarId=calendar_id).execute()
        events = events_result.get('items', [])
        return events

    @log_method_call
    def add_event(self, event: dict, calendar_id: str = 'primary') -> None:
        self.service.events().insert(calendarId=calendar_id, body=event).execute()

    @log_method_call
    def delete_event(self, event_id: str, calendar_id: str = 'primary') -> None:
        self.service.events().delete(calendarId=calendar_id, eventId=event_id).execute()
