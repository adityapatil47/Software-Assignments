class Event:
    def __init__(self, name, date, location, tickets_available, price):
        self.name = name
        self.date = date
        self.location = location
        self.tickets_available = tickets_available
        self.price = price

    def buy_ticket(self, quantity):
        if self.tickets_available >= quantity:
            self.tickets_available -= quantity
            print(
                f"{quantity} ticket(s) purchased for {self.name} on {self.date} at {self.location}.")
        else:
            print(
                f"Sorry, only {self.tickets_available} ticket(s) available for {self.name} on {self.date} at {self.location}.")


event1 = Event("Regional Theatre Performance",
               "April 20, 2023", "Mumbai", 100, 500)
event2 = Event("Spoken Word Showcase", "May 15, 2023", "New Delhi", 50, 300)


# def test_buy_ticket_successful():
event1.buy_ticket(2)
event2.buy_ticket(4)

# def test_buy_ticket_sold_out():
# def test_buy_ticket_insufficient_tickets():
event1.buy_ticket(110)
event2.buy_ticket(47)
