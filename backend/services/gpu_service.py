from backend.api.gpu_api import fetch_gpu_data
import json

"""
    - Fetches raw GPU data and performs data cleaning
    - Uses the same format as fetching CPU data
"""

def transform_gpu_data():
    try:
        response = fetch_gpu_data()
        data = json.loads(response)

        specs = []
    
        for gpu_data in data['video-card']:
            brand = gpu_data['brand']
            model = gpu_data['model']
            chipset = gpu_data['chipset']
            
            vram = gpu_data['vram']['total'] / 1_000_000_000 if gpu_data['vram'] else None
            core_clock = gpu_data['core_clock']['cycles'] / 1_000_000_000 if gpu_data['core_clock'] else None
            boost_clock = gpu_data['boost_clock']['cycles'] / 1_000_000_000 if gpu_data['boost_clock'] else None
            
            color = gpu_data['color']
            length = gpu_data['length']
            
            currency = gpu_data['price'][0] if gpu_data['price'] else None
            price = gpu_data['price'][1] if gpu_data['price'] else None
            
            
            specs.append({
                "brand": brand,
                "model": model,
                "chipset": chipset,
                "vram": vram,
                "core_clock": core_clock,
                "boost_clock": boost_clock,
                "color": color,
                "length": length,
                "currency": currency,
                "price": price
            })
            
        formatted_specs = json.dumps(specs, indent=2)
        print("GPU Components: ", formatted_specs)
        
        return formatted_specs
    
    except Exception as e:
        raise ValueError("Error cleaning Data:", e)

transform_gpu_data()