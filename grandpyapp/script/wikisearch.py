import requests


def get_page_info(user_query):
    """makes a request on wikipedia API and returns list[pageid, page title]"""
    url = f"https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch={user_query}&utf8=&format=json"
    try:
        r = requests.get(url, timeout=1.000)
        result = r.json()
        page_title = (result["query"]["search"][0]["title"])
        page_id = (result["query"]["search"][0]["pageid"])
        wiki_list = [page_id, page_title]
        return wiki_list
    except requests.ConnectionError:
        print("Connection error, make sure you are connected to internet")
    except requests.Timeout:
        print("Request has timed out")
    except requests.RequestException:
        print("A general error has been found")


def get_wiki_extract(page_title):
    """makes a request on wiki API and returns an extract of the article of {page title}"""
    url = f"https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&exsentences=3&exlimit=1&titles={page_title}&explaintext=1&formatversion=2&format=json"
    try:
        r = requests.get(url, timeout=1.000)
        result = r.json()
        return result["query"]["pages"][0]["extract"]

    except requests.ConnectionError:
        print("Connection error, make sure you are connected to internet")
    except requests.Timeout:
        print("Request has timed out")
    except requests.RequestException:
        print("A general error has been found")
