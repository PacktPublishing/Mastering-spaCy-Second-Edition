import srsly
import typer
import spacy 
from spacy.tokens import DocBin 
from pathlib import Path 
 
ASSETS_DIR = Path(__file__).parent.parent / "assets"
CORPUS_DIR = Path(__file__).parent.parent / "corpus"

def main(assets_dir: Path=ASSETS_DIR, corpus_dir: Path=CORPUS_DIR, lang: str="en"):
    nlp = spacy.blank(lang) 
    for jsonl_file in assets_dir.iterdir():
        if not jsonl_file.parts[-1].endswith(".jsonl"):
            continue
        db = DocBin() 

        for line in srsly.read_jsonl(jsonl_file):
            doc = nlp.make_doc(line["text"]) 
            doc.cats = line["cats"]
            db.add(doc) 

        out_file = corpus_dir / jsonl_file.with_suffix(".spacy").parts[-1]
        db.to_disk(out_file) 

if __name__ == "__main__":
    typer.run(main)