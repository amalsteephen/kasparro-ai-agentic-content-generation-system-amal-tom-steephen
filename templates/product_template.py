class ProductPageTemplate:
    def build(self, product: dict, content_blocks: dict) -> dict:
        return {
            "page_type": "Product Page",
            "product_name": product["name"],
            "ingredients": content_blocks["ingredients_block"]["ingredients"],
            "benefits": content_blocks["benefits_block"]["primary_benefits"],
            "usage": content_blocks["usage_block"]["instructions"],
            "side_effects": content_blocks["safety_block"]["side_effects"],
            "price_inr": content_blocks["price_block"]["price_inr"]
        }
