topic1 = set()
topic2 = set()
topic3 = set()


def notification_service(observers: set, msg: str):
    for observer in observers:
        observer.notification(msg)


class Subscriber:
    def __init__(self, name):
        self.name = name

    def notification(self, info):
        print(f"{self.name} got some {info= }")


slack = Subscriber("slack")
teams = Subscriber("teams")
emails = Subscriber("mailing_list")
logging_service = Subscriber("logging service")

topic1.update((slack, teams, emails, logging_service))
topic2.update((logging_service, emails))
topic3.update((slack, teams))

notification_service(topic1, "topic1 message")
print("\n")
notification_service(topic2, "topic2 message")
print("\n")
notification_service(topic3, "topic3 message")
