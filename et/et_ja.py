from janome.tokenizer import Tokenizer
from sklearn.feature_extraction.text import TfidfVectorizer


def extract_tags(text) -> list[str]:
    tokenizer = Tokenizer()
    tokens = " ".join([token.surface for token in tokenizer.tokenize(text)])
    # TF-IDF 提取关键词
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([tokens])
    keywords = vectorizer.get_feature_names_out()
    return keywords


if __name__ == "__main__":
    doc = "自然言語処理は非常に面白い分野で、機械学習にも使われています。 #Elon #哈哈"
    from langdetect import detect
    langs = detect(doc)
    print("语言:", langs)
    print("关键词:", extract_tags(doc))
