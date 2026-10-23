
from queue import Queue


def main():
    order_queue = Queue()

    print("Is queue empty?", order_queue.is_empty())

    order_queue.enqueue("ORD001")
    order_queue.enqueue("ORD002")
    order_queue.enqueue("ORD003")

    print("Number of orders:", order_queue.size())
    print("Next order to process:", order_queue.front())
    print("Processing order:", order_queue.dequeue())
    print("Next order after processing:", order_queue.front())
    print("Orders remaining:", order_queue.size())


if __name__ == "__main__":
    main()
