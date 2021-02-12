
from script.algorithm import identify_intent, string_modification

q1 = "Quelle est la capitale de la France"
q2 = "Ou se trouve le MuCem "
q3 = "Coucou, ou est le golden Gate ?"
q4 = "Hey raconte moi une blague !"
q5 = "Coucou, comment vas tu ?"
q6 = "Quelle est l'année de la révolution francaise"
q7 = "Fais moi rire"
q8 = "Hey"
q9 = "Qui a écrit Le petit Prince"
q10 = "Qui est le président des Etats Unis"


def test_intent():
    assert identify_intent(string_modification(q1)) == "location"
    assert identify_intent(string_modification(q2)) == "location"
    assert identify_intent(string_modification(q3)) == "location"
    assert identify_intent(string_modification(q4)) == "funny"
    assert identify_intent(string_modification(q5)) == "generic"
    assert identify_intent(string_modification(q6)) == "date"
    assert identify_intent(string_modification(q7)) == "funny"
    assert identify_intent(string_modification(q8)) == "generic"
    assert identify_intent(string_modification(q9)) == "person"
    assert identify_intent(string_modification(q10)) == "person"


print(identify_intent(q5))
