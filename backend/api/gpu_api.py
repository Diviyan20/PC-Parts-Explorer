from pcpartpicker import API

def fetch_gpu_data():
    api = API()
    gpu_data = api.retrieve("video-card").to_json()
    return gpu_data