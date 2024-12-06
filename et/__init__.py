import logging
from langdetect import detect_langs
from . import et_zh, et_ja, et_en


def extract_tags(text) -> list[str]:
    langs = detect_langs(text)
    if len(langs) > 1:
        lang = "zh"
    else:
        lang = langs[0].lang
    logging.info(f"language: {lang}")
    if lang == "zh" or lang == "zh-cn" or lang == "zh-tw" or lang == "zh-hk":
        keyword = et_zh.extract_tags(text)
    elif lang == "ja":
        keyword = et_ja.extract_tags(text)
    elif lang == "en":
        keyword = et_en.extract_tags(text)
    else:
        keyword = et_zh.extract_tags(text)
    return list(set(keyword))
