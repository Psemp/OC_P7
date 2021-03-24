import grandpyapp.script.question_processing as qp
from grandpyapp.models.question import Question

import grandpyapp.tests.mocks.mock_actions_on_str
import grandpyapp.tests.mocks.mock_map_search
import grandpyapp.tests.mocks.mock_wikisearch


qp.string_modification = grandpyapp.tests.mocks.mock_actions_on_str.string_modification
qp.data_cleaning = grandpyapp.tests.mocks.mock_actions_on_str.data_cleaning
qp.identify_intent = grandpyapp.tests.mocks.mock_actions_on_str.identify_intent
qp.get_page_info = grandpyapp.tests.mocks.mock_wikisearch.get_page_info
qp.get_wiki_extract = grandpyapp.tests.mocks.mock_wikisearch.get_wiki_extract
qp.get_coords = grandpyapp.tests.mocks.mock_map_search.get_coords
qp.get_embed_map = grandpyapp.tests.mocks.mock_map_search.get_embed_map

test_query = "Ou se trouve le Golden Gate ?"
test_question = Question()


def test_question_processing():
    """tests if formatting works, if 'embed map url' is in return --> intent identified correctly"""
    test_html_return = qp.question_processing(test_query, test_question)
    print(test_html_return)
    assert "wikipedia page extract" in test_html_return
    assert "embed map url" in test_html_return
