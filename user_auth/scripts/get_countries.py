import requests

def get_world_places() -> dict:
    """ Makes an API call that returns a list of countries and their respective states.

    Returns:
        dict: A dict with countries as keys and a list of states as values
    """

    url = "https://countriesnow.space/api/v0.1/countries/states"

    response = requests.get(url).json()

    data = { place["name"]: [state["name"] for state in place["states"]] for place in response["data"] }
    
    return data
