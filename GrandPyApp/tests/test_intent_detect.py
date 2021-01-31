import json, pathlib

from static.algorythm import identify_intent

with open('GrandPyApp/static/resources/intents.json') as f:
    intent_set = json.load(f)

intent_dict = {}

for intent in intent_set:
    intent_dict[intent] = intent_set[intent]


question1 = "Quelle est la capitale de la France"
question2 = "Ou se trouve le MuCem "
question3 = "Coucou, ou est le golden Gate "
question4 = "Hey  raconte moi une blague "
question5 = "Coucou, comment vas tu "
question6 = "Quelle est l'année de la révolution francaise"
question7 = "Fais moi rire"
question8 = "Hey"
question9 = "Qui a écrit Le petit Prince "
question10 = "Qui est le président des Etats Unis "

assert identify_intent(question1, intent_dict) == "location"
assert identify_intent(question2, intent_dict) == "location"
assert identify_intent(question3, intent_dict) == "location"
assert identify_intent(question4, intent_dict) == "funny"
assert identify_intent(question5, intent_dict) == "generic"
assert identify_intent(question6, intent_dict) == "date"
assert identify_intent(question7, intent_dict) == "funny"
assert identify_intent(question8, intent_dict) == "generic"
assert identify_intent(question9, intent_dict) == "person"
assert identify_intent(question10, intent_dict) == "person"
