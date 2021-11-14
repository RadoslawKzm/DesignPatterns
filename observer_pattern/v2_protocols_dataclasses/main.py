from observer_pattern.v2_protocols_dataclasses.observer import Subscriber, observer_decorator

logs = Subscriber(name="Logs")
slack_message = Subscriber(name="Slack")
email = Subscriber(name="Email")


@observer_decorator(logs)
def some_function():
    print("some some_function")


@observer_decorator(logs, slack_message)
def another_function():
    print("some another_function")


@observer_decorator(logs, slack_message, email)
def different_function():
    print("some different_function")


some_function()
print(f"\n")
another_function()
print(f"\n")
different_function()
print(f"\n")
