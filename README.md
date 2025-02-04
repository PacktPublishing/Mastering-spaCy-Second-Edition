# Mastering spaCy Second Edition

<a href="https://www.packtpub.com/en-us/product/mastering-spacy-9781835880463"><img src="https://content.packt.com/B22441/cover_image.jpg" alt="no-image" height="256px" align="right"></a>

This is the code repository for [Mastering spaCy Second Edition](https://www.packtpub.com/en-us/product/mastering-spacy-9781835880463), published by Packt.

**Build structured NLP solutions with custom components and models powered by spacy-llm**

## What is this book about?
Master modern NLP development with spaCy's ecosystem: from rapid prototyping with spaCy-LLM to production deployment. Learn to build custom components, integrate transformers, and manage end-to-end workflows with Weasel.

This book covers the following exciting features:
* Apply transformer models and fine-tune them for specialized NLP tasks
* Master spaCy core functionalities including data structures and processing pipelines
* Develop custom pipeline components and semantic extractors for domain-specific needs
* Build scalable applications by integrating spaCy with FastAPI, Streamlit, and Ray
* Master advanced spaCy features including coreference resolution and neural pipeline components
* Train domain-specific models, including NER and coreference resolution
* Prototype rapidly with spaCy-LLM and develop custom LLM tasks

If you feel this book is for you, get your [copy](https://www.amazon.com/Mastering-spaCy-structured-solutions-components/dp/B0DVCBRFZX/ref=sr_1_1?crid=D7V9PR1A2EZF&dib=eyJ2IjoiMSJ9.m_RTfomi5hxb7NXTRT9rQGdMm7ZpXYa4eNfYzA_gH5o5aibSYi05-qBVc2bmQ_VPmfYkQGmMx3E9IHP9MVpBhCHZ55TFPXDb5aIwVcoHwuUlsF2EImlOLyKG2pP9Z8emshM7jyzbho3qyC-jZRMDAt-8XsupG5YlOv_l1bh6_xQkKiFLsmUy_7DefM-SSCKI.Hg74WInz-_ZsHRH1X53I3-pUmbxzvJi6h-vwpLS-58s&dib_tag=se&keywords=mastering+spacy&qid=1738648186&sprefix=mastering+spacy%2Caps%2C388&sr=8-1) today!
<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders. For example, chapter_01.

The code will look like the following:
```
import spacy
nlp = spacy.load("en_core_web_md")
doc = nlp("It's been a crazy week!!!")
print([token.text for token in doc])
```
To effectively apply your understanding, make sure to execute the code in an appropriate environment with all required libraries and modules installed.

## Quick links

|No.| Chapter | Notebook | Colab |
|:--| :-------- | :-------- | :-------: |
|01| Getting Started with spaCy | [Chapter 01](chapter_01/chapter_01.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PacktPublishing/Mastering-spaCy-Second-Edition./blob/main/chapter_01/chapter_01.ipynb) | 
|02| Core Operations with spaCy | [Chapter 02](chapter_02/chapter_02.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PacktPublishing/Mastering-spaCy-Second-Edition./blob/main/chapter_02/chapter_02.ipynb) | 
|03| Extracting Linguistic Features | [Chapter 03](chapter_03/chapter_03.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PacktPublishing/Mastering-spaCy-Second-Edition./blob/main/chapter_03/chapter_03.ipynb) | 
|04| Mastering Rule-Based Matching | [Chapter 04](chapter_04/chapter_04.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PacktPublishing/Mastering-spaCy-Second-Edition./blob/main/chapter_04/chapter_04.ipynb) | 
|05| Extracting Semantic Representations with spaCy Pipelines | [Chapter 05](chapter_05/chapter_05.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PacktPublishing/Mastering-spaCy-Second-Edition./blob/main/chapter_05/chapter_05.ipynb) | 
|06| Utilizing spaCy with Transformers | [Chapter 06](chapter_06/chapter_06.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PacktPublishing/Mastering-spaCy-Second-Edition./blob/main/chapter_06/chapter_06.ipynb) | 
|07| Enhancing NLP tasks using LLMs with spacy-llm | [Chapter 07](chapter_07/chapter_07.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PacktPublishing/Mastering-spaCy-Second-Edition./blob/main/chapter_07/chapter_07.ipynb) | 
|08| Training a NER Component with Your Own Data | [Chapter 08](chapter_08/chapter_08.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PacktPublishing/Mastering-spaCy-Second-Edition./blob/main/chapter_08/chapter_08.ipynb) | 
|09| Creating End-to-End spaCy Workflows with Weasel | [Chapter 09](chapter_09/chapter_09.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PacktPublishing/Mastering-spaCy-Second-Edition./blob/main/chapter_09/chapter_09.ipynb) | 
|10| Training an Entity Linker Model with spaCy | [Chapter 10](chapter_10/) | - | 
|11| Integrating spaCy with Third-Party Libraries | [Chapter 11](chapter_11/) | - | 

**Following is what you need for this book:**
This book is tailored for NLP engineers, machine learning developers, and LLM engineers looking to build production-grade language processing solutions. While primarily targeting professionals working with language models and NLP pipelines, it's also valuable for software engineers transitioning into NLP development. Basic Python programming knowledge and familiarity with NLP concepts is recommended to leverage spaCy's latest capabilities.

With the following software and hardware list you can run all code files present in the book (Chapter 1-11).
## Software and Hardware List
| Chapter | Software required | OS required |
| -------- | ------------------------------------ | ----------------------------------- |
| 1-11 | Python >= 3.12 | Windows, macOS, or Linux |
| 1-11 | spaCy v3.7 | Windows, macOS, or Linux |
| 1-11 | spacy-transformers == 1.3.5 | Windows, macOS, or Linux |
| 1-11 | spacy-streamlit >= 1.0.6 | Windows, macOS, or Linux |
| 1-11 | FastAPI >= 0.112.0 | Windows, macOS, or Linux |

## Related products
* LLM Engineer's Handbook [[Packt]](https://www.packtpub.com/en-us/product/llm-engineers-handbook-9781836200079) [[Amazon]](https://www.amazon.com/LLM-Engineers-Handbook-engineering-production/dp/1836200072/ref=sr_1_1?crid=20CY8J1BQNREZ&dib=eyJ2IjoiMSJ9.9aGXn6xGorwhpBZedby-9_LYFh2pAPJqVTnPSu2-5xI4vyl89GWPW07EluA5wYDbxV-SZ1kcuaFLfjQyqQNZgbPYgjtZALx6mkzWyueTbSoxSOxcxd6Tl7HldUJzgr7F8GpLYIXISrgTYCtOWu8nEUSNBLa14zm7xsKggoyvx8uABRDdCiy5DarBbxhZqRp_VmwavuLfB3d5GSLRjK2Sz1a6DtCcJeNJt_pNqSAeT-4.aZM7pXpvPt78ZhABk3hYIAOnqBOFZXIPzrWztYg8NxU&dib_tag=se&keywords=llm+engineer%27s+handbook&qid=1737647540&sprefix=llm+engineer%27s+handboo%2Caps%2C923&sr=8-1)

* Practical Generative AI with ChatGPT - Second Edition [[Packt]](https://www.packtpub.com/en-us/product/practical-generative-ai-with-chatgpt-9781836647850) [[Amazon]](https://www.amazon.com/Practical-Generative-ChatGPT-generative-productivity/dp/1836647859/ref=sr_1_1?dib=eyJ2IjoiMSJ9.B3LOQOmaMxlQfnBFNnqNaSTDpuSwdizCEejeqY_YI13fwdhHPd9_SK7DGYuN6Iww3kHtwOnA1HFh3ya_5fUtEd7Op0GsjJxc5C5zzidHzaCfgfq9E-Hva5q7bzQbQo8L-5Q1l9ZeEKCx_bVtrj-VSdMtxYIyM0RhhCs9zvmcN_SogSQ_osvtxD2IWsjhgqaaC_LvY-kVYMWykfcV6AwPg9OU9FK5jzRLUcM5jnK5oh0.zUzowdRvvne_N-3uCDvlG7aYQW05UCG1WvM8wjrqUio&dib_tag=se&keywords=Practical+Generative+AI+with+ChatGPT&qid=1737647504&sr=8-1)

## Get to Know the Authors
**Déborah Mesquita**
is a data science consultant and writer. With a BSc in computer science from UFPE, one of Brazil’s top computer science programs, she brings a diversified skill set refined through hands-on experience with various technologies. Déborah has consistently delivered exceptional results in various data science projects, being able to navigate the business and technical sides of each project. Her ability to translate complex concepts into simple language, coupled with her quick learning and broad vision, make her an effective educator. Actively engaged in community initiatives, she works to ensure equitable access to knowledge, reflecting her belief that technology is not a panacea, but a powerful tool for societal improvement when used for that purpose. She writes a personal blog at deborahmesquita.com.

**Duygu Altinok**
is a senior Natural Language Processing (NLP) engineer with 12 years of experience in almost all areas of NLP, including search engine technology, speech recognition, text analytics, and conversational AI. She has published several publications in the NLP domain at conferences such as LREC and CLNLP. She also enjoys working on open source projects and is a contributor to the spaCy library. Duygu earned her undergraduate degree in computer engineering from METU, Ankara, in 2010 and later earned her master’s degree in mathematics from Bilkent University, Ankara, in 2012. She is currently a senior engineer at German Autolabs with a focus on conversational AI for voice assistants. Originally from Istanbul, Duygu currently resides in Berlin, Germany, with her cute dog Adele.
