# Kaggle VinBigData Chest X-ray Abnormalities Detection 🏥📽

### Chest X-ray Image를 object detection을 통해 폐 관련 14가지 질병을 detection.  

---

## Description

Purpose : Data augmentation, 모델에 따른 성능 비교

Team : DeepDream (조장:김수현, 조원:이봉학, 김현나, 이x정, 소x희)

Challenge Link : https://www.kaggle.com/competitions/vinbigdata-chest-xray-abnormalities-detection

Project period :  2022.06.13(월)  ~ 2022.07.11(월) 

---

## WorkFlow

<img src="https://user-images.githubusercontent.com/103362361/189588057-11ec4eaf-dba6-4362-ba50-03466d25d85a.png"  width="400" height="300"/>

### 1. 데이터 소개 및 분석.

- Kaggle의 ‘VinBigData Chest X-ray Abnormalites Detection’ 대회에서 베트남의 두 병원에서 제공해준 환자들의 흉부 x-ray 데이터셋

- 14개 라벨의 train image 15000장, test image 3000장 (512x512x3) & train image의 image_id, class_id, x_min, y_min, x_max, y_max 정보가 들어있는 train.csv 파일. 

- [Image Dataset](https://www.kaggle.com/datasets/awsaf49/vinbigdata-512-image-dataset) & [Label Dataset](https://www.kaggle.com/datasets/awsaf49/vinbigdata-yolo-labels-dataset)

  
- 데이터 분석
    - X-ray 이미지이기에 어느정도의 도메인 지식 및 조사가 필요. 각 라벨에 대한 사전조사를 하였다. 
    - 15000장 train image에서 14번라벨, 정상인 image 10606장을 빼고 남은 이미지는 4394장. => 이미지 4394장, 라벨 36096개
    - 하나의 이미지에 대해 여러 병변이 존재하는, 단일 이미지-다중 라벨
    - 라벨값과 병명
    
    <br/>
    
    
    |라벨|병명|라벨|병명|
    |----|----|----|----|
    |0 | [Aortic enlargement](https://www.baptisthealth.com/services/heart-care/conditions/aortic-aneurysm-enlarged-aorta)|7 | Lung Opacity|
    |1 | [Atelectasis](https://terms.naver.com/entry.naver?docId=927036&cid=51007&categoryId=51007)|8 | Nodule/Mass(결절/혹)|
    |2 | [Calcification](https://terms.naver.com/entry.naver?docId=493788&cid=60408&categoryId=55558)|9 | Other lesion|
    |3 | [Cardiomegaly](https://terms.naver.com/entry.naver?docId=927305&cid=51007&categoryId=51007)|10 | Pleural effusion|
    |4 | [Consolidation](https://blog.naver.com/daytoday_life/221561444265)|11 | Pleural thickening|
    |5 | [ILD(interstitial lung disease)](https://www.amc.seoul.kr/asan/healthinfo/disease/diseaseDetail.do?contentId=31848)|12 | Pneumothorax|
    |6 | Infiltration|13 | Pulmonary fibrosis|
    
    
    <!-- <img src="https://user-images.githubusercontent.com/103362361/188309386-e74a9214-643e-495b-acb5-cf72e455e5b9.jpg"  width="400" height="300"/> -->
    
    <img src="https://user-images.githubusercontent.com/103362361/189323442-ceb8591e-bd50-4b49-9ea2-426f7253fed3.png"  width="400" height="300"/>
    
    => 💡 데이터 불균형이 심하다 -> 학습에 영향을 줄수있기에 이문제를 어떻게 다룰지에 대한 방법이 필요. (다운샘플링을 할것인지, 부족한 라벨에 대해서 추가적인 Augmentation을 해줄것인지 등등..)
    
    => ❗ 데이터 불균형 해결이 어려웠던 이유 : 라벨 간의 극단적인 양의 차이, 단일 이미지에 대한 다중 라벨
    
    (이미지 하나에 라벨이 2-3개만 있거나 7~8개, 10개이상이 존재하는 등 이미지마다 라벨의 개수가 다르기때문에 단순히 이미지만 증강시키는것이 아니라 라벨도 신경을 써야함)
    
    - [병명 사전조사](https://www.notion.so/4e8668bfaf684adbab481b49f93207ef) (노션링크)
    
    => 💡 사전조사를 보면 흉부 X-ray를 통해 폐 질병을 진단 시, 폐의 '불투명도'는 매우 중요한 요소임을 확인. 이미지를 증강하거나 변형할 때 명암을 조절함에 있어서 주의가 필요
    
    
<br/>


---
### 2. 전처리 



#### 1. Image Augmentation

💬 이미지 4394장으로 학습하기에 적다고 생각하여 Augmentation이 필요하다고 판단. 

=> ❔ 그럼 어떤 기법을 적용시킬 것인가?? 

=> 💡 비슷한 Task를 진행한 Reference들 참고. (폐 X-ray 이미지 Object Detection 논문들, 코로나로 관련 논문들이 많이 올라왔음) - 어떤 레퍼런스에서 어떤 기법을 왜 사용했고 그 결과 성능이 어땠는지, 참고한 레퍼런스와 사용한 기법, 거기에 대한 결과 등 추가하기

주로 많이 한 Augmentation 기법 중 rotation 90도, zoom in, flip(horizontal)... 등등 리스트업을 하고 여러 데이터셋을 만들기로 하였다. (임시)


<br/>



#### 2. Dataset 생성 및 구분 - 추가정리필요

 <img src="https://user-images.githubusercontent.com/103362361/189592650-22ae97c3-60c9-487e-9ccf-c891bc914128.png"  width="400" height="300"/>

어떤 Augmentation들이 성능향상에 좋았는지 비교를 위해 여러 데이터셋을 생성

<!--
분류(A)|분류(B)|분류(C)|분류(D)|
-------|-------|-------|-------|
원본|rotation : 90°|rotation : 90°|rotation : 90°|
&nbsp;|flip: horizontal|flip: horizontal|flip: horizontal|
&nbsp;|zoom: 10%|zoom: 10%|zoom: 10%|
&nbsp;|&nbsp;|cutmix|cutmix|
&nbsp;|&nbsp;|mosaic|mosaic|
&nbsp;|&nbsp;| CLAHE | CLAHE 
-->
    
=> ❔ Augmentation이 어느정도 사용될 때 성능이 가장 좋을까??

=> ❔ 우리가 사용하는 데이터는 X-ray, 흑백 이미지. 각 Augmentation은 어떤 영향을 미칠까??

=> ❔ X-ray나 흑백 이미지 같은 경우에 적합한 Augmentation은 무엇일까??


<br/>

#### 3. COCO데이터셋으로 변환 및 배포.

- Augmentation을 한뒤에 이미지와 라벨, 바운딩박스 좌표가 들어있는 텍스트들을 COCO형식 데이터셋으로 만들어 조원들에게 배포하였다. 해당 [라이브러리](https://github.com/RapidAI/YOLO2COCO) (RapidAI-YOLO2COCO)를 사용해서 생성하였다.

  => ❔ COCO형식으로 데이터셋을 변환해준 이유는?? : 
  
  🗨 모델을 여러개 사용했으므로 데이터셋을 하나의 양식으로 통일하고 각 모델에 맞게 변형시키는 코드를 만들어서 '이미지 증강->COCO셋으로 생성->훈련' 일련의 과정을 자동화함.


---
### 3. 모델링 


- Faster R-CNN, YOLOX, EfficientDet 3개 모델 선정 및 사용

  => ❔ 왜 하나의 모델이 아닌 여러 모델을 사용했는가??

  => ❔ 모델 각각의 선정이유는??



#### 1. Faster R-CNN





     
#### 2. YOLOX





#### 3. EfficientDet





---
### 4. 결과




---


    
    
    
    
    
