from functools import wraps

from observer_pattern.unfinished_prototype.observer import Subscriber, Subject, SubscriberProtocol

logs = Subscriber(name="Logs")
slack_message = Subscriber(name="Slack")
email = Subscriber(name="Email")


def observer_decorator(*subscribers: SubscriberProtocol):
    def decorator(func):
        func_subject = Subject(subscribers={subscriber for subscriber in subscribers})

        @wraps(func)
        def wrapper(*args, **kwargs):
            func_subject.notify(msg=f"Starting function {func.__name__} with {args = }, {kwargs = }")
            ret_val = func(*args, **kwargs)
            func_subject.notify(msg=f"Closing function {func.__name__}")
            return ret_val

        return wrapper

    return decorator


code_message = Subject(name="Code messages subject")
warning_message = Subject(name="Warning messages subject")
critical_error = Subject(name="Critical error subject")


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
another_function()
different_function()
