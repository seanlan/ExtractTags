import jieba.analyse


def extract_tags(text) -> list[str]:
    return jieba.analyse.extract_tags(text)


if __name__ == "__main__":
    doc = "温暖的氛围中总是带着一丝紧张   #机车女孩#一加ace2pro"
    from langdetect import detect
    langs = detect(doc)
    print("语言:", langs)
    print("关键词:", extract_tags(doc))
