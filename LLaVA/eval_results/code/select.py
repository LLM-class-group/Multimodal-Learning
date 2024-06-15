import json
import random

with open('/data2/yhhe/code/ScienceQA/data/scienceqa/llava_train_QCM-LEA.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

minidata = random.sample(data,100)

minidata.sort(key=lambda item: int(item["id"]))

with open('/data2/yhhe/code/ScienceQA/data/scienceqa/llava_miniminitrain_QCM-LEA.json', 'w') as file:
    
    json.dump(minidata, file,indent=4)