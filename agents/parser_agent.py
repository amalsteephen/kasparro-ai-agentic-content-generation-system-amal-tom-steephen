class ProductParserAgent:
    def __init__(self, bus):
        self.bus = bus

    def decide(self):
        return self.bus.exists("raw_product")

    def act(self):
        raw = self.bus.read("raw_product")

        parsed = {
            "name": raw.get("product_name"),
            "benefits": raw.get("benefits"),
            "usage": raw.get("how_to_use"),
            "ingredients": raw.get("key_ingredients"),
            "price_inr": raw.get("price")
        }

        self.bus.publish("parsed_product", parsed)
