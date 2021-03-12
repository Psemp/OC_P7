from math import trunc
from grandpyapp.script.actions_on_str import string_modification
from grandpyapp.script.actions_on_str import data_cleaning, identify_intent
from grandpyapp.script.wikisearch import get_page_info
from grandpyapp.script.maps_search import get_coords


q1 = "Quelle est la capitale de la France"
q2 = "Ou se trouve le MuCem "
q3 = "Coucou, ou est la grande muraille de chine ?"
q4 = "Hey raconte moi une blague !"
q5 = "Coucou, comment vas tu ?"
q6 = "Quelle est l'année de la révolution francaise"
q7 = "Fais moi rire"
q8 = "Hey"
q9 = "Qui a écrit Le petit Prince"
q10 = "Qui est le président des Etats Unis"


def test_intent():
    """testing intent detection of 10 test strings"""
    assert identify_intent(string_modification(q1)) == "location"
    assert identify_intent(string_modification(q2)) == "location"
    assert identify_intent(string_modification(q3)) == "location"
    assert identify_intent(string_modification(q4)) == "funny"
    assert identify_intent(string_modification(q5)) is None
    assert identify_intent(string_modification(q6)) == "date"
    assert identify_intent(string_modification(q7)) == "funny"
    assert identify_intent(string_modification(q8)) is None
    assert identify_intent(string_modification(q9)) == "person"
    assert identify_intent(string_modification(q10)) == "person"


test_string = "Ou EST le GoldEN Gate !??"

test_clean_string = string_modification(test_string)
test_usr_intent = identify_intent(test_clean_string)
test_target = data_cleaning(test_clean_string)
test_wiki_page = get_page_info(test_target)
test_wiki_url = f"https://fr.wikipedia.org/?curid={test_wiki_page[0]}"
test_coordinates = get_coords(test_target)


def test_question_intent():
    """test intent detection of test_string"""
    assert test_usr_intent == "location"


def test_target_attribution():
    """test if target matches prediction"""
    assert test_target == "golden gate"


def test_data_cleaning():
    """tests if test string punctuation/accents and caps are removed"""
    assert test_clean_string == "ou est le golden gate "


def test_wiki():
    """tests if wiki url requested from API points to Golden Gate wiki page"""
    assert test_wiki_url == "https://fr.wikipedia.org/?curid=40490"


def test_maps_coordinates():
    """tests if the coordinates returned by google maps API are roughly the same"""
    """as the ones found on www.gps-latitude-longitude.com for test_target"""
    """golden gate bridge is approximately 37 lat / -122 lon, we use math.trunc to discard the decimals"""
    assert trunc(test_coordinates[0]) == 37
    assert trunc(test_coordinates[1]) == -122


test_intent()
test_question_intent()
test_target_attribution()
test_data_cleaning()
test_wiki()
test_maps_coordinates()
