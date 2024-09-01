# Chapter 10
## Training an Entity Linker Model with spaCy

1. [create_kb.py](create_kb.py)
2. [prepare_training_data.py](prepare_training_data.py)
3. `python3 -m spacy train ./config.cfg --output entity_linking_taylor --paths.train ./nel_taylor/train.spacy --paths.dev ./nel_taylor/dev.spacy --paths.kb nel_taylor/my_kb --paths.base_nlp ./nel_taylor/my_nlp --code custom_functions.py `