# 查找替换 llava-realigned-v4

# 创建目标目录，如果它不存在
mkdir -p eval_results/llava-realigned-v4

# 移动文件到目标目录
mv test_llava-13b.jsonl eval_results/llava-realigned-v4/test_llava-13b.jsonl
mv test_llava-13b_result.json eval_results/llava-realigned-v4/test_llava-13b_result.json
mv test_llava-13b_output.json eval_results/llava-realigned-v4/test_llava-13b_output.json

# 小心！
# rm test_llava-13b-chunk*.jsonl