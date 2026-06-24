from backend.api.motherboard_api import fetch_motherboard_data
import json

def transform_motherboard_data():
    response = fetch_motherboard_data()
    data = json.loads(response)

    specs = []
    try:

        for motherboard_data in data['motherboard']:
            brand = motherboard_data['brand']
            model = motherboard_data['model']
            socket = motherboard_data['socket']
            form_factor = motherboard_data['form_factor']

            ram_slots = motherboard_data['ram_slots']
            max_ram = motherboard_data['max_ram']['total'] / 1_000_000_000 if motherboard_data['max_ram'] else None

            color = motherboard_data['color']

            currency = motherboard_data['price'][0] if motherboard_data['price'] else None
            price = motherboard_data['price'][1] if motherboard_data['price'] else None

        
            specs.append({
                "brand": brand,
                "model": model,
                "socket": socket,
                "form_factor": form_factor,
                "ram_slots" : ram_slots,
                "max_ram" : max_ram,
                "color": color,
                "currency" : currency,
                "price": price
            })
        
        formatted_specs = json.dumps(specs, indent=2)
        print(f"Motherboard Components:{formatted_specs}")
        return formatted_specs
    
    except Exception as e:
        raise ValueError("Error cleaning data:", e)

transform_motherboard_data()