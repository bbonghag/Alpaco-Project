
### Data Preprocessing
- Augmentation
  - Rotation 90도
  - Flip(horizontal)
  - Zoomin 10%
  - CLAHE(Contrast Limited Adaptive Histogram Equalization)
  - EqualizeHist
  - Cutmix
  
- Imbalance  
  - 0,3,11,13번 라벨 다운샘플링 + 1,12번 라벨 Augmentation 6개 적용.
  
- Json-to-DataFrame
  - COCO형식의 Json에서 필요한 내용들만 뽑아서 데이터프레임으로 변환.
