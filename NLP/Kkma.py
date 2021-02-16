from konlpy.tag import Kkma
from konlpy.utils import pprint

if __name__ == '__main__':
    kkma = Kkma()
    message = '안녕하세요 저는 홍길동입니다.'
    hello = "안녕하세요. 저는 홍길동이며 고등학교 3학년입니다. 오늘 자연어 처리 공부를 시작한 학생이며 앞으로 앱에 자연어 처리 기술을 응용하며 개발을 진행할 예정입니다. 앞으로 많은 관심과 응원 부탁드립니다. 감사합니다."

    # 형태소 추출
    pprint("morphs : " + str(kkma.morphs(message)))

    # 형태소와 품사 태그 추출
    pprint("nouns : " + str(kkma.nouns(message)))

    # 명사만 추출
    pprint("pos : " + str(kkma.pos(message)))

    # 문장 분리
    sentences = kkma.sentences(hello)
    pprint("sentences : " + str(sentences))
    for i in sentences:
        print(i)