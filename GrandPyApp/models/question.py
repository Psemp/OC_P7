
class Question:
    def __init__(self, question_target, user_intent, page_id, extract):
        self.target = question_target
        self.intent = user_intent
        self.true_url = f"https://fr.wikipedia.org/?curid={page_id}"
        self.wiki_extract = extract
        self.maplink = None
