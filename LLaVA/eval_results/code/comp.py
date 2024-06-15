import json

with open('/data2/yhhe/code/LLaVA/eval_results/mini/llama-mini-origin-0/test_llava-13b_output.json', 'r', encoding='utf-8') as file1:
    data1 = json.load(file1)
with open('/data2/yhhe/code/LLaVA/eval_results/mini/llama-mini-realigned-0/test_llava-13b_output.json', 'r', encoding='utf-8') as file2:
    data2 = json.load(file2)

data1_id = 0
data2_id = 0
len1 = len(data1["incorrect"])
len2 = len(data2["incorrect"])
same = []
only1 = []
only2 = []

while data1_id < len1 and data2_id < len2:
    a1 = int(data1["incorrect"][data1_id]["question_id"])
    a2 = int(data2["incorrect"][data2_id]["question_id"])
    if a1 == a2 :
        data1_id = data1_id + 1
        data2_id = data2_id + 1
        same.append(a1)
    elif a1 < a2:
        data1_id = data1_id + 1
        only1.append(a1)
    elif a1 > a2:
        data2_id = data2_id + 1
        only2.append(a2)
while data1_id < len1:
    a1 = int(data1["incorrect"][data1_id]["question_id"])
    data1_id = data1_id + 1
    only1.append(a1)
while data2_id < len2:
    a2 = int(data2["incorrect"][data2_id]["question_id"])
    data2_id = data2_id + 1
    only1.append(a2)
print(f"same num:{len(same)};only1 num:{len(only1)};only2 num:{len(only2)}")
print(only2)