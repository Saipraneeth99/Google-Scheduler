from googleCalendarServiceImpl import GoogleCalendarService
from decorators import log_method_call

class BackUpCalendar:
    def __init__(self, credentials):
        self.service = GoogleCalendarService(credentials)

    @log_method_call
    def back_up(self, csv_file, calendar_id: str = 'primary') -> None:
        events = self.service.list_events(calendar_id)
        self._save_events_to_csv(events, csv_file)

    @log_method_call
    def _save_events_to_csv(self, events, csv_file):
        import csv
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Summary', 'Start', 'End', 'Description'])
            for event in events:
                summary = event.get('summary', 'No Title')
                start = event['start'].get('dateTime', event['start'].get('date'))
                end = event['end'].get('dateTime', event['end'].get('date'))
                description = event.get('description', 'No Description')
                writer.writerow([summary, start, end, description])
