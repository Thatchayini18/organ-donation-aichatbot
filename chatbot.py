import knowledge as kb

def chatbot_response(user_input):
    text = user_input.lower()

    if "donor" in text or "donate" in text:
        return kb.donor_info()

    elif "recipient" in text or "patient" in text:
        return kb.recipient_info()

    elif "register" in text or "signup" in text:
        return kb.registration_help()

    elif "match" in text or "matching" in text:
        return kb.matching_info()

    else:
        return kb.general_help()
