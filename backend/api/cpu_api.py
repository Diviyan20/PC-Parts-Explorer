from pcpartpicker import API

def fetch_cpu_data():
    api = API()
    cpu_data = api.retrieve("cpu").to_json()
    return cpu_data