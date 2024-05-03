import pandas as pd
import json
# 读取CSV文件
df = pd.read_csv(r'C:\Users\Lenovo\Desktop\lawzhidao_filter.csv')
# 读取df的title和reply列
data=df[['title', 'reply']]
# 遍历DataFrame的每一行，并创建JSON对象
json_data = [{"input": row["title"], "output": row["reply"]} for index, row in data.iterrows()]
# 将JSON对象保存到一个大的JSON数组中
json_str = json.dumps(json_data, indent=4)
# 将JSON字符串写入到一个名为'output.json'的文件中
with open(r'C:\Users\Lenovo\Desktop\output.json', 'w',encoding='utf-8') as json_file:
    json_file.write(json_str)
