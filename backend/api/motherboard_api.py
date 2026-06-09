from pcpartpicker import API

api = API()

motherboard_data = api.retrieve("motherboard").to_json()

print("Data: ", motherboard_data)