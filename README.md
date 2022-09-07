## Kaggle VinBigData Chest X-ray Abnormalities Detection 🏥📽

### Chest X-ray Image를 object detection을 통해 폐 관련 14가지 질병을 detection.  

Purpose : 의료 종사자가 X-ray 이미지를 보고 진단을 내릴때 도움을 주어서 업무 부담을 줄이고자 한 보조 프로그램.

Team : DeepDream (조장:김x현, 조원:이x학, 김x나, 이x정, 소x희)

Challenge Link : https://www.kaggle.com/competitions/vinbigdata-chest-xray-abnormalities-detection

---

### Description

1. 데이터 : Kaggle의 14개 라벨의 이미지 15000장(512x512x3)  및 63574개의 라벨 csv 파일. [Image Dataset](https://www.kaggle.com/datasets/awsaf49/vinbigdata-512-image-dataset), [Label Dataset](https://www.kaggle.com/datasets/awsaf49/vinbigdata-yolo-labels-dataset)

  - 데이터 분석
    - 라벨값과 병명
    
    |라벨|병명|사진|
    |----|----|----|
    |0 | [Aortic enlargement](https://www.baptisthealth.com/services/heart-care/conditions/aortic-aneurysm-enlarged-aorta)|<img src="https://user-images.githubusercontent.com/103362361/188856182-1965963c-7a6b-4fb2-a867-0a3ec25842a6.png"  width="200" height="200"/>|
    |1 | [Atelectasis](https://terms.naver.com/entry.naver?docId=927036&cid=51007&categoryId=51007)|<img src="https://user-images.githubusercontent.com/103362361/188856681-f3db74aa-9db1-43be-9a6e-32b3b974b4f1.png"  width="200" height="200"/>|
    |2 | [Calcification](https://terms.naver.com/entry.naver?docId=493788&cid=60408&categoryId=55558)|<img src="https://user-images.githubusercontent.com/103362361/188857391-3eaec5b8-6e2a-4cac-8cca-9d1b38212c6d.png"  width="200" height="200"/>|
    |3 | [Cardiomegaly](https://terms.naver.com/entry.naver?docId=927305&cid=51007&categoryId=51007)|<img src="https://user-images.githubusercontent.com/103362361/188857765-79d8fef5-ad5d-4e1d-b923-46587cd76e49.png"  width="200" height="200"/>|
    |4 | Consolidation|
    |5 | ILD|
    |6 | Infiltration|
    |7 | Lung Opacity|
    |8 | Nodule/Mass|
    |9 | Other lesion|
    |10 | Pleural effusion|
    |11 | Pleural thickening|
    |12 | Pneumothorax|
    |13 | Pulmonary fibrosis|
    <img src="https://user-images.githubusercontent.com/103362361/188309386-e74a9214-643e-495b-acb5-cf72e455e5b9.jpg"  width="400" height="300"/>
    
    
    
    
    
