import requests
import os


def get_coords(target):
    """returns list of coordinates (lat/lon) of target on Google Place"""
    key = os.environ.get('GOOGLE_KEY')
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={target}&key={key}"

    try:
        r = requests.get(url, timeout=2.000)
        result = r.json()
        return extract_coordinates(result)

    except requests.ConnectionError:
        print("Connection error, make sure you are connected to internet")
    except requests.Timeout:
        print("Request has timed out")
    except requests.RequestException:
        print("A general error has been found")


def get_embed_map(coords):
    """returns link of image map centered at coords"""
    key = os.environ.get('GOOGLE_KEY')
    lat = coords[0]
    lon = coords[1]
    map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lon}&zoom=15&size=400x400&key={key}"
    return map_url


def extract_coordinates(result):
    lat = result["results"][0]["geometry"]["location"]["lat"]
    lon = result["results"][0]["geometry"]["location"]["lng"]
    coordinates = [lat, lon]
    return coordinates
