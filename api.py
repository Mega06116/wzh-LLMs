from zhipuai import ZhipuAI
import json
client = ZhipuAI(api_key="d73b11472acc79dc97599f8991ddb0a9.5lOHaIgroQavOTa6")
# 读取JSON文件
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
output_file_path = 'Conversation.json'
# 依次访问JSON文件中的信息，并调用API
for item in data:
    # 发送请求到API
    response = client.chat.completions.create(
        model="glm-4",
        messages=[
            {"role": "user", "content": item['content']}
        ],
    )
    content=response.choices[0].message.content
    print(content)
    data = {"instruction": item['content'], "output": content}
    with open(output_file_path, 'a', encoding='utf-8') as file:
        if file.tell() == 0:        # 文件为空时，直接写入字典
            json.dump(data, file, ensure_ascii=False)
        else:
            json.dump(data, file, ensure_ascii=False)# 写入逗号和新的一行，为后续追加内容做准备
        file.write(',\n')





