## X-ray Data EDA

- 이번 대회에서는 흉부 X-ray 이미지를 통해 병변을 찾고 분류하는, object detection and classification task이다.
- 각 테스트이미지마다 바운딩박스와 클래스를 예측한 값들을 csv파일로 만들어 제출한다.
- 병변이 없는경우(no findings), 정상일 경우에는 14 1 0 0 1 1 이렇게 표시한다(14는 no finding의 라벨)

### Data Files
- train.csv - 훈련 이미지에 대한 정보들이 담겨있음. 하나의 이미지에 여러 라벨 및 어노테이션들이 있으므로 이미지 파일 이름이 중복되어 존재한다.
- train_columns
-   | columns | name | 
    |-------|----------------|
    |image_id | 이미지 파일 이름
    class_name | 병명 이름 (or "No finding")
    class_id | 병명 라벨
    rad_id | 해당 어노테이션을 붙인 방사선전문의 id(사용x)
    x_min | 바운딩 박스 최소값 x의 좌표
    y_min | 바운딩 박스 최소값 y의 좌표
    x_max | 바운딩 박스 최댓값 x의 좌표
    y_max | 바운딩 박스 최댓값 y의 좌표
    
- test.csv - 정답 라벨은 캐글에서 갖고 있으며 이미지의 너비, 높이만 제공된다.
- train_image : 15000장
- test_image : 3000장

### Data Analysis

- 이미지당 총 어노테이션 개수 분포 시각화 (중복포함)
- 
<img src="https://user-images.githubusercontent.com/103362361/203062793-be1485e2-d51e-40ff-8bee-29f7f6ed5ea9.png"  width="300" height="300"/>
<img src="https://user-images.githubusercontent.com/103362361/203064037-225c2208-1fb5-4662-a858-f8df5df52ce4.png"  width="500" height="300"/>

1. 이미지 당 들어있는 라벨은 최소 3개. 어떤 이미지든 라벨이 3개이상 들어있다.
2. 하나의 이미지에 들어있는 라벨 최댓값은 57개.
3. 이미지 중 거의 대부분이 라벨 3개를 갖는다.(전체 15000장 중 10976장)
4. 분포도가 왼쪽으로 많이 치우침. 왜곡도가 높다. 좋은 분포는 skew값이 0이다.

<br/>

- 한 이미지 당 존재하는 병명 수 (중복x)
<img src="https://user-images.githubusercontent.com/103362361/203064397-f3127560-e664-409e-b50a-2012dc7f41a5.png"  width="500" height="300"/>

1. 아래 x축 숫자는 병명 개수를, y축은 이미지 개수를 뜻한다
2. 그래프를 보면 병명이 1개인 이미지가 10k, 10935장이 존재하는데 14번 라벨-no finding인 정상인 이미지의 대부분이 여기에 속한다. 
3. 병명이 1개인 이미지를 제하고 보면 대부분의 이미지들은 최소 2개에서 많게는 10개까지 라벨을 가짐을 알수 있다

<br/>

- 라벨당(병명당) 어노테이션 갯수

<img src="https://user-images.githubusercontent.com/103362361/203063219-533f3ba5-1609-462f-ae4f-81cec55a26b1.png"  width="500" height="300"/>

1. x축은 라벨, y축은 라벨당 총 개수
2. no-finding을 제외한다면 4개의 라벨이 제일 많고 극도로 적은 2개의 라벨이 보인다
3. 데이터의 불균형이 존재. 

