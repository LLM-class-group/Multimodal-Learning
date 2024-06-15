import json


def main():
    # 读取原始JSON文件
    with open("/data2/yhhe/code/ReAlign/code/dataset_short.json", 'r', encoding='utf-8') as f:
        short_data = json.load(f)

    with open("/data2/yhhe/code/ReAlign/code/realign_dataset.json", 'r', encoding='utf-8') as f2:
        realign_data = json.load(f2)

    output_data = []

    for entry in short_data:
        # 提取需要的字段
        new_entry = {
            "id": entry["id"],
            "image": entry["image"],
            "conversations": []
        } if "image" in entry else {
            "id": entry["id"],
            "conversations": []
        }

        # 遍历 items 并只保留需要的信息
        for item in entry["items"]:
            conversation = {
                "from": item["from"],
                "value": item["value"]
            }
            new_entry["conversations"].append(conversation)

        # 添加重整后的条目到新列表
        output_data.append(new_entry)

    for entry in realign_data:
        # 提取需要的字段
        new_entry = {
            "id": entry["id"],
            "image": entry["image"],
            "conversations": []
        } if "image" in entry else {
            "id": entry["id"],
            "conversations": []
        }

        # 遍历 items 并只保留需要的信息
        for item in entry["items"]:
            conversation = {
                "from": item["from"],
                "value": item["value"]
            }
            new_entry["conversations"].append(conversation)

        # 添加重整后的条目到新列表
        output_data.append(new_entry)

    # 保存转换后的结果到新的JSON文件
    with open('/data2/yhhe/code/ScienceQA/data/scienceqa/llava_minitrain_realigned_2.json', 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
