## LG화학 입자 형태 분석 모델 개발 해커톤 🏅🎖
### 입자 검출 정보를 기반으로 입자들의 형태 변화를 계량적 지표로 산출 가능한 모델 개발

---

## Description

대회 링크 : https://aifactory.space/competition/detail/2067

대회 기간 : 2022.07.07(목) 8:00 ~ 2022.08.08(월) 18:00

주최 : LG화학

주관 : AIFactory

주제 : 유체상에 떠다니는 입자를 촬영한 화상을 바탕으로 각 입자와 그 형상을 최대한 잘 검출해내는 Instance Segmentation 모델 개발.

팀 : DeepDream(조장 : 김x현, 조원 : 김x나, 이x정, 소x희, 이x학)




<img src="https://user-images.githubusercontent.com/103362361/187381517-1abe006c-6073-4f27-9e55-ae35d388828e.png"  width="500" height="300"/> <br/>

<br/>


1. 데이터 : LG화학에서 제공하느 유체상에 떠다니는 입자를 촬영한 사진.
   
   train dataset 520장, Test dataset 350장 및 어노테이션 파일(입자 레이블링 형식에 따라 label_train.json, label(polygon)train.json) 
   
   객체 카테고리는 1개(Normal) 클래스만 존재, 이미지 해상도는 (Height, Width) = (1024, 1280) 크기



2. 진행 내용

   애옹 김애옹.
   
   1주차(7/13 ~ 7/17) : Instance segmentation 공부, MMdetection 라이브러리 사용법 익히기, base-line 돌려보기, EDA(데이터분석)

   2주차(7/18 ~ 7/24) : Segmentation model 조원들에게 분배후 제출하여 점수가 높은 4가지 모델 (SCNet, Mask R-CNN, Mask Scoring R-CNN, Cascade Mask R-CNN) 
   선정 후 model 공부, modeling

   3주차(7/25 ~ 7/31) : 전처리 - Augmentation(이미지 증강 기법) 리스트업하여 각각 어떤 증강기법을 사용할 것인지 분배하고 성능확인 및 어떤걸 쓸지 선정.
   backbone 분배후 성능확인 및 backbone 선정

   4주차(8/1 ~ 8/8) : Optimizer, Lr-scheduler 분배 후 선정, 성능향상을 위한 하이퍼파라미터 조정. 
   
   
   
 3. 결과 : 62팀 중 7등 달성!

    동글동글
    
    
    
    
    <img src="https://user-images.githubusercontent.com/103362361/187385788-913ff59d-cc4a-4d4a-bebc-456c99575e92.png"  width="500" height="300"/> <br/>
    
    <br/>
    
    <img src="https://user-images.githubusercontent.com/103362361/187386154-609a16be-80f0-448a-8033-e97df87c3954.png"  width="500" height="300"/> <br/>
    
     < 예측 결과 이미지 >
    

   
---

## Usage Library & Baseline

Usage Library : MMdetection ( https://github.com/open-mmlab/mmdetection )

Base line : Mask R-CNN (대회측에서 baseline code 제공)

---




