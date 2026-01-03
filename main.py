from agents.event_bus import EventBus
from agents.parser_agent import ProductParserAgent
from agents.question_agent import QuestionGenerationAgent
from agents.content_logic_agent import ContentLogicAgent
from agents.template_agent import TemplateAssemblyAgent
from agents.orchestrator import OrchestratorAgent
from data.product_data import RAW_PRODUCT_DATA
import json
import os

def main():
    bus = EventBus()
    bus.publish("raw_product", RAW_PRODUCT_DATA)

    agents = [
        ProductParserAgent(bus),
        QuestionGenerationAgent(bus),
        ContentLogicAgent(bus),
        TemplateAssemblyAgent(bus)
    ]

    orchestrator = OrchestratorAgent(agents, bus)
    orchestrator.run()

    # 🔽 SAVE OUTPUTS (PROOF OF EXECUTION)
    pages = bus.read("pages")

    os.makedirs("outputs", exist_ok=True)

    with open("outputs/faq.json", "w") as f:
        json.dump(pages["faq_page"], f, indent=2)

    with open("outputs/product_page.json", "w") as f:
        json.dump(pages["product_page"], f, indent=2)

    print("✅ Content generation completed successfully.")

if __name__ == "__main__":
    main()
