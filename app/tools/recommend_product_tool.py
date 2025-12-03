from langchain_core.tools import Tool
from db.mongo_setup import MongoSetup
from config.settings import PRODUCT_COLLECTION

mongo_setup = MongoSetup()


def recommend_product(product_tag: str):
    product_tag = product_tag.lower().strip()

    products_result = mongo_setup.find_all_docs(
        collection_name=PRODUCT_COLLECTION,
        query={"tags": {"$in": [product_tag]}},
    )

    if not products_result:
        return "No products found that match this category."

    products_info = ''

    for i, product in enumerate(products_result, 1):
        products_info += f"""
        
{i}.{product['name']}
Product description: {product['description']}
Product Price: {product['price']}$
"""

    return products_info


recommend_product_tool = Tool(
    name="recommend_product",
    description="Use this tool to recommend products based on a category or usage keyword.",
    func=recommend_product
)