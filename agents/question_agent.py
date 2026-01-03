class QuestionGenerationAgent:
    def __init__(self, bus):
        self.bus = bus

    def decide(self):
        return self.bus.has("parsed_product") and not self.bus.has("questions")

    def act(self):
        product = self.bus.read("parsed_product")
       

        questions = {
            "informational": [
                f"What is {product['name']}?",
                f"What ingredients are used in {product['name']}?"
            ],
            "usage": [
                f"How should {product['name']} be used?"
            ],
            "safety": [
                f"Is {product['name']} safe for sensitive skin?"
            ]
        }

        self.bus.publish("questions", questions)
