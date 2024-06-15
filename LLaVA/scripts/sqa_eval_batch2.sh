CHUNKS=8
for IDX in {0..7}; do
    CUDA_VISIBLE_DEVICES=$IDX python -m llava.eval.model_vqa_science \
        --model-path /data2/yhhe/code/LLaVA/checkpoints/llava-vicuna-13b-v1.3-mini-realigned-2-12e \
        --question-file /data2/yhhe/code/ScienceQA/data/scienceqa/llava_test_QCM-LEA.json \
        --image-folder /data2/yhhe/code/ScienceQA/data/scienceqa/images/test \
        --answers-file ./test_llava-realigined-13b-chunk$CHUNKS_$IDX.jsonl \
        --num-chunks $CHUNKS \
        --chunk-idx $IDX \
        --temperature 0 \
        --conv-mode llava_v1 &
done