# Dataset Creation via LLM / Custom Documents

1. Create .env file with your OpenAI key (or change to local LLM in code)
2. Set directory paths and save names in main.py, parse_docs.py, and create_datasets.py
3. Run main.py attended to ensure no initial issues (once the dataset creation begins, it will create the JSON file and append as it goes, so you can check it during the process to make sure it's working).
4. After completion, run cleandataset.py against the JSON file to clean up leading and trailing whitespace and identify any entries without the full input/instruction/output keys.

Can be easily updated to create different dataset types by editing the Pydantic classes in create_datasets.py and the secondary prompt.
