import uuid
from dataclasses import dataclass, field
from typing import Protocol


class SubscriberProtocol(Protocol):
    name: str

    def notify(self, msg: str, *args, **kwargs) -> None:
        ...

    def __hash__(self):
        ...


@dataclass(unsafe_hash=True)
class Subscriber:
    name: str

    def notify(self, msg: str, *args, **kwargs):
        print(f"{self.name} received {msg = }, {args= }, {kwargs= }")


# class SubjectProtocol(Protocol):
#     subscribers: set[SubscriberProtocol]
#
#     def subscribe(self, subscriber: SubscriberProtocol) -> None:
#         ...
#
#     def unsubscribe(self, subscriber: SubscriberProtocol) -> None:
#         ...
#
#     def notify(self) -> None:
#         ...


@dataclass
class Subject:
    name: str
    subscribers: set[SubscriberProtocol] = field(default_factory=set)

    def subscribe(self, subscriber: SubscriberProtocol) -> None:
        self.subscribers.add(subscriber)

    def unsubscribe(self, subscriber: SubscriberProtocol) -> None:
        self.subscribers.remove(subscriber)

    def notify(self, msg: str, *args, **kwargs):
        msg = f"TOPIC:{self.name}: {msg}"
        for subscriber in self.subscribers:
            subscriber.notify(msg, *args, **kwargs)
