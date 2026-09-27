def explain_topic(text):
    if not text.strip():
        return "Please enter a topic to explain."

    return (
        "EduGenie Explanation:\n\n"
        "Here is a simple explanation of your topic:\n\n"
        + text
    )