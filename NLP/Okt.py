from konlpy.tag import Okt


if __name__ == '__main__':
    # Okt 형태소 분석기 객체 생성
    okt = Okt()

    text = "시원한 파워에이드 음료수 마시고 싶다."

    # 형태소 추출
    morphs = okt.morphs(text)
    print(morphs)

    # 형태소와 품사 태그 추출
    pos = okt.pos(text)
    print(pos)

    # 명사만 추출
    nouns = okt.nouns(text)
    print(nouns)

    # 정규화, 어구 추출
    message = "오늘 날씨가 좋아욕ㅋㅋ"
    print(okt.normalize(message))  # 정규화
    print("어구 : " + str(okt.phrases(message)))  # 어구

    # Noun        : 명사
    # Verb        : 동사
    # Adjective   : 형용사
    # Josa        : 조사
    # Punctuation : 구두점

