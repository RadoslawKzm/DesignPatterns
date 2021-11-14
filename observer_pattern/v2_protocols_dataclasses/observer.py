from dataclasses import dataclass, field
from functools import wraps
from typing import Protocol


class SubscriberProtocol(Protocol):
    name: str

    def notify(self, msg: str, *args, **kwargs) -> None:
        ...


@dataclass(frozen=True)
class Subscriber:
    name: str

    def notify(self, msg: str, *args, **kwargs):
        print(f"{self.name}:{msg}, {args= }, {kwargs= }")


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


def observer_decorator(*subscribers: SubscriberProtocol):
    def decorator(func):
        func_subject = Subject(subscribers={subscriber for subscriber in subscribers}, name=f"{func.__name__}")

        @wraps(func)
        def wrapper(*args, **kwargs):
            func_subject.notify(msg=f"Starting")
            ret_val = func(*args, **kwargs)
            func_subject.notify(msg=f"Closing")
            return ret_val

        return wrapper

    return decorator
