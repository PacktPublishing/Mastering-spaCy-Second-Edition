import streamlit as st 
import spacy_streamlit 

DEFAULT_TEXT = """Givenchy is looking at buying U.K. startup for $1 billion""" 

spacy_model = "../chapter_08/pipelines/fashion_ner_with_base_entities" 

st.title("NER Fashion Brands App") 

with st.form("my_form"):
    text = st.text_area("Text to analyze", DEFAULT_TEXT, height=200) 
    submitted = st.form_submit_button("Submit")

    if submitted:
        doc = spacy_streamlit.process_text(spacy_model, text) 
        spacy_streamlit.visualize_ner( 
            doc, 
            labels=["FASHION_BRAND", "GPE"], 
            show_table=False, 
            title="Fashion brands and locations", 
        ) 