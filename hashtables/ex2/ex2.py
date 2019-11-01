#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # add each trip as an item in the hashtable
    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    # start with source none
    start = hash_table_retrieve(hashtable, "NONE")
    current_item = start
    
    for i in range(length):
        # append each destination to the route
        route[i] = current_item
        # find each next item using the destination from the previous
        current_item = hash_table_retrieve(hashtable, current_item)
        
    return route

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

result = reconstruct_trip(tickets, 3)
print(result)