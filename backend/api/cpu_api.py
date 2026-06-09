from pcpartpicker import API

api = API()

cpu_data = api.retrieve("cpu").to_json()

print("Data: ", cpu_data)