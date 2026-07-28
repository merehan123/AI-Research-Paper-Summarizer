from src.llm.inference import classify_request
from src.services.greeting import greeting
from src.services.summarizer import generate_summary
from src.services.contributions import extract_contributions
from src.services.explanation import explain_concepts
from src.services.qa_service import answer_question

def research_assistant(
    user_request: str,
    paper_text: str,
    vector_store,
):
    """
    Main routing function.
    """

    intent = classify_request(user_request)

    print(f"\nDetected Intent: {intent}\n")

    if intent == "GREETING":
        return greeting(user_request)

    elif intent == "SUMMARY":
        return generate_summary(
            paper_text
        )

    elif intent == "CONTRIBUTIONS":
        return extract_contributions(
            paper_text
        )

    elif intent == "CONCEPTS":
        return explain_concepts(
            user_request,
            paper_text,
        )

    elif intent == "QUESTION":
        return answer_question(
            question=user_request,
            vector_store=vector_store,
        )

    else:
        return "Unable to classify the request."