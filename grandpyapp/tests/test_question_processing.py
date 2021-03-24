from grandpyapp.script.question_processing import question_processing
from grandpyapp.models.question import Question

from grandpyapp.script.actions_on_str import string_modification
from grandpyapp.script.actions_on_str import data_cleaning, identify_intent
from grandpyapp.script.wikisearch import get_page_info, get_wiki_extract
from grandpyapp.script.maps_search import get_coords, get_embed_map

test_query = "Ou se trouve le Golden Gate ?"
test_question = Question()


def test_question_processing():
    """tests if formatting works, if 'embed map url' is in return --> intent identified correctly"""
    test_html_return = question_processing(test_query, test_question)
    print(test_html_return)
    assert "wikipedia page extract" in test_html_return
    assert "embed map url" in test_html_return
