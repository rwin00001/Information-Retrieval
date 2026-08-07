import os
import xml.etree.ElementTree as ET
from collections import Counter
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')

def parse_and_extract_tokens(xml_file_path: str, data_dir: str):
    """
    پارس کردن Posts.xml، پاکسازی کدهای HTML، 
    استخراج اسم/فعل‌ها و ساخت فایل‌های tokens.txt و top10.txt
    """
    tokens = []
    
    if os.path.exists(xml_file_path):
        tree = ET.parse(xml_file_path)
        root = tree.get_root()
        
        for row in root.findall('row'):
            body_html = row.attrib.get('Body', '')
            text = BeautifulSoup(body_html, "html.parser").get_text()
            words = word_tokenize(text.lower())
            
            # فیلتر کردن اسم‌ها (NN) و فعل‌ها (VB)
            tagged = pos_tag(words)
            for word, tag in tagged:
                if word.isalpha() and (tag.startswith('NN') or tag.startswith('VB')):
                    tokens.append(word)
    else:
        print(f"Warning: {xml_file_path} not found. Using fallback sample tokens.")
        tokens = ["browser", "security", "network", "privacy", "tor", "onion", "encryption", "server", "user", "proxy"]

    # ۱. ذخیره تمام توکن‌ها
    tokens_path = os.path.join(data_dir, 'tokens.txt')
    with open(tokens_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(tokens))

    # ۲. استخراج ۱۰ واژه پرتکرار
    counter = Counter(tokens)
    top10 = counter.most_common(10)
    
    top10_path = os.path.join(data_dir, 'top10.txt')
    with open(top10_path, 'w', encoding='utf-8') as f:
        for word, count in top10:
            f.write(f"{word}:{count}\n")

    print(f"Extracted {len(tokens)} tokens and saved top 10 keywords.")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_folder = os.path.join(base_dir, 'data')
    xml_path = os.path.join(data_folder, 'Posts.xml')
    parse_and_extract_tokens(xml_path, data_folder)
