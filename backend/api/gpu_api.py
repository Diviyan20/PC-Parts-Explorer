from pcpartpicker import API

api = API()

gpu_data = api.retrieve("video-card").to_json()

print("Data: ", gpu_data)