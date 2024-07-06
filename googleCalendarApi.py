from abc import ABC, abstractmethod

class GoogleCalendarAPI(ABC):
    @abstractmethod
    def authenticate(self) -> None:
        pass

    @abstractmethod
    def list_events(self, calendar_id: str = 'primary') -> list:
        pass

    @abstractmethod
    def add_event(self, event: dict, calendar_id: str = 'primary') -> None:
        pass

    @abstractmethod
    def delete_event(self, event_id: str, calendar_id: str = 'primary') -> None:
        pass
