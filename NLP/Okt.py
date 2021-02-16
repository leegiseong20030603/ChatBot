from konlpy.tag import Okt

class OKT:
    def OKT(self):

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
        text = "오늘 날씨가 좋아욕ㅋㅋ"
        print(okt.normalize(text)) # 정규화
        print("어구 : " + str(okt.phrases(text))) # 어구
