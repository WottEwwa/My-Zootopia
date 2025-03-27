import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding='utf-8') as handle:
        return json.load(handle)

# Load animals data
animals_data = load_data('animals_data.json')

# Generate animals information as plain text
output = ''
for animal in animals_data:
    output += '<li class="cards__item">'
    output += f"Name: {animal.get('name', 'N/A')}<br/>\n"
    output += f"Diet: {animal.get('characteristics', {}).get('diet', 'N/A')}<br/>\n"
    output += f"Locations: {', '.join(animal.get('locations', ['N/A']))}<br/>\n"
    output += f"Type: {animal.get('characteristics', {}).get('type', 'N/A')}<br/>\n\n"
    output += '</li>'

    print(output)
try:
    # Load template
    with open('animals_template.html', 'r', encoding='utf-8') as template_file:
        template_content = template_file.read()
    
    # Verify placeholder exists
    if '__REPLACE_ANIMALS_INFO__' not in template_content:
        raise ValueError("Template is missing '__REPLACE_ANIMALS_INFO__' placeholder")
    
    # Replace placeholder with generated content
    complete_text = template_content.replace('__REPLACE_ANIMALS_INFO__', output)
    
    # Write output file
    with open('animals.html', 'w', encoding='utf-8') as output_file:
        output_file.write(complete_text)
    
    print("Successfully generated: animals.html")

except FileNotFoundError:
    print("Error: animals_template.html not found")
except Exception as e:
    print(f"An error occurred: {str(e)}")