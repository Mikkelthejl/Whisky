import json
import os

class Filehandler:
    def __init__(self):
        self.sites = []
    
    async def initialize(self):
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            json_path = os.path.join(script_dir,"sites.json")
            with open(json_path, "r") as file:
                
                self.sites = json.load(file)
                
        except FileNotFoundError:
            print("Fejl: 'sites.json' findes ikke")
        except json.JSONDecodeError:
            print("Fejl: kunne ikke afkode JSON")