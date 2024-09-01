import pandas as pd 
from spacy.tokens import DocBin 
import math
import spacy
from spacy.tokens import Span 
from collections import Counter   
 
df_labeled = pd.read_csv("https://raw.githubusercontent.com/PacktPublishing/Mastering-spaCy-Second-Edition./main/chapter_10/taylor_labeled_dataset.csv") 
df_train = df_labeled.sample(frac=0.8, random_state=123) 
df_test = df_labeled.drop(df_train.index)   

# ---

nlp_dir = "chapter_10/nel_taylor/my_nlp" 
nlp = spacy.load(nlp_dir) 

docs = [] 
QIDs = [] 
 
for _,row in df_train.iterrows(): 
    sentence = row["text"] 
    QID = row["QID"] 
    span_start = row["ent_start"] 
    span_end = row["ent_end"]  
    doc = nlp(sentence) 
    QIDs.append(QID)      

    label_ent = "PERSON" 
    ent_span = Span(doc, span_start, span_end, label_ent, kb_id=QID)
    doc.ents = [ent_span] 
    docs.append(doc) 

# ---

train_docs = DocBin() 
dev_docs = DocBin() 

entities = {'Q26876': 'Taylor Swift', 'Q23359': 'Taylor Lautner', 'Q17660516': 'Taylor Fritz'} 

for QID in entities.keys(): 
    indexes_sentences_qid = [i for i, j in enumerate(QIDs) if j == QID] 
    for index in indexes_sentences_qid[0:8]: 
        train_docs.add(docs[index]) 

    for index in indexes_sentences_qid[8:]: 
        dev_docs.add(docs[index]) 

train_corpus = "chapter_10/nel_taylor/train.spacy" 
dev_corpus = "chapter_10/nel_taylor/dev.spacy"   

train_docs.to_disk(train_corpus) 
dev_docs.to_disk(dev_corpus) 