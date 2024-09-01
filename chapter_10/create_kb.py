import os 
import spacy 
from spacy.kb import InMemoryLookupKB 
 
nlp = spacy.load("en_core_web_md") 
 
ruler = nlp.add_pipe("span_ruler", after="ner") 
patterns = [{"label": "PERSON", "pattern": [{"LOWER": "taylor"}]}] 
ruler.add_patterns(patterns) 

kb_loc = "chapter_10/nel_taylor/my_kb" 
nlp_dir = "chapter_10/nel_taylor/my_nlp" 

# ---
  
kb = InMemoryLookupKB(vocab=nlp.vocab, entity_vector_length=300) 

entities = {'Q26876': 'Taylor Swift', 'Q23359': 'Taylor Lautner', 'Q17660516': 'Taylor Fritz'} 
descriptions = {'Q26876': 'American singer-songwriter (born 1989)', 'Q23359': 'American actor', 'Q17660516': 'American tennis player'} 

for qid, desc in descriptions.items(): 
    desc_doc = nlp(desc) 
    desc_vector = desc_doc.vector 
    kb.add_entity(entity=qid, entity_vector=desc_vector, freq=111) 

for qid, name in entities.items(): 
    kb.add_alias(alias=name, entities=[qid], probabilities=[1]) 

qids = entities.keys() 
kb.add_alias(alias="Taylor", entities=qids, probabilities=[0.3, 0.3, 0.3]) 

print(f"Entities in the KB: {kb.get_entity_strings()}") 
print(f"Aliases in the KB: {kb.get_alias_strings()}") 

kb.to_disk(kb_loc) 

if not os.path.exists(nlp_dir): 
    os.mkdir(nlp_dir) 

nlp.to_disk(nlp_dir) 