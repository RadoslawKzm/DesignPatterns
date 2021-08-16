"""Ticket ordering example of strategy pattern"""
from abc import ABC, abstractmethod
import random
import string
from typing import List


def generate_id(*, length=8):
    # helper function for generating an id
    return "".join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:
    def __init__(self, *, customer, issue):
        self.id: str = generate_id()
        self.customer: str = customer
        self.issue: str = issue


class TicketStrategy(ABC):
    """Abstract interface for future strategies of ticket ordering"""

    @abstractmethod
    def get_ticket(self, *, tickets: List[SupportTicket]) -> List[SupportTicket]:
        pass


class ReverseTicketStrategy(TicketStrategy):
    def get_ticket(self, *, tickets: List[SupportTicket]) -> List[SupportTicket]:
        list_ = tickets.copy()
        list_.reverse()
        return list_


class RandomTicketStrategy(TicketStrategy):
    def get_ticket(self, *, tickets: List[SupportTicket]) -> List[SupportTicket]:
        list_ = tickets.copy()
        random.shuffle(list_)
        return list_


class FIFOTicketStrategy(TicketStrategy):
    def get_ticket(self, *, tickets: List[SupportTicket]) -> List[SupportTicket]:
        return tickets.copy()


class CustomerSupport:
    def __init__(self):
        self.tickets: List[SupportTicket] = []

    def create_ticket(self, *, customer: str, issue: str):
        self.tickets.append(SupportTicket(customer=customer, issue=issue))

    def process_tickets(self, *, processing_strategy: TicketStrategy):
        if not self.tickets:
            raise ValueError("nothing to process")
        processed_tickets = processing_strategy.get_ticket(tickets=self.tickets)
        for ticket in processed_tickets:
            self.process_ticket(ticket=ticket)

    @staticmethod
    def process_ticket(*, ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


app = CustomerSupport()
app.create_ticket(customer="Test1", issue="Random message 1")
app.create_ticket(customer="Test2", issue="Random message 2")
app.create_ticket(customer="Test3", issue="Random message 3")

app.process_tickets(processing_strategy=ReverseTicketStrategy())
