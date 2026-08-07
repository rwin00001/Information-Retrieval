# Vector Space Model Search Engine

A lightweight Information Retrieval (IR) search engine implementing the Vector Space Model (VSM) with TF-IDF weighting and Cosine Similarity scoring.

## Features
- **Text Preprocessing**: Lowercasing, punctuation stripping, tokenization, stopword removal, and lemmatization via NLTK.
- **Indexing**: Inverted Index dictionary construction and Scikit-Learn TF-IDF Matrix calculation.
- **Search & Ranking**: Vectorized query evaluation using Cosine Similarity.

## Project Structure
```text
project1-vector-space-search/
├── data/                  # Raw and processed datasets
│   ├── raw/               # Sample JSON documents
│   ├── processed/         # Sample inverted index
│   └── README.md          # Dataset documentation
├── src/
│   ├── preprocessing.py   # Text tokenization & lemmatization
│   ├── indexer.py         # Inverted index & TF-IDF builder
│   └── search_engine.py   # Query processing & similarity calculation
├── requirements.txt
└── README.md
```

Quick Start
```Bash
pip install -r requirements.txt
python src/search_engine.py
```
