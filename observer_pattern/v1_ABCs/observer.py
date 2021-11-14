from abc import ABC, abstractmethod
from typing import List


class ObserverABC(ABC):
    @abstractmethod
    def notify(self, *args, **kwargs):
        """notify observers"""


class SubjectABC(ABC):
    @abstractmethod
    def __init__(self):
        self._observers: set = set()

    @abstractmethod
    def subscribe(self, *, observer: ObserverABC):
        """subscribe to observers"""

    @abstractmethod
    def unsubscribe(self, *, observer: ObserverABC):
        """delete observer from subscribers"""

    @abstractmethod
    def notify(self):
        """Notify observers"""


class Subject(SubjectABC):
    def __init__(self):
        self._observers: set = set()

    def subscribe(self, *, observer: ObserverABC) -> None:
        self._observers.add(observer)

    def unsubscribe(self, *, observer: ObserverABC) -> None:
        self._observers.remove(observer)

    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer.notify(args, kwargs)


class Observer(ObserverABC):
    def __init__(self, *, name: str, _subjects: List[SubjectABC]):
        self.name = name
        for _subject in _subjects:
            _subject.subscribe(observer=self)

    def notify(self, *args, **kwargs):
        print(f"{self.name} received {args= }, {kwargs= }")


system_message = Subject()
logs = Subject()
corpo_notifications = Subject()

slack = Observer(name="slack", _subjects=[corpo_notifications])
sentry_io = Observer(name="sentry_io", _subjects=[logs, system_message, corpo_notifications])


system_message.notify("system message")
logs.notify("some logging info of severity low")
corpo_notifications.notify("Lets welcome new ork in our Sauron inc. the mordor corporation")
