import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# دانلود نیازمندی‌های NLTK در صورت عدم وجود
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')

class TextPreprocessor:
    """کلاس پیش‌پردازش متون شامل نرمال‌سازی، توکن‌سازی، حذف Stopwords و Lemmatization."""
    
    def __init__(self, language='english'):
        self.stop_words = set(stopwords.words(language))
        self.lemmatizer = WordNetLemmatizer()

    def clean_text(self, text: str) -> str:
        """حذف علائم نگارشی، اعداد و تبدیل به حروف کوچک."""
        text = text.lower()
        text = re.sub(r'\d+', '', text)
        text = text.translate(str.maketrans('', '', string.punctuation))
        return text.strip()

    def preprocess(self, text: str) -> list[str]:
        """اجرای کامل خط‌لوله‌ی پیش‌پردازش متن."""
        cleaned_text = self.clean_text(text)
        tokens = word_tokenize(cleaned_text)
        
        # حذف کلمات ایست (Stopwords) و لِماتایز کردن
        processed_tokens = [
            self.lemmatizer.lemmatize(word) 
            for word in tokens 
            if word not in self.stop_words and len(word) > 1
        ]
        return processed_tokens

    def preprocess_to_string(self, text: str) -> str:
        """خروجی پیش‌پردازش‌شده به صورت رشته مجزا (مناسب برای TfidfVectorizer)."""
        return " ".join(self.preprocess(text))
