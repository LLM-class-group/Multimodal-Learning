import json

# 假设你的 JSON 数据保存在名为 data.json 的文件中
json_file = '/data2/yhhe/code/ScienceQA/data/scienceqa/llava_minitrain_QCM-LEA.json'

# 读取 JSON 文件
with open(json_file, 'r', encoding='utf-8') as file:
    all_data = json.load(file)

# 初始化一个列表来存储符合条件的元素
filtered_elements = []


for data in all_data:
    # 遍历 conversations 列表
    for conversation in data.get('conversations', []):
        if conversation.get('from') == 'gpt' and len(conversation.get('value', '')) < 200:
            filtered_elements.append(data)

out_file = '/data2/yhhe/code/ScienceQA/data/scienceqa/llava_minitrain_filt_short.json'
# 输出符合条件的元素
with open(out_file, 'w', encoding='utf-8') as file:
    json.dump(filtered_elements, file, indent=4)
