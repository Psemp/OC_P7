import json

from grandpyapp.script.wikisearch import extract_infos, extract_sentences

with open('grandpyapp/tests/mocks/golden_gate_request_wiki.json') as f:
    mock_wiki = json.load(f)

with open('grandpyapp/tests/mocks/golden_gate_request_wiki_extract.json') as f:
    mock_extract = json.load(f)

with open('grandpyapp/tests/mocks/golden_gate_3_sentences.json') as f:
    mock_sentences = json.load(f)

test_infos = extract_infos(mock_wiki)
test_sentences = extract_sentences(mock_extract)


def test_extract_info():
    print("mock")
    assert test_infos == [40490, "Pont du Golden Gate"]


def test_extract_sentences():
    assert test_sentences == mock_sentences
