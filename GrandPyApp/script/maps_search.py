import requests


def get_coords(target):
    """returns list of coordinates (lat/lon) of target on Google Place"""
    key = "AIzaSyAZsG6c0kXUbEbztvmFY2FGed8BXtDLCcc"
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={target}&key={key}"
    r = requests.get(url)
    result = r.json()
    lat = result["results"][0]["geometry"]["location"]["lat"]
    lon = result["results"][0]["geometry"]["location"]["lng"]
    coordinates = [lat, lon]
    return coordinates


def get_embed_map(coords):
    """returns link of image map centered at coords"""
    key = "AIzaSyAZsG6c0kXUbEbztvmFY2FGed8BXtDLCcc"
    lat = coords[0]
    lon = coords[1]
    map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lon}&zoom=15&size=400x400&key={key}"
    return map_url
