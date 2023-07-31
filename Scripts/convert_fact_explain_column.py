import pandas as pd

# 读取CSV文件
df = pd.read_csv('./Data/fact.csv')

# 查看前几行数据，以及确认explain这一列的唯一值
df_head = df.head()
unique_explain_values = df['explain'].unique()

# df_head, unique_explain_values

# 将“伪科学”和“伪常识”修正成“证实为不真实”
df['explain'] = df['explain'].replace(['伪科学', '伪常识'], '证实为不真实')

# 查看修改后的explain这一列的唯一值
updated_unique_explain_values = df['explain'].unique()
# updated_unique_explain_values

json_path = "./Data/fact_updated.json"
df.to_json(json_path, orient='records', lines=True, force_ascii=False)