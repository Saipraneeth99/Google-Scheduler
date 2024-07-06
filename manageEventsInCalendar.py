from googleCalendarServiceImpl import GoogleCalendarService
from decorators import log_method_call
import logging

class ManageEventsInCalendar:
    def __init__(self, credentials):
        self.service = GoogleCalendarService(credentials)

    @log_method_call
    def list_events(self, calendar_id: str = 'primary') -> list:
        events = self.service.list_events(calendar_id)
        logging.debug(f"Listing events: {events}")
        return events

    @log_method_call
    def delete_event(self, event_id: str, calendar_id: str = 'primary') -> None:
        self.service.delete_event(event_id, calendar_id)
        logging.debug(f"Deleted event with ID: {event_id}")

    @log_method_call
    def delete_all_events(self, calendar_id: str = 'primary') -> None:
        events = self.service.list_events(calendar_id)
        for event in events:
            self.delete_event(event['id'], calendar_id)
        logging.debug("Deleted all events")
