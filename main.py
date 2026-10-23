
"""Run the E-Commerce Order and Support Management System."""

from stack import Stack
from queue import Queue
from linkedlist import LinkedList


def main():
    """Run the application's main menu."""
    action_history = Stack()
    order_queue = Queue()
    order_records = LinkedList()
    next_order_number = 1

    while True:
        print("\n" + "=" * 45)
        print(" E-COMMERCE ORDER AND SUPPORT MANAGEMENT")
        print("=" * 45)
        print("1. Add a new order")
        print("2. Process the next order")
        print("3. View all order records")
        print("4. Search for an order")
        print("5. Delete an order record")
        print("6. Undo the last action")
        print("7. View pending orders")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            order_id = f"ORD{next_order_number:03d}"
            customer = input("Enter customer name: ").strip()
            item = input("Enter item ordered: ").strip()

            if not customer or not item:
                print("Error: Customer name and item are required.")
                continue

            order = {
                "order_id": order_id,
                "customer": customer,
                "item": item,
                "status": "Pending"
            }

            order_records.insert_at_end(order)
            order_queue.enqueue(order_id)
            action_history.push({
                "action": "add_order",
                "order": order
            })

            next_order_number += 1
            print(f"Order {order_id} added successfully.")

        elif choice == "8":
            print("Thank you for using the application. Goodbye!")
            break

        
        elif choice == "2":
            order_id = order_queue.dequeue()

            if order_id is None:
                print("There are no pending orders to process.")
                continue

            order = order_records.search(order_id)

            if order is None:
                print("Error: Order record could not be found.")
                continue

            order["status"] = "Processed"

            action_history.push({
                "action": "process_order",
                "order": order.copy()
            })

            print(f"Order {order_id} has been processed.")

            
        elif choice == "3":
            records = order_records.display()

            if not records:
                print("No order records found.")
                continue

            print("\n--- ALL ORDER RECORDS ---")

            for order in records:
                print(f"Order ID: {order['order_id']}")
                print(f"Customer: {order['customer']}")
                print(f"Item: {order['item']}")
                print(f"Status: {order['status']}")
                print("-" * 30)


                
        elif choice == "4":
            order_id = input("Enter the order ID to search: ").strip().upper()
            order = order_records.search(order_id)

            if order is None:
                print(f"Order {order_id} was not found.")
            else:
                print("\n--- ORDER DETAILS ---")
                print(f"Order ID: {order['order_id']}")
                print(f"Customer: {order['customer']}")
                print(f"Item: {order['item']}")
                print(f"Status: {order['status']}")

                
        
        elif choice == "5":
            order_id = input(
                "Enter the order ID to delete: "
            ).strip().upper()

            order = order_records.search(order_id)

            if order is None:
                print(f"Order {order_id} was not found.")
                continue

            # Save both original positions before deletion.
            list_position = order_records.index_of(order_id)
            queue_position = order_queue.remove(order_id)

            # Remove the order record from the linked list.
            deleted = order_records.delete(order_id)

            if deleted:
                action_history.push({
                    "action": "delete_order",
                    "order": order.copy(),
                    "list_position": list_position,
                    "queue_position": queue_position
                })

                print(f"Order {order_id} deleted successfully.")
            else:
                print(f"Could not delete order {order_id}.")

                
        elif choice == "6":
            if action_history.is_empty():
                print("There are no actions to undo.")
                continue

            last_action = action_history.pop()
            action_type = last_action["action"]
            order = last_action["order"]
            order_id = order["order_id"]

            if action_type == "add_order":
                order_queue.remove(order_id)
                order_records.delete(order_id)

                print(f"Addition of order {order_id} has been undone.")

            
            elif action_type == "process_order":
                # Find the actual record stored in the linked list.
                current_order = order_records.search(order_id)

                if current_order is not None:
                    current_order["status"] = "Pending"

                    # Restore the order to the front of the queue.
                    order_queue.insert_at(0, order_id)

                    print(
                        f"Processing of order {order_id} "
                        "has been undone."
                    )
                else:
                    print(
                        f"Cannot undo processing: "
                        f"order {order_id} was not found."
                    )

            
            elif action_type == "delete_order":
                # Restore the record to its original list position.
                list_position = last_action["list_position"]
                order_records.insert_at(list_position, order)

                # Restore the order to its original queue position
                # if it was pending when deleted.
                queue_position = last_action["queue_position"]

                if queue_position >= 0:
                    order_queue.insert_at(queue_position, order_id)

                print(
                    f"Deletion of order {order_id} "
                    "has been undone."
                )




        
        elif choice == "7":
            pending_orders = []

            for order_id in order_queue.items():
                order = order_records.search(order_id)

                if order is not None:
                    pending_orders.append(order)

            if not pending_orders:
                print("There are no pending orders.")
                continue

            print("\n--- PENDING ORDERS ---")

            for order in pending_orders:
                print(f"Order ID: {order['order_id']}")
                print(f"Customer: {order['customer']}")
                print(f"Item: {order['item']}")
                print(f"Status: {order['status']}")
                print("-" * 30)

        else:
            print("Invalid choice. Please select an option from 1 to 8.")


if __name__ == "__main__":
    main()
