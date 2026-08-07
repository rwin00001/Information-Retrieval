from collections import defaultdict
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from preprocessing import TextPreprocessor

class InvertedIndexBuilder:
    """کلاس ساخت نمایه معکوس (Inverted Index) و محاسبه ماتریس TF-IDF."""
    
    def __init__(self):
        self.preprocessor = TextPreprocessor()
        self.vectorizer = TfidfVectorizer()
        self.inverted_index = defaultdict(list)
        self.tfidf_matrix = None
        self.doc_ids = []

    def build_index(self, documents: dict[int, str]):
        """
        دریافت دیکشنری اسناد به فرمت {doc_id: doc_text} 
        و ساخت نمایه معکوس + ماتریس TF-IDF
        """
        self.doc_ids = list(documents.keys())
        raw_corpus = list(documents.values())
        
        # پیش‌پردازش اسناد
        processed_corpus = [
            self.preprocessor.preprocess_to_string(doc) for doc in raw_corpus
        ]

        # ۱. ساخت Inverted Index بر اساس توکن‌ها
        for doc_id, text in documents.items():
            tokens = self.preprocessor.preprocess(text)
            for token in set(tokens):
                self.inverted_index[token].append(doc_id)

        # ۲. محاسبه ماتریس TF-IDF
        self.tfidf_matrix = self.vectorizer.fit_transform(processed_corpus)
        return self.inverted_index, self.tfidf_matrix

    def get_feature_names(self):
        """دریافت لیست کلمات موجود در دیکشنری مدل."""
        return self.vectorizer.get_feature_names_out()
