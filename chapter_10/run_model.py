import spacy
from spacy import displacy 

nlp = spacy.load("entity_linking_taylor/model-best") 

text = 'Taylor struggled with chilly temperatures in Edinburgh, pausing the show to warm up her hands and to assist a distressed fan.' 
doc = nlp(text) 
displacy.serve(doc, style="ent") 