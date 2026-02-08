import requests

def get_cat_fact():
    url = "https://catfact.ninja/fact"
    # Write your code here
    try:
        reponse = requests.get(url)
        reponse.raise_for_status()
        data = reponse.json()
        print(data["fact"])
    except Exception:
        print("Failed to retrieve cat fact.")
get_cat_fact()
