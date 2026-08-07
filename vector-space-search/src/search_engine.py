import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from indexer import InvertedIndexBuilder

class VectorSpaceSearchEngine:
    """موتور جستجو بر پایه مدل فضای برداری و تشابه کسینوسی."""
    
    def __init__(self, indexer: InvertedIndexBuilder):
        self.indexer = indexer

    def search(self, query: str, top_k: int = 5) -> list[tuple[int, float]]:
        """
        جستجوی کوئری و بازگرداندن شناسه اسناد و نمره تشابه بر اساس Cosine Similarity.
        """
        # پیش‌پردازش پرس‌وجو
        processed_query = self.indexer.preprocessor.preprocess_to_string(query)
        if not processed_query:
            return []

        # تبدیل کوئری به بردار TF-IDF
        query_vector = self.indexer.vectorizer.transform([processed_query])

        # محاسبه تشابه کسینوسی بین بردار کوئری و تمام اسناد
        similarities = cosine_similarity(query_vector, self.indexer.tfidf_matrix).flatten()

        # مرتب‌سازی نتایج بر اساس بیشترین تشابه
        top_indices = np.argsort(similarities)[::-1][:top_k]

        results = []
        for idx in top_indices:
            score = similarities[idx]
            if score > 0:  # فقط اسنادی که نمره تشابه مثبت دارند
                doc_id = self.indexer.doc_ids[idx]
                results.append((doc_id, float(score)))

        return results


# نمونه اجرای آزمایشی (Demo)
if __name__ == "__main__":
    docs = {
        1: "Information retrieval system searches documents based on user queries.",
        2: "Vector space model converts text documents into term frequency vectors.",
        3: "Python implementation of cosine similarity search engine using TF-IDF.",
        4: "Natural language processing includes tokenization, stopword removal, and lemmatization."
    }

    # ساخت نمایه
    indexer = InvertedIndexBuilder()
    indexer.build_index(docs)

    # راه اندازی موتور جستجو
    search_engine = VectorSpaceSearchEngine(indexer)

    # کوئری نمونه
    query_text = "vector space search retrieval"
    results = search_engine.search(query_text, top_k=3)

    print(f"Query: '{query_text}'\nResults:")
    for doc_id, score in results:
        print(f" -> Doc ID: {doc_id} | Cosine Similarity Score: {score:.4f}")
        print(f"    Content: {docs[doc_id]}\n")
