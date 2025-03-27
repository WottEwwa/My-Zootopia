import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

for animal in animals_data:
  print(f"Name: {animal.get('name', 'N/A')}")
  print(f"Diet: {animal.get('characteristics', {}).get('diet', 'N/A')}")
  
  # location array
  locations = animal.get('locations', [])
  print(f"Locations: {', '.join(locations) if locations else 'N/A'}")

  print(f"Type: {animal.get('characteristics', {}).get('type', 'N/A')}")
  print()