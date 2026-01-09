def chatbot_response(user_input):
    text = user_input.lower()

    if "organ donation" in text:
        return "Organ donation is the process of donating organs to save lives."

    elif "donor" in text:
        return "A donor is a person who voluntarily donates an organ."

    elif "recipient" in text:
        return "A recipient is a patient waiting to receive an organ."

    elif "matching" in text:
        return "Organ matching is based on blood group, urgency, and compatibility."

    elif "priority" in text:
        return "Recipients are prioritized based on urgency and waiting time."

    else:
        return "Sorry, I can answer only organ donation related questions."
