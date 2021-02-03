import json


# with open('../resources/intents.json') as f:
#     intent_set = json.load(f)

# intent_dict = {}

# for intent in intent_set:
#     intent_dict[intent] = intent_set[intent]


# # TEST

# for key in intent_dict:
#     for intent in intent_dict[key]:
#         print(intent)


# TEST


def identify_intent(user_question, intent_dict):
    for key in intent_dict:
        for intent in intent_dict[key]:
            print(intent)
            if intent in user_question:
                return key
            else:
                return "generic"
