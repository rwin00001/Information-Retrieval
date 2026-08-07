# Information Retrieval & Text Analytics Suite

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![NLTK](https://img.shields.io/badge/NLTK-3.8%2B-green.svg)](https://www.nltk.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.2%2B-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A portfolio-grade collection of two Information Retrieval (IR) systems demonstrating classic vector-based document retrieval, text preprocessing pipelines, XML data parsing, and an empirical evaluation of 11 string similarity and edit-distance algorithms.

---

## 📑 Table of Contents
- [Overview](#-overview)
- [Repository Architecture](#-repository-architecture)
- [Project 1: Vector Space Search Engine](#1-vector-space-search-engine)
  - [Mathematical Formulation](#mathematical-formulation)
  - [Pipeline Architecture](#pipeline-architecture)
- [Project 2: Token Similarity & Metrics Engine](#2-token-similarity--metrics-engine)
  - [Evaluated Algorithms](#evaluated-algorithms)
  - [Data Extraction & Parsing](#data-extraction--parsing)
- [Installation & Setup](#-installation--setup)
- [Sample Results & Benchmarks](#-sample-results--benchmarks)
- [License](#-license)

---

## 🔬 Overview

This repository bridges two core subfields of Information Retrieval:
1. **Semantic & Vector Retrieval**: Mapping documents and queries into high-dimensional vector spaces using term frequency-inverse document frequency ($\text{TF-IDF}$) weights and evaluating relevance via Cosine Similarity.
2. **Syntactic & Phonetic String Matching**: Evaluating structural, edit-distance, phonetic, and $n$-gram similarities across thousands of tokens extracted from StackExchange XML dumps.

---

## 📁 Repository Architecture

```text
information-retrieval-lab/
├── project1-vector-space-search/
│   ├── data/
│   │   ├── raw/                       # JSON document collections
│   │   ├── processed/                 # Inverted index & vocabulary mappings
│   │   └── README.md                  # Schema documentation
│   ├── src/
│   │   ├── preprocessing.py           # NLP pipeline (Tokenization, Lemmatization)
│   │   ├── indexer.py                 # Inverted Index & TF-IDF matrix builder
│   │   └── search_engine.py           # Vector space query evaluator & ranker
│   ├── requirements.txt
│   └── README.md
│
├── project2-token-similarity/
│   ├── data/
│   │   ├── Posts.xml                  # Raw StackExchange data dump
│   │   ├── tokens.txt                 # Extracted Nouns & Verbs
│   │   ├── top10.txt                  # High-frequency keywords
│   │   └── README.md
│   ├── src/
│   │   ├── xml_parser.py              # BeautifulSoup XML parser & POS tagger
│   │   ├── similarity_metrics.py      # Implementation of 11 distance metrics
│   │   └── evaluate_matches.py        # Benchmark execution loop
│   ├── results/
│   │   └── similar_tokens.txt         # Metric evaluation outputs
│   ├── requirements.txt
│   └── README.md
│
└── README.md                          # Global repository guide
