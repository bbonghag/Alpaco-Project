# dataset settings
dataset_type = 'CocoDataset'
# data_root = 'data/coco/'

# # 데이터 폴더 설정
data_root = '/content/content/lg_test/mmdetection/data/dataset/'
classes = ('Normal',)

img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True, with_mask=True),
    # dict(type='Resize', img_scale=(1280,1024), keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    # dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels', 'gt_masks']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(1280,1024),
        flip=False,
        transforms=[
            # dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            # dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]

# 데이터 설정
data = dict(
    samples_per_gpu=1,
    workers_per_gpu=0,
    train=dict(
      type = dataset_type,
      img_prefix=data_root + "train/",
      classes = classes,
    #   ann_file=data_root + "aug_ro_label_train.json",
    #   ann_file=[data_root + "label(polygon)_train.json", data_root + 'Rotate_Rotation_annotations.coco.json', data_root +'bbox_rotate_rotation_annotations.coco.json'], 
        ann_file=data_root + "label(polygon)_train.json",
      pipeline=train_pipeline
),
    val=dict(
        type = dataset_type,
        img_prefix=data_root + "train/",
        classes = classes,
        # ann_file=data_root + "aug_ro_label_train.json", 
        # ann_file=[data_root + "label(polygon)_train.json", data_root + 'Rotate_Rotation_annotations.coco.json', data_root +'bbox_rotate_rotation_annotations.coco.json'], 
        ann_file=data_root + "label(polygon)_train.json",
        pipeline=train_pipeline
),
    test=dict(
        type = dataset_type,
        img_prefix=data_root + "test/",
        classes = classes,
        ann_file=data_root + "test.json",
        pipeline=test_pipeline
)
)

# 평가 방법
evaluation = dict(interval=1, metric=['bbox', 'segm'])

# max_epochs= 12
# num_last_epochs= 6
# # 평가 방법
# evaluation = dict(
#     metric=['bbox', 'segm'],
#     save_best='auto',
#     # The evaluation interval is 'interval' when running epoch is
#     # less than ‘max_epochs - num_last_epochs’.
#     # The evaluation interval is 1 when running epoch is greater than
#     # or equal to ‘max_epochs - num_last_epochs’.
#     interval=520, #best를 한 epoch당 주고 싶어서 우리의 data수 520으로
#     dynamic_intervals=[(max_epochs - num_last_epochs, 1)]
#     )

# 기존 데이터 양식
# data = dict(
#     samples_per_gpu=2,
#     workers_per_gpu=2,
#     train=dict(
#         type=dataset_type,
#         ann_file=data_root + 'annotations/instances_train2017.json',
#         img_prefix=data_root + 'train2017/',
#         pipeline=train_pipeline),
#     val=dict(
#         type=dataset_type,
#         ann_file=data_root + 'annotations/instances_val2017.json',
#         img_prefix=data_root + 'val2017/',
#         pipeline=test_pipeline),
#     test=dict(
#         type=dataset_type,
#         ann_file=data_root + 'annotations/instances_val2017.json',
#         img_prefix=data_root + 'val2017/',
#         pipeline=test_pipeline))
# evaluation = dict(metric=['bbox', 'segm'])
