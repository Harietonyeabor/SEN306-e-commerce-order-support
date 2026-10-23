
"""Provide a Queue data structure for order processing."""


class Queue:
    """Implement a First-In, First-Out (FIFO) queue."""

    def __init__(self):
        """Create an empty queue."""
        self._items = []

        
    def items(self):
        """Return a copy of the items currently in the queue."""
        return self._items.copy()


    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self._items.append(item)

    def dequeue(self):
        """Remove and return the oldest item, or None if empty."""
        if self.is_empty():
            return None

        return self._items.pop(0)

    def remove(self, item):
        """Remove an item and return its position, or -1 if not found."""
        for index, queued_item in enumerate(self._items):
            if queued_item == item:
                self._items.pop(index)
                return index

        return -1

    def insert_at(self, index, item):
        """Insert an item at a specified queue position."""
        self._items.insert(index, item)

    def front(self):
        """Return the oldest item without removing it."""
        if self.is_empty():
            return None

        return self._items[0]

    def is_empty(self):
        """Return True if the queue contains no items."""
        return len(self._items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self._items)
