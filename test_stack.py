
from stack import Stack


def main():
    action_history = Stack()

    print("Is stack empty?", action_history.is_empty())

    action_history.push("Add order ORD001")
    action_history.push("Add order ORD002")
    action_history.push("Add order ORD003")

    print("Number of actions:", action_history.size())
    print("Latest action:", action_history.peek())
    print("Undo action:", action_history.pop())
    print("Latest action after undo:", action_history.peek())
    print("Number of actions remaining:", action_history.size())


if __name__ == "__main__":
    main()
