
def remove_punctuation(phrase):
    """returns a phrase without punctuation or special characters"""
    punctuation = '''!'()-[];:",<>./?@#$%^&*_~'''
    corrected_phrase = ""

    for character in phrase:
        if character not in punctuation:
            corrected_phrase = corrected_phrase + character

    return corrected_phrase


def remove_accents(phrase):
    """returns a string with accents removed"""
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
    """returns a string (phrase) whitout punctuation, accents or caps"""
    phrase = phrase.lower()
    phrase = remove_punctuation(phrase)
    phrase = remove_accents(phrase)
    return(phrase)


def subfinder(large_list, sublist):
    """looks for a pattern(sublist) into largelist and returns True if pattern found"""
    matches = []

    for i in range(len(large_list)):
        if large_list[i] == sublist[0] and large_list[i:i+len(sublist)] == sublist:
            matches.append(sublist)

    if len(matches) >= 1:
        return True
    else:
        return False


def identify_intent(user_question):
    """returns the intent found in user_question by using subfinder() on a json file"""
    import json

    with open("resources/intents.json") as f:
        intent_set = json.load(f)

    intent_dict = {}

    for intent in intent_set:
        intent_dict[intent] = intent_set[intent]

    for key in intent_dict:
        for intent in intent_dict[key]:
            if subfinder(user_question.split(), intent.split()) is True:
                return key


def data_cleaning(user_question):
    """returns a string without stopwords contained in stopwords-fr.json"""
    import json

    with open("resources/stopwords-fr.json") as f:
        stopwords = json.load(f)

    user_question = user_question.split()
    corrected_phrase_list = []

    for word in user_question:
        if word not in stopwords:
            corrected_phrase_list.append(word)
    corrected_phrase = " ".join(str(x) for x in corrected_phrase_list)

    return corrected_phrase
