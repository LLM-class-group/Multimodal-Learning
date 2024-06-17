#!/bin/bash

# IMPORTANT: this is the training script for the original LLaVA, NOT FOR LLaVA V1.5!
# localhost 后跟要用的显卡编号
# 改相应参数使得乘积不变，详见readme
# 重跑前记得把output dir 删了，不然出事(貌似自动加载之前的权重，然后它不认识)
# todo save_steps 参数可能要略调小一些，用来保存，我们应该一共就199*epochs个。 
# --lora_enable True --lora_r 128 --lora_alpha 256 --mm_projector_lr 2e-5 \


DS_SKIP_CUDA_CHECK=1 deepspeed --include=localhost:1,2 --master_port=29600 /data2/yhhe/code/LLaVA/llava/train/train_mem.py \
    --deepspeed ./scripts/zero3_offload.json \
    --model_name_or_path lmsys/vicuna-13b-v1.3 \
    --version v1 \
    --data_path /data2/yhhe/code/ScienceQA/data/scienceqa/llava_minitrain_realigned_3.json \
    --image_folder /data2/yhhe/code/ScienceQA/data/scienceqa/images/train \
    --vision_tower openai/clip-vit-large-patch14 \
    --pretrain_mm_mlp_adapter ./checkpoints/llava-pretrain-vicuna-13b-v1.3/mm_projector.bin \
    --mm_vision_select_layer -2 \
    --mm_use_im_start_end False \
    --mm_use_im_patch_token False \
    --bf16 True \
    --output_dir ./checkpoints/llava-vicuna-13b-v1.3-realigned-3 \
    --num_train_epochs 12 \
    --per_device_train_batch_size 64 \
    --per_device_eval_batch_size 4 \
    --gradient_accumulation_steps 2 \
    --evaluation_strategy "no" \
    --save_strategy "steps" \
    --save_steps 20 \
    --save_total_limit 2 \
    --learning_rate 2e-5 \
    --weight_decay 0. \
    --warmup_ratio 0.03 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --tf32 True \
    --model_max_length 2048 \
    --gradient_checkpointing True \
    --dataloader_num_workers 4 \
    --lazy_preprocess True \
    --report_to wandb
