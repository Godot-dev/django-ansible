import requests

API_KEY = "b1b3627c-9aab-4b22-b7d1-a6a71460f38f"

# Créer une session persistante
session = requests.Session()
session.headers.update({
    "Authorization": API_KEY
})

api_base_link = "https://api.sncf.com/v1/coverage/sncf/"

def ask_sncf(service, params=None):
    url = api_base_link + service
    response = session.get(url, params=params, verify=False)

    # Results
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Erreur {response.status_code} : {response.text}")
        return None