import string
import random


def generate_id(*, length=8):
    # helper function for generating an id
    return "".join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:
    def __init__(self, *, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


class CustomerSupport:
    def __init__(self, *, processing_strategy: str = "fifo"):
        self.tickets = []
        self.processing_strategy = processing_strategy

    def create_ticket(self, *, customer, issue):
        self.tickets.append(SupportTicket(customer=customer, issue=issue))

    def process_tickets(self):
        # if it's empty, don't do anything
        if len(self.tickets) == 0:
            print("There are no tickets to process. Well done!")
            return

        if self.processing_strategy == "fifo":
            for ticket in self.tickets:
                self.process_ticket(ticket=ticket)
        elif self.processing_strategy == "filo":
            for ticket in reversed(self.tickets):
                self.process_ticket(ticket=ticket)
        elif self.processing_strategy == "random":
            list_copy = self.tickets.copy()
            random.shuffle(list_copy)
            for ticket in list_copy:
                self.process_ticket(ticket=ticket)

    @staticmethod
    def process_ticket(*, ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


# create the application
app = CustomerSupport(processing_strategy="filo")

# register a few tickets
app.create_ticket(customer="John Smith", issue="My computer makes strange sounds!")
app.create_ticket(customer="Linus Sebastian", issue="I can't upload any videos, please help.")
app.create_ticket(customer="Bill Gates", issue="VSCode doesn't automatically solve my bugs.")

# process the tickets
app.process_tickets()
