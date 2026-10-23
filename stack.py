
"""Provide a Stack data structure for undo action history."""


class Stack:
    """Implement a Last-In, First-Out (LIFO) stack."""

    def __init__(self):
        """Create an empty stack."""
        self._items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return the top item, or None if empty."""
        if self.is_empty():
            return None

        return self._items.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            return None

        return self._items[-1]

    def is_empty(self):
        """Return True if the stack contains no items."""
        return len(self._items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self._items)
