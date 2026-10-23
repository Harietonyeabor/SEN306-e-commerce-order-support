
"""Provide a singly linked list for storing order records."""


class Node:
    """Represent one node in a singly linked list."""

    def __init__(self, data):
        """Initialize a node with data and no next node."""
        self.data = data
        self.next = None


class LinkedList:
    """Manage order records using connected nodes."""

    def __init__(self):
        """Create an empty linked list."""
        self.head = None

    def is_empty(self):
        """Return True if the list has no nodes."""
        return self.head is None

    def insert_at_end(self, data):
        """Add a new node to the end of the list."""
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def search(self, order_id):
        """Find and return an order record by ID, or None."""
        current = self.head

        while current is not None:
            if current.data["order_id"] == order_id:
                return current.data

            current = current.next

        return None

    def delete(self, order_id):
        """Delete an order record by ID and report success."""
        current = self.head
        previous = None

        while current is not None:
            if current.data["order_id"] == order_id:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                return True

            previous = current
            current = current.next

        return False

    
    def insert_at(self, index, data):
        """Insert an order record at a specified position."""
        if index <= 0 or self.head is None:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return

        new_node = Node(data)
        current = self.head
        position = 0

        while current.next is not None and position < index - 1:
            current = current.next
            position += 1

        new_node.next = current.next
        current.next = new_node

    def index_of(self, order_id):
        """Return an order's position, or -1 if it is not found."""
        current = self.head
        index = 0

        while current is not None:
            if current.data["order_id"] == order_id:
                return index

            current = current.next
            index += 1

        return -1


    def display(self):
        """Return all order records in list order."""
        records = []
        current = self.head

        while current is not None:
            records.append(current.data)
            current = current.next

        return records
