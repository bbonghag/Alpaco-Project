checkpoint_config = dict(interval=1)
# yapf:disable
# log_config = dict(
#     interval=50,
#     hooks=[
#         dict(type='TextLoggerHook'),
#         # dict(type='TensorboardLoggerHook')
#     ])

# wandb 사용 config
log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook', interval=500),
        dict(type='WandbLoggerHook',interval=1000,
            init_kwargs=dict(
                project='deepdream3',
                entity = 'leebongbong',
                name = 'mask_rcnn_r50_fpn_12epoch' # 사용할 모델에 맞게 이름 써주기
            ),
            )
    ])
# yapf:enable
custom_hooks = [dict(type='NumClassCheckHook')]

dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
resume_from = None
workflow = [('train', 1)]

# disable opencv multithreading to avoid system being overloaded
opencv_num_threads = 0
# set multi-process start method as `fork` to speed up the training
mp_start_method = 'fork'

# Default setting for scaling LR automatically
#   - `enable` means enable scaling LR automatically
#       or not by default.
#   - `base_batch_size` = (8 GPUs) x (2 samples per GPU).
auto_scale_lr = dict(enable=True, base_batch_size=16)
