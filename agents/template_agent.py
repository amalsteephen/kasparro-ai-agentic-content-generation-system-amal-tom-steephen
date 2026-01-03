class TemplateAssemblyAgent:
    def __init__(self, bus):
        self.bus = bus

    def decide(self):
        return (
            self.bus.has("questions")
            and self.bus.has("logic_blocks")
            and not self.bus.has("pages")
        )

    def act(self):
        pages = {
            "faq_page": self.bus.read("questions"),
            "product_page": self.bus.read("logic_blocks")
        }

        self.bus.publish("pages", pages)
