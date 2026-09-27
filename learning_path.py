def recommend_learning_path(topic):
    if not topic.strip():
        return "Please enter a topic for learning recommendations."

    return (
        "EduGenie Learning Path:\n\n"
        "Topic:\n"
        + topic
        + "\n\n"
        "Beginner → Intermediate → Advanced\n\n"
        "This is the Learning Path module response."
    )