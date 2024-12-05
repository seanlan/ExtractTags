import yake


def extract_tags(text) -> list[str]:
    kw_extractor = yake.KeywordExtractor()
    keywords = kw_extractor.extract_keywords(text)
    # 按照得分排序
    keywords = [keyword for keyword, score in sorted(keywords, key=lambda x: x[1], reverse=True)]
    return keywords


if __name__ == "__main__":
    doc = "한국어 텍스트 분석은 자연 언어 처리의 중요한 영역이다 #study #studymotivation #studyinspirational  #productivestudy #motivation #Elon"
    from langdetect import detect
    langs = detect(doc)
    print("语言:", langs)
    print("关键词:", extract_tags(doc))
