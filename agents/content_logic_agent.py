class ContentLogicAgent:
    def __init__(self, bus):
        self.bus = bus

    def decide(self):
        return self.bus.exists("parsed_product")

    def act(self):
        product = self.bus.read("parsed_product")

        logic_blocks = {
            "benefits": product.get("benefits", []),
            "usage": product.get("usage"),
            "ingredients": product.get("ingredients", []),
            "price": product.get("price_inr")
        }

        self.bus.publish("logic_blocks", logic_blocks)
