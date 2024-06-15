import json
# from classification import get_category


def convert_json_format(input_data):
    # 初始化结果列表
    result = []
    result_short = []

    # 遍历数据中的每个对话组
    for entry in input_data:
        short = False

        item = {
            "id": entry["id"],
            "items": []
        } if "image" not in entry else {
            "id": entry["id"],
            "image": entry["image"],
            "items": []
        }

        # 遍历每个对话组中的对话
        for conv in entry['conversations']:
            if conv['from'] == 'human':
                category = "exam_problem_solving_tutor"
                item['items'].append({
                    "from": conv['from'],
                    "value": conv['value'],
                    "category": category
                })
            else:
                if len(conv['value']) < 200:
                    short = True
                item['items'].append({
                    "from": conv['from'],
                    "value": conv['value']
                })

        if short:
            result_short.append(item)
        else:
            result.append(item)

    return result, result_short


def main():
    # 读取原始JSON文件
    with open('/data2/yhhe/code/ScienceQA/data/scienceqa/llava_minitrain_QCM-LEA.json', 'r', encoding='utf-8') as f:
        input_data = json.load(f)

    # 转换JSON格式
    output_data, output_data_short = convert_json_format(input_data)

    # 保存转换后的结果到新的JSON文件
    with open('dataset.json', 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)

    # 保存转换后的结果到新的JSON文件
    with open('dataset_short.json', 'w', encoding='utf-8') as f:
        json.dump(output_data_short, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
