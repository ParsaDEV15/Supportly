from mongo_setup import MongoSetup
from config.settings import ORDER_COLLECTION

mongo_setup = MongoSetup()


def create_order_info():
    full_name = input('Full name: ')
    supply_name = input('Supply name: ')

    while True:
        try:
            total_amount = int(input('Total amount($): '))
            break
        except ValueError:
            print("Invalid number. Please enter an integer.")

    order_status = input('Order status: ')

    return {
        "full_name": full_name,
        "supply_name": supply_name,
        "total_amount($)": total_amount,
        "order_status": order_status
    }


def create_order(order_data: dict):
    mongo_setup.insert_one_document(
        collection_name=ORDER_COLLECTION,
        data=order_data
    )


def get_orders_info():
    docs = list(mongo_setup.find_all_docs(collection_name=ORDER_COLLECTION, query={}))

    if len(docs) != 0:
        for doc in docs:
            print(f"""
            ────────── ORDER ──────────
            Name:          {doc['full_name']}
            Supply:        {doc['supply_name']}
            Total Amount($):  {doc['total_amount($)']}
            Status:        {doc['order_status']}
            ────────────────────────────
            """)
    else:
        print("No orders found.")


if __name__ == '__main__':
    while True:
        response = input('\nDo you want to (c)create order, get orders (i)info or (e)exit? ')

        match response.lower():
            case 'c':
                print("\nCreating new order...")
                print("\nDon't leave anything empty!")
                order_data = create_order_info()
                create_order(order_data)
                print("\nOrder created successfully.")

            case 'i':
                get_orders_info()

            case 'e':
                print("\nExiting...")
                break

            case _:
                print("Invalid choice. Please enter c or e.")

    # mongo_setup.delete_all_docs(collection_name=COLLECTION_NAME, query={})