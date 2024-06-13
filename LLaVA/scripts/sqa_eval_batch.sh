#!/bin/bash

CHUNKS=6
for IDX in {0..5}; do
# for IDX in {0,1}; do
    CUDA_VISIBLE_DEVICES=$IDX python -m llava.eval.model_vqa_science \
        --model-path /data2/yhhe/code/LLaVA/checkpoints/llava-vicuna-13b-v1.3-short-12e/checkpoint-1200 \
        --question-file /data2/yhhe/code/ScienceQA/data/scienceqa/llava_test_QCM-LEA.json \
        --image-folder /data2/yhhe/code/ScienceQA/data/scienceqa/images/test \
        --answers-file ./test_llava-13b-chunk$CHUNKS_$IDX.jsonl \
        --num-chunks $CHUNKS \
        --chunk-idx $IDX \
        --conv-mode llava_v1 &
done

# --model-path /data2/yhhe/code/LLaVA/checkpoints/llava-vicuna-13b-v1.3-pretrain_lcs558k_plain-ScienceQA_QCM_LEA-12e \
# --model-path liuhaotian/llava-lcs558k-scienceqa-vicuna-13b-v1.3 \

# CUDA_VISIBLE_DEVICES=7 python -m llava.eval.model_vqa_science \
#         --model-path /data2/yhhe/code/LLaVA/checkpoints/llava-vicuna-13b-v1.3-short-12e/checkpoint-800 \
#         --question-file /data2/yhhe/code/ScienceQA/data/scienceqa/llava_test_QCM-LEA.json \
#         --image-folder /data2/yhhe/code/ScienceQA/data/scienceqa/images/test \
#         --answers-file ./test_llava-13b-chunk2.jsonl \
#         --num-chunks $CHUNKS \
#         --chunk-idx 2 \
#         --conv-mode llava_v1 &