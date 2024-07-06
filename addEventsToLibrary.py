from googleCalendarServiceImpl import GoogleCalendarService
from decorators import log_method_call
import logging

class AddEventsToLibrary:
    def __init__(self, credentials):
        self.service = GoogleCalendarService(credentials)

    @log_method_call
    def add_events(self, csv_file, calendar_id: str = 'primary') -> None:
        events = self._load_events_from_csv(csv_file)
        for event in events:
            logging.debug(f"Adding event: {event}")
            self.service.add_event(event, calendar_id)

    @log_method_call
    def _load_events_from_csv(self, csv_file):
        import csv
        events = []
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                start_date = row['Start Date']
                start_time = row['Start Time']
                end_date = row['End Date']
                end_time = row['End Time']

                if not start_date or not start_time or not end_date or not end_time:
                    logging.warning(f"Skipping event with missing date/time: {row}")
                    continue
                
                event = {
                    'summary': row['Subject'],
                    'description': row['Description'],
                    'start': {
                        'dateTime': self.convert_time(start_date, start_time),
                        'timeZone': 'America/New_York',
                    },
                    'end': {
                        'dateTime': self.convert_time(end_date, end_time),
                        'timeZone': 'America/New_York',
                    },
                    'recurrence': [
                        'RRULE:FREQ=DAILY;COUNT=7'  # Adjust the recurrence rule as needed
                    ]
                }
                events.append(event)
        return events

    @staticmethod
    @log_method_call
    def convert_time(date, time):
        import datetime
        dt = datetime.datetime.strptime(date + ' ' + time, '%Y-%m-%d %I:%M %p')
        return dt.isoformat()
