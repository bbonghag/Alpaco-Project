_base_ = [
    '../_base_/models/cascade_mask_rcnn_r50_fpn.py',
    '../_base_/datasets/coco_instance.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]

# log 저장 위치 - 구글드라이브에 interval당 pth파일 저장.
checkpoint_config = dict(interval=1,out_dir='/content/drive/MyDrive/dataset/lg/cascade_mask_rcnn_r50_fpn_1x_coco')

# 사전 가중치 사용(모델별 readme확인후 링크가져와서 사용.) - 12epoch
load_from = 'https://download.openmmlab.com/mmdetection/v2.0/cascade_rcnn/cascade_mask_rcnn_r50_fpn_1x_coco/cascade_mask_rcnn_r50_fpn_1x_coco_20200203-9d4dcb24.pth'