import traceback
import parse_docs as pd
import create_datasets as cd
import json
from pathlib import Path

directory = Path("path/to/files")
files = list(directory.glob("*.pdf"))  # Get a list of PDF files in the directory

policy_docs = []
datasets = []

for file in files:
    try:
        print(f"Processing file: {file}")
        file_data = pd.parse([file])  # Pass the file path as a list
        
        for data in file_data:
            for element in data:
                if isinstance(element, str):
                    raw_text = element
                elif isinstance(element, dict):
                    raw_text = element.get('text', '')
                elif hasattr(element, 'text'):  # Check if element has a 'text' attribute
                    raw_text = element.text
                else:
                    continue
                
                print("Raw text:", raw_text[:100])
                policy_doc = cd.perform_extraction(raw_text)
                policy_doc_dict = policy_doc.dict()  # Convert PolicyDoc to dictionary
                policy_docs.append(policy_doc_dict)
                
                # Generate the dataset for the current policy document
                dataset = cd.perform_secondary_extraction([policy_doc])
                datasets.extend(dataset)
                
                # Save the policy documents to a JSON file
                with open("docs.json", "w") as f:
                    json.dump(policy_docs, f)
                print("Saved policy docs to docs.json")
                
                # Save the datasets to a JSON file
                with open("dataset.json", "w") as f:
                    json.dump(datasets, f)
                print("Saved dataset to dataset.json")
    except Exception as e:
        print(f"Error processing file {file}: {e}")
        traceback.print_exc()  # Print full exception traceback