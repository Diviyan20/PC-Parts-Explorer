from backend.api.cpu_api import fetch_cpu_data
import json

# Fetches the raw CPU data and transforms it so that it's clean and organized
def transform_cpu_data():
    response = fetch_cpu_data() # Fetches data from the API
    
    data = json.loads(response) # Loads response in JSON format
    
    # Loop through the dictionary to retrieve each individual object   
    for cpu_data in data['cpu']:
        
        cpu_brand = cpu_data['brand']
        cpu_model = cpu_data['model']
        cpu_cores = cpu_data['cores']
        
        """
            - Convert both base_clock and boost_clock from huge integers to decimals, but in GHz format
            - Example: 2700000000 = 2.7GHz
            - Added conditional checks for CPUs that have no base or boost clock
        """
        base_clock = cpu_data['base_clock']['cycles'] / 1_000_000_000 if cpu_data['base_clock'] else None
        boost_clock = cpu_data['boost_clock']['cycles'] / 1_000_000_000 if cpu_data['boost_clock'] else None
        
        cpu_tdp = cpu_data['tdp']
        integrated_graphics = cpu_data['integrated_graphics']
        multithreading = cpu_data['multithreading']
        
        """
            - Fetch both the currency and the actual price of the CPU
            - Conditional check for CPUs that have no price
        """
        currency = cpu_data['price'][0] if cpu_data['price'] else None
        price = cpu_data['price'][1] if cpu_data['price'] else None
        
        # Append all fetched values in an array
        components = []
        components.append({
            "brand": cpu_brand,
            "model": cpu_model,
            "cores": cpu_cores,
            "base_clock": f"{base_clock}",
            "boost_clock": f"{boost_clock}",
            "tdp": cpu_tdp,
            "integrated_graphics": integrated_graphics,
            "multithreading": multithreading,
            "currency": currency,
            "price": price
        })
        
        print("Components:", components)
    
    return components    

transform_cpu_data()