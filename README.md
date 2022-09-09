# Kaggle VinBigData Chest X-ray Abnormalities Detection 🏥📽

### Chest X-ray Image를 object detection을 통해 폐 관련 14가지 질병을 detection.  

---

## Description

Purpose : 의료 종사자가 X-ray 이미지를 보고 진단을 내릴때 도움을 주어서 업무 부담을 줄이고자 한 보조 프로그램.

Team : DeepDream (조장:김수현, 조원:이봉학, 김현나, 이x정, 소x희)

Challenge Link : https://www.kaggle.com/competitions/vinbigdata-chest-xray-abnormalities-detection

---

## WorkFlow

### 1. 데이터  

Kaggle의 14개 라벨의 이미지 15000장(512x512x3)  및 63574개의 라벨 csv 파일. 

[Image Dataset](https://www.kaggle.com/datasets/awsaf49/vinbigdata-512-image-dataset) & [Label Dataset](https://www.kaggle.com/datasets/awsaf49/vinbigdata-yolo-labels-dataset)

  - 데이터 분석
    - 라벨값과 병명
    - X-ray 이미지이기에 어느정도의 도메인 지식 및 조사가 필요. 각 라벨에 대한 사전조사를 하였다.
    
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
    
    <img src="https://user-images.githubusercontent.com/103362361/188309386-e74a9214-643e-495b-acb5-cf72e455e5b9.jpg"  width="400" height="300"/>
    
    => 💡 데이터 불균형이 심하다 -> 학습에 영향을 줄수있기에 이문제를 어떻게 다룰지에 대한 방법이 필요. (다운샘플링을 할것인지, 부족한 라벨에 대해서 추가적인 Augmentation을 해줄것인지 등등..)
  
<!--     |라벨|병명|사진|라벨|병명|사진|
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

#### 1. data preprocessing


      
      
     




    
    
    
    
    
