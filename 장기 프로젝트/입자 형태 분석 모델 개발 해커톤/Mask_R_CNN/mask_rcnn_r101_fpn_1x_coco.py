_base_ = './mask_rcnn_r50_fpn_1x_coco.py'
model = dict(
    backbone=dict(
        depth=101,
        init_cfg=dict(type='Pretrained',
                      checkpoint='torchvision://resnet101')))


# log 저장 위치 - 구글드라이브에 interval당 pth파일 저장.
checkpoint_config = dict(interval=1,out_dir='/content/drive/MyDrive/dataset/lg/mask_rcnn_r101_fpn_1x_coco')

# 사전 가중치 사용(모델별 readme확인후 링크가져와서 사용.) - 12epoch
load_from = 'https://download.openmmlab.com/mmdetection/v2.0/mask_rcnn/mask_rcnn_r101_fpn_1x_coco/mask_rcnn_r101_fpn_1x_coco_20200204-1efe0ed5.pth'

