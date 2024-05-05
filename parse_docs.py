from unstructured.partition.pdf import partition_pdf
import create_datasets as cd
from unstructured.staging.base import convert_to_dict

def parse(files):
    for file in files:
        try:
            table_and_text_elements = partition_pdf(
                filename=str(file),  # Convert the Path object to a string
                extract_images_in_pdf=False,
                infer_table_structure=True,
                chunking_strategy="by_title",  # Uses title elements to identify sections within the document for chunking
                max_characters=3000,
                new_after_n_chars=1500,
                combine_text_under_n_chars=1000,
            )
            yield table_and_text_elements
        except Exception as e:
            print(f"An error occurred: {e}")
            yield []  # Yield an empty list if an error occurs