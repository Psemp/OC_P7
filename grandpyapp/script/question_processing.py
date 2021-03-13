import json
import random

from .actions_on_str import string_modification
from .actions_on_str import data_cleaning, identify_intent
from .wikisearch import get_page_info, get_wiki_extract
from .maps_search import get_coords, get_embed_map


def question_processing(user_query, user_question):
    """returns html code w/ all relevant data for usr"""
    with open("grandpyapp/resources/humanization.json") as f:
        humanization = json.load(f)

    quote_list = humanization["quotes"]
    quote = random.choice(quote_list)
    clean_string = string_modification(user_query)
    wiki_page_info = get_page_info(clean_string)

    user_question.intent = identify_intent(clean_string)
    user_question.target = data_cleaning(clean_string)
    user_question.wiki_extract = get_wiki_extract(wiki_page_info[1])
    user_question.true_url = f"https://fr.wikipedia.org/?curid={wiki_page_info[0]}"

    if user_question.intent == "location":
        coords = get_coords(user_question.target)
        user_question.maplink = get_embed_map(coords)

    if user_question.intent != "location":
        html_return = f"""<span >{quote} {user_question.wiki_extract} -- <br>
        <a href="{user_question.true_url}" target="_blank" style="color:white">Tu peux en savoir plus ici !</a>
        </span>"""
    elif user_question.intent == "location":
        html_return = f"""<span >{quote} {user_question.wiki_extract} -- <br>
        <a href="{user_question.true_url}" target="_blank" style="color:white">Tu peux en savoir plus ici !</a>
        <br><img src="{user_question.maplink}" alt="Map Image" width="400" height="400"></span>"""

    return html_return
