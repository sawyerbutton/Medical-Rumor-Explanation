import csv
import json

# 读取fact.csv文件
with open('./Data/fact.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    huatuo_json_list = []
    med_chatglm_json_list = []


    # 遍历每一行数据，构建json对象
    for row in reader:
        title = row['title']
        abstract = row['abstract']
        explain = row['explain']
        
        # 构建json对象
        json_obj1 = {
            "instruction": title + '请判断上述内容是以下四种谣言分类中的哪一种（确实如此，尚无定论，伪科学，伪常识），并以step by step的方式解释其判断过程。',
            "input": "",
            "output": "上述言论属于" + explain + ",因为" + abstract
        }

        json_obj2 = {
            "context":"问题：请判断三引号中的内容是以下四种谣言分类中的哪一种（确实如此，尚无定论，伪科学，伪常识），并以step by step的方式解释其判断过程，'''" + title + "''' \n 回答:",
            "target":"上述言论属于" + explain + ",因为"+ abstract
        }
        
        huatuo_json_list.append(json_obj1)
        med_chatglm_json_list.append(json_obj2)

# 将json对象列表保存为json文件
json_file_path1 = "./Data/huatuo_rumor_dataset.json"
json_file_path2 = "./Data/med_chatglm_rumor_dataset.json"

with open(json_file_path1, 'w', encoding='utf-8') as jsonfile:
    json.dump(huatuo_json_list, jsonfile, ensure_ascii=False, indent=4)
with open(json_file_path2, 'w', encoding='utf-8') as jsonfile:
    json.dump(med_chatglm_json_list, jsonfile, ensure_ascii=False, indent=4)

