from konlpy.tag import Komoran
import numpy as np

if __name__ == '__main__':
    komoran = Komoran()
    text = "오늘 날씨는 상온 16도이며 구름이 많습니다."

    # 명사만 추출
    nouns = komoran.nouns(text)
    print(nouns)

    # 단어 사전 구축 및 단어별 인덱스 부여
    dics = {}
    for word in nouns:
        if word not in dics.keys():
            dics[word] = len(dics)

    print(dics)

    # 원-핫 인코딩 #
    nb_classes = len(dics)
    targets = list(dics.values())

    #  eye() 함수는 인자 크기대로 단위 행렬을 반환하며 [targets]를 이용해 생성된 단위행렬의 순서를 단어 사전의 순서에 맞게 정렬해준다.
    one_hot_targets = np.eye(nb_classes)[targets]

    print(one_hot_targets)