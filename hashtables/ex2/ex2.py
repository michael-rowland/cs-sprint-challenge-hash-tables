class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    storage = {}
    for ticket in tickets:
        storage[ticket.source] = ticket.destination

    route = ["NONE"]
    next_stop = ""
    while next_stop != "NONE":
        next_stop = storage[route[-1]]
        route.append(next_stop)
    return route[1:]
