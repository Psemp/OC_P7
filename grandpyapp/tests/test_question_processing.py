from grandpyapp.script.question_processing import question_processing
from grandpyapp.models.question import Question

# FUNCTIONS RECREATED TO CONTROL THE ENVIRONMENT OF QUESTION PROCESSING EXECUTION #
# this does not work #


def string_modification(user_query):
    return "ou se trouve le golden gate "


def data_cleaning(clean_string):
    return "golden gate"


def identify_intent(clean_string):
    return "location"


def get_page_info(clean_string):
    return [40490, "Pont du Golden Gate"]


def get_wiki_extract(mock_title):
    return "wikipedia page extract"


def get_coords(target):
    [0, 0]


def get_embed_map(mock_coords):
    return "embed map url"


# FUNCTIONS RECREATED TO CONTROL THE ENVIRONMENT OF QUESTION PROCESSING EXECUTION #

test_query = "Ou se trouve le Golden Gate ?"
test_question = Question()


def test_question_processing():
    """tests if formatting works, if 'embed map url' is in return --> intent identified correctly"""
    test_html_return = question_processing(test_query, test_question)
    print(test_html_return)
    assert "wikipedia page extract" in test_html_return
    assert "embed map url" in test_html_return
