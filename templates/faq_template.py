class FAQTemplate:
    def build(self, questions: dict, content_blocks: dict) -> dict:
        faqs = []

        for category, qs in questions.items():
            for q in qs:
                answer = "Refer to product details for more information."
                faqs.append({
                    "category": category,
                    "question": q,
                    "answer": answer
                })

        return {
            "page_type": "FAQ",
            "faqs": faqs
        }
