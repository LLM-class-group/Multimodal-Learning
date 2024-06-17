#!/bin/bash

# CHUNKS=8
# for IDX in {0..7}; do
#     CUDA_VISIBLE_DEVICES=$IDX python -m llava.eval.model_vqa_science \
#         --model-path /data2/yhhe/code/LLaVA/checkpoints/llava-vicuna-13b-v1.3-mini-realigned-3 \
#         --question-file /data2/yhhe/code/ScienceQA/data/scienceqa/llava_test_QCM-LEA.json \
#         --image-folder /data2/yhhe/code/ScienceQA/data/scienceqa/images/test \
#         --answers-file ./test_llava-realigned-40-13b-chunk$CHUNKS_$IDX.jsonl \
#         --num-chunks $CHUNKS \
#         --chunk-idx $IDX \
#         --temperature 0 \
#         --conv-mode llava_v1 &
# done

CUDA_VISIBLE_DEVICES=1 python -m llava.eval.model_vqa_science \
        --model-path /data2/yhhe/code/LLaVA/checkpoints/llava-vicuna-13b-v1.3-mini-realigned-3 \
        --question-file /data2/yhhe/code/ScienceQA/data/scienceqa/llava_test_QCM-LEA.json \
        --image-folder /data2/yhhe/code/ScienceQA/data/scienceqa/images/test \
        --answers-file ./test_llava-realigned-3-13b-chunk0.jsonl \
        --num-chunks 2 \
        --chunk-idx 0 \
        --temperature 0 \
        --conv-mode llava_v1 &

CUDA_VISIBLE_DEVICES=2 python -m llava.eval.model_vqa_science \
        --model-path /data2/yhhe/code/LLaVA/checkpoints/llava-vicuna-13b-v1.3-mini-realigned-3 \
        --question-file /data2/yhhe/code/ScienceQA/data/scienceqa/llava_test_QCM-LEA.json \
        --image-folder /data2/yhhe/code/ScienceQA/data/scienceqa/images/test \
        --answers-file ./test_llava-realigned-3-13b-chunk1.jsonl \
        --num-chunks 2 \
        --chunk-idx 1 \
        --temperature 0 \
        --conv-mode llava_v1 &


# 

# CHUNKS=4

# CUDA_VISIBLE_DEVICES=0 python -m llava.eval.model_vqa_science \
#         --model-path /data2/yhhe/code/LLaVA/checkpoints/llava-vicuna-13b-v1.3-mini-realigned-2-12e \
#         --question-file /data2/yhhe/code/ScienceQA/data/scienceqa/llava_test_QCM-LEA.json \
#         --image-folder /data2/yhhe/code/ScienceQA/data/scienceqa/images/test \
#         --answers-file ./test_llava-13b-chunk0_realign.jsonl \
#         --num-chunks $CHUNKS \
#         --chunk-idx 0 \
#         --conv-mode llava_v1 &

# CUDA_VISIBLE_DEVICES=4 python -m llava.eval.model_vqa_science \
#         --model-path /data2/yhhe/code/LLaVA/checkpoints/llava-vicuna-13b-v1.3-mini-realigned-2-12e \
#         --question-file /data2/yhhe/code/ScienceQA/data/scienceqa/llava_test_QCM-LEA.json \
#         --image-folder /data2/yhhe/code/ScienceQA/data/scienceqa/images/test \
#         --answers-file ./test_llava-13b-chunk1_realign.jsonl \
#         --num-chunks $CHUNKS \
#         --chunk-idx 1 \
#         --conv-mode llava_v1 &

# CUDA_VISIBLE_DEVICES=5 python -m llava.eval.model_vqa_science \
#         --model-path /data2/yhhe/code/LLaVA/checkpoints/llava-vicuna-13b-v1.3-mini-realigned-2-12e \
#         --question-file /data2/yhhe/code/ScienceQA/data/scienceqa/llava_test_QCM-LEA.json \
#         --image-folder /data2/yhhe/code/ScienceQA/data/scienceqa/images/test \
#         --answers-file ./test_llava-13b-chunk2_realign.jsonl \
#         --num-chunks $CHUNKS \
#         --chunk-idx 2 \
#         --conv-mode llava_v1 &

# CUDA_VISIBLE_DEVICES=4 python -m llava.eval.model_vqa_science \
#         --model-path /data2/yhhe/code/LLaVA/checkpoints/llava-vicuna-13b-v1.3-mini-realigned-2-12e \
#         --question-file /data2/yhhe/code/ScienceQA/data/scienceqa/llava_test_QCM-LEA.json \
#         --image-folder /data2/yhhe/code/ScienceQA/data/scienceqa/images/test \
#         --answers-file ./test_llava-13b-chunk3_realign.jsonl \
#         --num-chunks $CHUNKS \
#         --chunk-idx 3 \
#         --conv-mode llava_v1 &

# wait