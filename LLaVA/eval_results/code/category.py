import json

with open('/data2/yhhe/code/ScienceQA/data/scienceqa/llava_minitrain_realigned_2.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

with open('/data2/yhhe/code/ScienceQA/data/scienceqa/problems.json', 'r', encoding='utf-8') as file:
    problems = json.load(file)


for i in range(len(data)):
    data[i]["conversations"][1]["value"] = "The category of the problem is " + \
        problems[data[i]["id"]]["category"] + ". " + \
        data[i]["conversations"][1]["value"]


with open('/data2/yhhe/code/ScienceQA/data/scienceqa/llava_minitrain_realigned_3.json', 'w') as file:

    json.dump(data, file, indent=4)
