#!/bin/bash

CHUNKS=8
dir="/data2/yhhe/code/LLaVA/eval_results/mini/llama-mini-realigned-40-0/"
output_file=${dir}"test_llava-13b.jsonl"

mkdir ${dir}

# Clear out the output file if it exists.
> "$output_file"

# Loop through the indices and concatenate each file.
for idx in $(seq 0 $((CHUNKS-1))); do
  cat "./test_llava-realigned-40-13b-chunk${idx}.jsonl" >> "$output_file"
done

python llava/eval/eval_science_qa.py \
    --base-dir /data2/yhhe/code/ScienceQA/data/scienceqa \
    --result-file ${output_file} \
    --output-file ${dir}/test_llava-13b_output.json \
    --output-result ${dir}/test_llava-13b_result.json




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

