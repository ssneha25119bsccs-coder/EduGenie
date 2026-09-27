def generate_quiz(topic):
    if not topic.strip():
        return "Please enter a topic for the quiz."

    return {
        "topic": topic,
        "questions": [
            {
                "question": "What is Python?",
                "options": [
                    "A programming language",
                    "A database",
                    "An operating system",
                    "A web browser"
                ],
                "answer": "A programming language"
            },
            {
                "question": "Which symbol is used for comments in Python?",
                "options": [
                    "#",
                    "//",
                    "/* */",
                    "<!-- -->"
                ],
                "answer": "#"
            },
            {
                "question": "Which function is used to display output in Python?",
                "options": [
                    "print()",
                    "show()",
                    "display()",
                    "output()"
                ],
                "answer": "print()"
            }
        ]
    }