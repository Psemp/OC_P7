class Question:
    def __init__(self, user_input):
        self.question = user_input.lower()
        self.intent = "generic"
        self.target = "generic"
        self.answer = "generic"
