
import json
from script.algorythm import identify_intent, string_modification

with open('resources/intents.json') as f:
    intent_set = json.load(f)

intent_dict = {}

for intent in intent_set:
    intent_dict[intent] = intent_set[intent]


q1 = "Quelle est la capitale de la France"
q2 = "Ou se trouve le MuCem "
q3 = "Coucou, ou est le golden Gate ?"
q4 = "Hey  raconte moi une blague !"
q5 = "Coucou, comment vas tu ?"
q6 = "Quelle est l'année de la révolution francaise"
q7 = "Fais moi rire"
q8 = "Hey"
q9 = "Qui a écrit Le petit Prince "
q10 = "Qui est le président des Etats Unis "


def test_intent(intent_dict):
    assert identify_intent(string_modification(q1), intent_dict) == "location"
    assert identify_intent(string_modification(q2), intent_dict) == "location"
    assert identify_intent(string_modification(q3), intent_dict) == "location"
    assert identify_intent(string_modification(q4), intent_dict) == "funny"
    assert identify_intent(string_modification(q5), intent_dict) == "generic"
    assert identify_intent(string_modification(q6), intent_dict) == "date"
    assert identify_intent(string_modification(q7), intent_dict) == "funny"
    assert identify_intent(string_modification(q8), intent_dict) == "generic"
    assert identify_intent(string_modification(q9), intent_dict) == "person"
    assert identify_intent(string_modification(q10), intent_dict) == "person"


test_intent(intent_dict)
