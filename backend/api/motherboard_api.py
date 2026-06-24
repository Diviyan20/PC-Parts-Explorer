from pcpartpicker import API

def fetch_motherboard_data():
    api = API()

    motherboard_data = api.retrieve("motherboard").to_json()
    return motherboard_data