from et import extract_tags

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    doc1 = "한국어 텍스트 분석은 자연 언어 처리의 중요한 영역이다 #study #studymotivation #studyinspirational  #productivestudy #motivation #Elon"
    print("关键词:", extract_tags(doc1))
    doc2 = "温暖的氛围中总是带着一丝紧张   #机车女孩#一加ace2pro"
    print("关键词:", extract_tags(doc2))
    doc3 = "自然言語処理は非常に面白い分野で、機械学習にも使われています。 #Elon #哈哈"
    print("关键词:", extract_tags(doc3))
    doc4 = "Natural language processing is a very interesting field that is also used in machine learning"
    print("关键词:", extract_tags(doc4))