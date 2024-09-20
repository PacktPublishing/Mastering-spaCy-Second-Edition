import spacy

nlp = spacy.blank("en")
llm = nlp.add_pipe("llm_textcat")


llm.add_label("INSULT")
llm.add_label("COMPLIMENT")
doc = nlp("You look gorgeous!")
print(doc.cats)
# {"COMPLIMENT": 1.0, "INSULT": 0.0}

from spacy_llm.util import assemble

nlp = assemble("config.cfg")
content = """
As we saw on Chapter 6, Language Modeling is the task of predicting the next token given the sequence of previous tokens. The example we've used was that given the sequence of words Yesterday I visited a, a language model can predict the next token as one of the tokens such as church, hospital, school, and so on. Conventional language models are usually trained on a supervised manner to perform a specific task. Pre-trained language models (PLM) are trained on a self-supervised manner, with the aim of learning a generic representation of the language. These PLM models are then fine-tuned to perform a specific downstream task. This self-supervised pre-training made the PLM models much more powerful than the regular language models.

The Large Language Models (LLMs) are the evolution of PLMs that have much more model parameters and larger training datasets. The GPT-3 model for example has 175B parameters. It's successor, GPT3.5, was the base for the ChatGPT model release on november 2022. LLMs can serve as general-purpose tools, capable of tasks from language translation to coding assistance. Their ability to understand and generate human-like text has led to impactful applications in medicine, education, science, math, law, and more. In medicine, LLMs support doctors with evidence-based recommendations and enhance patient interactions. In education, they customize learning experiences and assist teachers in creating content. In science, LLMs speed up research and scientific writing. In law, they analyze legal documents and clarify complex terms.

We can also use LLMs to regular NLP tasks like Named Entity Recognition, text categorization, text summarization and so on. Basically these models can do almost anything we ask them to. But this doesn't come for free since training them require extensive computational resources and the large number of layers and parameters make them produce answers much slowly them non-LLM models. LLMs can also "hallucinate", the case when they produce responses that at first seem plausible but are in fact incorrect or not aligned with the facts or context. This phenomenon occurs because the models generate text based on patterns learned from their training data, rather than verifying information against an external source. As a result, they might create statements that sound reasonable but are misleading, inaccurate, or entirely fictional. Given all that, LLMs are useful but we should always analyze if they are the best solution to the project at hand.

To interact with the LLMs we use prompts. The prompts should guide the models to generate answers or make the model take actions. Prompts usually have these elements:

Instruction: the task you want the model to execute
Context: External information or additional context that should be useful to produce better answers
Input data: the input/question we want to be answered
Output indicator: the type of format we want to see as the model output
With spacy-llm we define the prompts as tasks. When building spaCy pipelines with LLMs each LLM component is defined using a task and a model. The task defines the prompt as well as the functionality to parse the resulting response. The model defines the LLM model and how to connect to it.

Now that you know what LLMs are and how to interact with them, let's use a spacy-llm component in a pipeline. In the next section we're going to create a pipeline to summarize texts using a LLM.
"""
doc = nlp(content)
doc._.summary
print([(ent.text, ent.label_) for ent in doc.ents])


from spacy_llm.util import assemble
from quote import QuoteContextExtractTask

nlp = assemble("config_custom_task.cfg")
quote = "Life isn't about getting and having, it's about giving and being."
doc = nlp(quote)
print("Context:", doc._.context)