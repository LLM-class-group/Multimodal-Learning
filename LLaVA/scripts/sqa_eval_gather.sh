#!/bin/bash

CHUNKS=8
output_file="test_llava-13b.jsonl"

# Clear out the output file if it exists.
> "$output_file"

# Loop through the indices and concatenate each file.
for idx in $(seq 0 $((CHUNKS-1))); do
  cat "./test_llava-13b-chunk${idx}.jsonl" >> "$output_file"
done

python llava/eval/eval_science_qa.py \
    --base-dir /data2/yhhe/code/ScienceQA/data/scienceqa \
    --result-file ./test_llava-13b.jsonl \
    --output-file ./test_llava-13b_output.json \
    --output-result ./test_llava-13b_result.json




# for gathered
#!/bin/bash

# dirs=("/data2/yhhe/code/LLaVA/eval_results/llava-hf/" "/data2/yhhe/code/LLaVA/eval_results/llava-origin" "/data2/yhhe/code/LLaVA/eval_results/llava-realigned-v1-1" "/data2/yhhe/code/LLaVA/eval_results/llava-realigned-v1-2")

# for dir in ${dirs[@]}; do
#   result_file=${dir}"/test_llava-13b.jsonl"
#   output_file=${dir}"/test_llava-13b_output_eval_2.json"
#   output_result=${dir}"/test_llava-13b_result_eval_2.json"
#   python ../llava/eval/eval_science_qa.py \
#     --base-dir /data2/yhhe/code/ScienceQA/data/scienceqa \
#     --result-file ${result_file}\
#     --output-file ${output_file}\
#     --output-result ${output_result}
# done

