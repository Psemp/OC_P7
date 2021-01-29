import json

# from models.question import Question


with open('resources/intents.json') as f:
    intent_set = json.load(f)

intent_dict = {}

for intent in intent_set:
    intent_dict[intent] = intent_set[intent]

for key in intent_dict:
    print(key, intent_dict[key])


def identify_intent(user_question, intent_dict):
    for key in intent_dict:
        for intent in intent_dict[key]:
            if intent in user_question:
                return intent
            else:
                return "generic"


for key in intent_dict:
    for intent in intent_dict[key]:
        print(intent)
