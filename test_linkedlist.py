
from linkedlist import LinkedList


def main():
    order_records = LinkedList()

    print("Is list empty?", order_records.is_empty())

    order_records.insert_at_end({
        "order_id": "ORD001",
        "customer": "Ada",
        "item": "Laptop"
    })

    order_records.insert_at_end({
        "order_id": "ORD002",
        "customer": "Chika",
        "item": "Headphones"
    })

    order_records.insert_at_end({
        "order_id": "ORD003",
        "customer": "David",
        "item": "Keyboard"
    })

    print("All order records:", order_records.display())
    print("Search for ORD002:", order_records.search("ORD002"))

    print("Delete ORD001:", order_records.delete("ORD001"))
    print("Records after deletion:", order_records.display())
    print("Is list empty?", order_records.is_empty())


if __name__ == "__main__":
    main()
