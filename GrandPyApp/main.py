from models.question import Question
from script.algorithm import data_cleaning, identify_intent, string_modification
from script.wikisearch import get_wiki_extract, get_page_info

test_string = "Qui a ecrit le Petit Prince ?"

clean_string = string_modification(test_string)
test_intent = identify_intent(clean_string)
test_target = data_cleaning(clean_string)

print(clean_string)
print(test_intent)
print(test_target)

info_list = get_page_info(test_target)
wiki_extract = get_wiki_extract(info_list[1])

test_question = Question(test_target, test_intent, info_list[0], wiki_extract)

print(test_question.true_url)
print(test_question.wiki_extract)
