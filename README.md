# Kaggle VinBigData Chest X-ray Abnormalities Detection 🏥📽

### Chest X-ray Image를 object detection을 통해 폐 관련 14가지 질병을 detection.  

---

## Description

Purpose : Data augmentation, 모델에 따른 성능 비교

Team : DeepDream (조장:김수현, 조원:이봉학, 김현나, 이x정, 소x희)

Challenge Link : https://www.kaggle.com/competitions/vinbigdata-chest-xray-abnormalities-detection

---

## WorkFlow

### 1. 데이터 소개 및 분석.

Kaggle의 ‘VinBigData Chest X-ray Abnormalites Detection’ 대회에서 베트남의 두 병원에서 제공해준 환자들의 흉부 x-ray 데이터셋

14개 라벨의 train image 15000장, test image 3000장 (512x512x3) & train image의 image_id, class_id, x_min, y_min, x_max, y_max 정보가 들어있는 train.csv 파일. 

[Image Dataset](https://www.kaggle.com/datasets/awsaf49/vinbigdata-512-image-dataset) & [Label Dataset](https://www.kaggle.com/datasets/awsaf49/vinbigdata-yolo-labels-dataset)

  - 데이터 분석
    - X-ray 이미지이기에 어느정도의 도메인 지식 및 조사가 필요. 각 라벨에 대한 사전조사를 하였다. 
    - 15000장 train image에서 14번라벨, 정상인 image 10606장을 빼고 남은 이미지는 4394장. => 이미지 4393장, 라벨 36096개
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
    
    - [병명 사전조사](https://www.notion.so/4e8668bfaf684adbab481b49f93207ef)(노션링크)
    
    => 💡 사전조사를 보면 흉부 X-ray를 통해 폐 질병을 진단 시, 폐의 '불투명도'는 매우 중요한 요소임을 확인. 이미지를 증강하거나 변형할 때 명암을 조절함에 있어서 주의가 필요
    
    
  <!--
    |라벨|병명|사진|라벨|병명|사진|
    |----|----|----|----|----|----|
    |0 | [Aortic enlargement](https://www.baptisthealth.com/services/heart-care/conditions/aortic-aneurysm-enlarged-aorta)|<img src="https://user-images.githubusercontent.com/103362361/188856182-1965963c-7a6b-4fb2-a867-0a3ec25842a6.png"  width="200" height="200"/>|7 | Lung Opacity|<img src="https://user-images.githubusercontent.com/103362361/188861827-bfed1297-7fc1-46f2-8bd2-2d283a7eac82.png"  width="200" height="200"/>|
    |1 | [Atelectasis](https://terms.naver.com/entry.naver?docId=927036&cid=51007&categoryId=51007)|<img src="https://user-images.githubusercontent.com/103362361/188856681-f3db74aa-9db1-43be-9a6e-32b3b974b4f1.png"  width="200" height="200"/>|8 | Nodule/Mass(결절/혹)|<img src="https://user-images.githubusercontent.com/103362361/188862273-df3186e4-e80c-49e0-a8f2-ee8df3663684.png"  width="200" height="200"/>|
    |2 | [Calcification](https://terms.naver.com/entry.naver?docId=493788&cid=60408&categoryId=55558)|<img src="https://user-images.githubusercontent.com/103362361/188857391-3eaec5b8-6e2a-4cac-8cca-9d1b38212c6d.png"  width="200" height="200"/>|9 | Other lesion|<img src="https://user-images.githubusercontent.com/103362361/188862546-573d91d4-2cdc-4a69-b047-152ca706811e.png"  width="200" height="200"/>|
    |3 | [Cardiomegaly](https://terms.naver.com/entry.naver?docId=927305&cid=51007&categoryId=51007)|<img src="https://user-images.githubusercontent.com/103362361/188857765-79d8fef5-ad5d-4e1d-b923-46587cd76e49.png"  width="200" height="200"/>|10 | Pleural effusion|<img src="https://user-images.githubusercontent.com/103362361/188863451-88206ec6-a5b5-4c55-b683-4e4b5cedcb9a.png"  width="200" height="200"/>|
    |4 | [Consolidation](https://blog.naver.com/daytoday_life/221561444265)|<img src="https://user-images.githubusercontent.com/103362361/188860325-a53560df-ca0a-4065-9b2a-ed4810c071dc.png"  width="200" height="200"/>|11 | Pleural thickening|<img src="https://user-images.githubusercontent.com/103362361/188863622-733c3db1-7295-4010-8649-56f2310f2ad6.png"  width="200" height="200"/>|
    |5 | [ILD(interstitial lung disease)](https://www.amc.seoul.kr/asan/healthinfo/disease/diseaseDetail.do?contentId=31848)|<img src="https://user-images.githubusercontent.com/103362361/188860660-5e410681-6a88-4e24-8b68-91d70ed991f0.png"  width="200" height="200"/>|12 | Pneumothorax|<img src="https://user-images.githubusercontent.com/103362361/188863766-89054ee8-8ba3-4255-8c5d-e5da9f78c323.png"  width="200" height="200"/>|
    |6 | Infiltration|<img src="https://user-images.githubusercontent.com/103362361/188860923-6284177b-452c-466f-b2ac-19427f7d2507.png"  width="200" height="200"/>|13 | Pulmonary fibrosis|<img src="https://user-images.githubusercontent.com/103362361/188863911-78194e9b-8c39-4c4b-835e-d3240f70c444.png"  width="200" height="200"/>| 
-->



   
### 2. 진행 내용

#### 1. data preprocessing - 추가정리필요

이미지가 적음 -> Augmentation이 필요하다고 판단. 그럼 어떤 기법을 적용시킬 것인가?? 

-> 비슷한 Task를 진행한 Reference들 참고. (폐X-ray이미지 Object Detection 논문들, 코로나로 관련 논문들이 많이 올라왔음)

주로 많이 한 Augmentation 기법 중 rotation 90도, zoom in, flip(horizontal)... 



#### 2. dataset 생성 및 구분 - 추가정리필요

Augmentation을 한 이미지들을 coco형식으로 만듬. 조원들에게 배포.

어떤 Augmentation이 성능향상에 좋았는지 비교를 위해 여러 데이터셋을 생성

분류(A)|분류(B)|분류(C)|분류(D)|
-------|-------|-------|-------|
원본|rotation : 90°|rotation : 90°|rotation : 90°|
&nbsp;|flip: horizontal|flip: horizontal|flip: horizontal|
&nbsp;|zoom: 10%|zoom: 10%|zoom: 10%|
&nbsp;|&nbsp;|cutmix|cutmix|
&nbsp;|&nbsp;|mosaic|mosaic|
&nbsp;|&nbsp;| CLAHE | CLAHE 
    






      
      
     




    
    
    
    
    
