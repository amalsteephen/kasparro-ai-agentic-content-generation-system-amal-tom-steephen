class ComparisonAgent:
    """
    Agent responsible for generating a structured comparison
    between the main product and a fictional competitor.
    """

    def generate(self, product_a: dict) -> dict:
        product_b = {
            "name": "RadiantC Serum",
            "ingredients": ["Vitamin C", "Niacinamide"],
            "benefits": ["Glow enhancement"],
            "price_inr": 799
        }

        comparison = {
            "product_a": {
                "name": product_a["name"],
                "ingredients": product_a["ingredients"],
                "benefits": product_a["benefits"],
                "price_inr": product_a["price_inr"]
            },
            "product_b": product_b
        }

        return {
            "page_type": "Comparison Page",
            "comparison": comparison
        }
