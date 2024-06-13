import json


def replace_answer(input_string, answer):
    # 查找 "The answer is" 的位置
    index = input_string.find("The answer is")
    tail = "The answer is " + answer + "."

    # 查找 "The answer is [A-Z]." 是否存在
    exist = input_string.find(tail) != -1

    no_find = False

    # 如果找到了 "The answer is"
    if index != -1:
        # 创建新的字符串，保留 "The answer is" 之前的部分，并加上新的答案
        output_string = input_string[:index +
                                     len("The answer is")] + " " + answer + "."
    else:
        # 如果没找到 "The answer is"，拼接"The answer is"字符串
        no_find = True
        therefore = input_string.find("Therefore,")
        if therefore != -1:
            # 创建新的字符串，保留 "Therefore," 之前的部分，并加上新的答案
            output_string = input_string[:therefore] + tail
            # print(f"corrected test string:\n {output_string}\n")
        else:
            output_string = input_string + " " + tail
            # print(f"corrected error string:\n {output_string}\n")

    updated = input_string != output_string

    return output_string, updated, exist, no_find


def reformat_json(data, problems):
    # 初始化一个新的列表来存储重整后的数据
    new_data = []
    corrected = 0
    existed = 0
    total = len(data)
    no_found = 0

    for entry in data:
        # 提取需要的字段
        new_entry = {
            "id": entry["id"],
            "image": entry["image"],
            "conversations": []
        } if "image" in entry else {
            "id": entry["id"],
            "conversations": []
        }

        answer = chr(int(problems[entry["id"]]["answer"]) + 65)  # 'A' = 65

        # 遍历 items 并只保留需要的信息
        for item in entry["items"]:
            from_ = item["from"]
            value_ = item["value"]

            if str(from_) == "gpt":
                # aver_len += len(value_)
                # max_len = max(max_len, len(value_))
                value_, updated, exist, no_find = replace_answer(
                    value_, answer)
                # max_len_v2 = max(max_len_v2, len(value_))
                if updated:
                    corrected += 1
                if exist:
                    existed += 1
                if no_find:
                    no_found += 1

            conversation = {
                "from": from_,
                "value": value_
            }
            new_entry["conversations"].append(conversation)

        # 添加重整后的条目到新列表
        new_data.append(new_entry)

    print(f"corrected answer: {corrected}")
    print(f"existed answer: {existed}")
    print(f"no found answer: {no_found}")
    print(f"total: {total}")

    return new_data


def reformat_json_2(data, problems):
    # 初始化一个新的列表来存储重整后的数据
    new_data = []

    for entry in data:
        # 提取需要的字段
        new_entry = {
            "id": entry["id"],
            "image": entry["image"],
            "conversations": []
        } if "image" in entry else {
            "id": entry["id"],
            "conversations": []
        }

        answer = chr(int(problems[entry["id"]]["answer"]) + 65)  # 'A' = 65

        # 遍历 items 并只保留需要的信息
        for item in entry["items"]:
            from_ = item["from"]
            value_ = item["value"]

            if str(from_) == "gpt":
                value_ = answer + "."

            conversation = {
                "from": from_,
                "value": value_
            }
            new_entry["conversations"].append(conversation)

        # 添加重整后的条目到新列表
        new_data.append(new_entry)

    return new_data


def main():
    # 读取原始JSON文件
    with open("/data2/yhhe/code/ReAlign/code/realign_dataset.json", 'r', encoding='utf-8') as f:
        input_data = json.load(f)

    with open("/data2/yhhe/code/ScienceQA/data/scienceqa/problems.json", 'r', encoding='utf-8') as f2:
        problems = json.load(f2)

    # 转换JSON格式
    output_data = reformat_json_2(input_data, problems)

    # 保存转换后的结果到新的JSON文件
    with open('/data2/yhhe/code/ScienceQA/data/scienceqa/llava_train_short_v2.json', 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
