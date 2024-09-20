from pathlib import Path
from spacy_llm.registry import registry
import jinja2
from typing import Iterable
from spacy.tokens import Doc

TEMPLATE_DIR = Path("templates")

def read_template(name: str) -> str:
    """Read the text from a Jinja template using pathlib"""

    path = TEMPLATE_DIR / f"{name}.jinja"

    if not path.exists():
        raise ValueError(f"{name} is not a valid template.")

    return path.read_text()

@registry.llm_tasks("my_namespace.QuoteContextExtractTask.v1")
def make_quote_extraction() -> "QuoteContextExtractTask":
    return QuoteContextExtractTask()

class QuoteContextExtractTask:
  def __init__(self, template: str = "quote_context_extract", field: str = "context"):
    self._template = read_template(template)
    self._field = field


  def generate_prompts(self, docs: Iterable[Doc]) -> Iterable[str]:
    environment = jinja2.Environment()
    _template = environment.from_string(self._template)
    for doc in docs:
        prompt = _template.render(
            text=doc.text,
        )
        yield prompt  

  def _check_doc_extension(self):
     """Add extension if need be."""
     if not Doc.has_extension(self._field):
         Doc.set_extension(self._field, default=None)

  def parse_responses(
      self, docs: Iterable[Doc], responses: Iterable[str]
  ) -> Iterable[Doc]:
    self._check_doc_extension()
    for doc, prompt_response in zip(docs, responses):     
      try:
        setattr(
            doc._,
            self._field,
            prompt_response[0].strip(),
        ),
      except ValueError:
        setattr(doc._, self._field, None)
          
    yield doc