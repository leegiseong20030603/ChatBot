from konlpy.tag import Komoran
class KOMORAN:
    def KOMORAN(self):
        # Komoran은 자바로 개발한 한국어 형태소 분석기이며 경량화 버전도 존재하다
        # Kkma 비교
        # 장점 : 형태소를 빠르게 분석하며 다양한 품사 태그를 지원함.
        # 단점 : 함수 3가지 밖에 지원 안함
        komoran = Komoran()
        text = "안드로이드 스튜디오는 인텔리제이에서 개발한 앱 개발 IDE이다. 나는 그중 Flutter 플러그인을 설치해 Flutter 프레임워크를 사용하여 Android, IOS 앱을 개발을 진행하고 있고, Flutter 프레임워크의 장점은 하나의 코드로 Android, IOS 앱 개발을 동시에 할 수 있어 비용, 시간적으로 매우 효율적이다."

        # 형태소 추출
        morphs = komoran.morphs(text)
        print(morphs)

        # 형태소와 품사 태그 추출
        pos = komoran.pos(text)
        print(pos)

        # 명사만 추출
        nouns = komoran.nouns(text)
        print(nouns)

        # NNG : 일반 명사
        # JKS : 주격 조사
        # JKB : 부사격 조사
        # VV : 동사
        # EF : 종결 어미
        # SF : 마침표, 물음표, 느낌표