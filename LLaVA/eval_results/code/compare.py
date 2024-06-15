import json


def incorrect_arr(data):
    incorrect = data["incorrect"]
    arr = []
    for entry in incorrect:
        arr.append(int(entry["question_id"]))
    return arr


def intersection(a1, a2):
    return [value for value in a1 if value in a2]


def json_(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def compare3(data1, data2, data3):
    arr1 = incorrect_arr(data1)
    arr2 = incorrect_arr(data2)
    arr3 = incorrect_arr(data3)
    inter = intersection(arr1, arr2)
    inter = intersection(inter, arr3)
    common_cnt = len(inter)
    cnt1 = len(arr1)
    cnt2 = len(arr2)
    cnt3 = len(arr3)
    print(f"common incorrect count: {common_cnt}")
    print(f"incorrect count in file1: {cnt1}")
    print(f"incorrect count in file2: {cnt2}")
    print(f"incorrect count in file3: {cnt3}")


def compare2(data1, data2):
    arr1 = incorrect_arr(data1)
    arr2 = incorrect_arr(data2)
    inter = intersection(arr1, arr2)
    common_cnt = len(inter)
    cnt1 = len(arr1)
    cnt2 = len(arr2)
    print(f"common incorrect count: {common_cnt}")
    print(f"incorrect count in file1: {cnt1}")
    print(f"incorrect count in file2: {cnt2}")
    fal2 = [value for value in arr2 if value not in inter]
    print(fal2)


file1 = "/data2/yhhe/code/LLaVA/eval_results/llava-hf/test_llava-13b_output.json"
file2 = "/data2/yhhe/code/LLaVA/eval_results/llava-realigned-v4/test_llava-13b_output.json"
file3 = "/data2/yhhe/code/LLaVA/eval_results/llava-short-10e/test_llava-13b_output.json"


def main():
    data1 = json_(file1)
    data2 = json_(file2)
    data3 = json_(file3)

    compare2(data1, data2)


if __name__ == '__main__':
    main()
