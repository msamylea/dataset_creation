import json

data_files = "path/to/files.json"
with open(data_files, 'r', encoding='utf-8') as f:
    data = json.load(f)

cleaned_data = []
for i, item in enumerate(data):
    # Remove leading and trailing whitespaces from keys
    cleaned_item = {k.strip(): v for k, v in item.items()}
    
    if not all(key in cleaned_item for key in ('input', 'instruction', 'output')):
        print(f"Dictionary at index {i} does not contain 'input', 'instruction', and 'output' keys.")
        print(cleaned_item)
    else:
        cleaned_data.append(cleaned_item)

# Save the cleaned data to a new JSON file
with open('cleaned_file.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned_data, f)