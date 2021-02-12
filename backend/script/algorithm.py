
def remove_punctuation(phrase):

    punctuation = '''!()-[];:",<>./?@#$%^&*_~'''
    corrected_phrase = ""

    for character in phrase:
        if character not in punctuation:
            corrected_phrase = corrected_phrase + character

    return corrected_phrase


def remove_accents(phrase):

    corrected_phrase = ""

    for character in phrase:
        if character == "é" or character == "è" or character == "ê":
            corrected_phrase = corrected_phrase + "e"
        elif character == "à":
            corrected_phrase = corrected_phrase + "a"
        elif character == "ù":
            corrected_phrase = corrected_phrase + "u"
        else:
            corrected_phrase = corrected_phrase + character

    return corrected_phrase


def string_modification(phrase):
    phrase = phrase.lower()
    phrase = remove_punctuation(phrase)
    phrase = remove_accents(phrase)
    return(phrase)


def identify_intent(user_question):
    import json

    with open('resources/intents.json') as f:
        intent_set = json.load(f)

    intent_dict = {}

    for intent in intent_set:
        intent_dict[intent] = intent_set[intent]

    for key in intent_dict:
        for intent in intent_dict[key]:
            if (user_question.find(intent) == -1):
                continue
            else:
                print(key)
                return key


def data_cleaning(user_question):
    import json

    with open('resources/stopwords-fr.json') as f:
        stopwords = json.load(f)

    user_question = user_question.split()
    corrected_phrase_list = []

    for word in user_question:
        if word not in stopwords:
            corrected_phrase_list.append(word)
    corrected_phrase = " ".join(str(x) for x in corrected_phrase_list)

    return corrected_phrase
