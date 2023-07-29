import csv
import json

# 读取fact.csv文件
with open('./Data/fact.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    json_list = []

    # 遍历每一行数据，构建json对象
    for row in reader:
        title = row['title']
        abstract = row['abstract']
        explain = row['explain']
        
        # 构建json对象
        json_obj = {
            "instruction": title + '请判断上述内容是以下四种谣言分类中的哪一种（确实如此，尚无定论，伪科学，伪常识），并以step by step的方式解释其判断过程。',
            "input": "",
            "output": '上述言论属于' + explain + ',因为' + abstract
        }
        
        json_list.append(json_obj)

# 将json对象列表保存为json文件
json_file_path = "./Data/rumor_dataset.json"
with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(json_list, jsonfile, ensure_ascii=False, indent=4)

json_file_path
