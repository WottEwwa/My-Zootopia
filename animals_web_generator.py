import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding='utf-8') as handle:
        return json.load(handle)


# Load animals data
animals_data = load_data('animals_data.json')

def serialize_animal(animal_obj):
    """Serialize an animal object to HTML"""
    output = ''

    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_obj.get("name", "N/A")}</div>\n'

    output += '<div class="card__text">\n'
    output += '<ul>\n'
    output += f'<li><strong>Diet:</strong> {animal_obj.get("characteristics", {}).get("diet", "N/A")}</li>\n'
    output += f'<li><strong>Locations:</strong> {", ".join(animal_obj.get("locations", ["N/A"]))}</li>\n'
    output += f'<li><strong>Type:</strong> {animal_obj.get("characteristics", {}).get("type", "N/A")}</li>\n'
    output += '</ul>\n'
    output += '</div>\n'

    # Characteristic details
    characteristic = animal_obj.get("characteristics", {})
    if characteristic:
        output += '<details>\n'
        output += '<summary>Additional characteristics</summary>\n'
        output += '<ul>\n'
        
        for key, value in characteristic.items():
            if key not in ["diet", "type"]:
                output += f'<li><strong>{key.replace("_", " ").title()}:</strong> {value}</li>\n'
        
        output += '</ul>\n'
        output += '</details>\n'

    # Taxonomy details
    taxonomy = animal_obj.get("taxonomy", {})
    if taxonomy:
        output += '<details>\n'
        output += '<summary>Taxonomic classification</summary>\n'
        output += '<ul>\n'
        output += '<li><strong>Kingdom:</strong> {}</li>\n'.format(taxonomy.get("kingdom", "N/A"))
        output += '<li><strong>Phylum:</strong> {}</li>\n'.format(taxonomy.get("phylum", "N/A"))
        output += '<li><strong>Class:</strong> {}</li>\n'.format(taxonomy.get("class", "N/A"))
        output += '<li><strong>Order:</strong> {}</li>\n'.format(taxonomy.get("order", "N/A"))
        output += '<li><strong>Family:</strong> {}</li>\n'.format(taxonomy.get("family", "N/A"))
        output += '<li><strong>Genus:</strong> {}</li>\n'.format(taxonomy.get("genus", "N/A"))
        output += '<li><strong>Scientific Name:</strong> {}</li>\n'.format(taxonomy.get("scientific_name", "N/A"))
        output += '</ul>\n'
        output += '</details>\n'

    output += '</div></li>\n'

    return output


output = ''
for animal_obj in animals_data:
    output += serialize_animal(animal_obj)

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