from langchain_core.tools import Tool
from db.mongo_setup import MongoSetup
from config.settings import ORDER_COLLECTION


def get_order_status(full_name: str) -> str:
    mongo_setup = MongoSetup()

    order_result = mongo_setup.find_one_doc(
        collection_name=ORDER_COLLECTION,
        query={'full_name': full_name}
    )

    if order_result is None:
        return "No order found"

    order_status = order_result['order_status']
    return order_status


get_order_status_tool = Tool(
    name='get_order_status',
    description='Use this tool to get the order status of an order using the customer full name.',
    func=get_order_status
)