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




<img src="https://user-images.githubusercontent.com/103362361/187381517-1abe006c-6073-4f27-9e55-ae35d388828e.png"  width="500" height="300"/>


1. 데이터 : LG화학에서 제공하느 유체상에 떠다니는 입자를 촬영한 사진.
   
   train dataset 520장, Test dataset 350장 및 어노테이션 파일(입자 레이블링 형식에 따라 label_train.json, label(polygon)train.json) 
   
   객체 카테고리는 1개(Normal) 클래스만 존재, 이미지 해상도는 (Height, Width) = (1024, 1280) 크기


2. 


---

## Usage Library & Baseline

Usage Library : MMdetection ( https://github.com/open-mmlab/mmdetection )

Base line : Mask R-CNN (대회측에서 baseline code 제공)

---




