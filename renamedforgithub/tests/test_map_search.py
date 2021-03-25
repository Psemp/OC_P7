import json
import os

from grandpyapp.script.maps_search import extract_coordinates, get_embed_map

key = os.environ.get('GOOGLE_KEY')

with open('grandpyapp/tests/mocks/golden_gate_request_map.json') as f:
    mock_maps = json.load(f)

coordinates = extract_coordinates(mock_maps)
formatted_url = get_embed_map(coordinates)
test_url = f'https://maps.googleapis.com/maps/api/staticmap?center=37.8199286,-122.4782551&zoom=15&size=400x400&key={key}'


def test_extraction():
    assert coordinates == [37.8199286, -122.4782551]


def test_url_formatting():
    assert formatted_url == test_url


test_extraction()
test_url_formatting()
