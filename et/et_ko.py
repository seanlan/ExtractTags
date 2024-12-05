from krwordrank.word import KRWordRank

# 输入文本
text = ["한국어 텍스트 분석은 자연 언어 처리의 중요한 영역이다"]

# 初始化 KRWordRank
wordrank = KRWordRank(
    min_count=1,   # 最小出现次数
    max_length=10  # 最大关键词长度
)

# 提取关键词
keywords,b,c = wordrank.extract(text)



# 打印结果
for word, score in keywords.items():
    print(f"{word}: {score}")