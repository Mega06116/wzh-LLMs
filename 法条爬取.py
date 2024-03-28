import requests
import os
import time
import random
# 确保目标文件夹存在
filename = '法律条文\\'
if not os.path.exists(filename):
    os.mkdir(filename)
# API的基础URL和请求头
url = 'https://flk.npc.gov.cn/api/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
# 初始页码
page = 1

# 用于停止循环的条件，例如当API返回的数据量少于请求的数量时
while True:
    # 构建请求参数
    data = {
        'type': 'flfg',
        'searchType': 'title;vague',
        'sortTr': 'f_bbrq_s;desc',
        'gbrqStart': '',
        'gbrqEnd': '',
        'sxrqStart': '',
        'sxrqEnd': '',
        'sort': 'true',
        'page': str(page),
        'size': '10',
        '_': '1704800783355',
    }

    # 发送GET请求
    response = requests.get(url=url, params=data, headers=headers)
    data_json = response.json()

    # 检查是否有数据返回
    if not data_json['result']['data']:
        break  # 如果没有数据，退出循环
    # 处理返回的数据
    for index in data_json['result']['data']:
        id = index['id']
        title = index['title']
        detail_url = 'https://flk.npc.gov.cn/api/detail'
        detail_data = {
            'id': id
        }
        new_data = requests.post(url=detail_url, data=detail_data, headers=headers).json()
        try:
            body_data = new_data['result']['body'][0]
            down_load = 'https://wb.flk.npc.gov.cn' + body_data['path']
            name = body_data['path'].split('.')[-1]
            content = requests.get(url=down_load, headers=headers).content
            with open(f'法律条文\\{title}.{name}', mode='wb') as f:
                f.write(content)
            print(title, down_load, name)
            time.sleep(random.randint(1,2))
        except (TypeError, KeyError, IndexError) as e:
            # 如果遇到错误，打印错误消息并继续
            print(f"Error processing title: {title}. Error: {e}")
            continue
        down_load = 'https://wb.flk.npc.gov.cn' + new_data['result']['body'][0]['path']
        name = new_data['result']['body'][0]['path'].split('.')[-1]
        content = requests.get(url=down_load, headers=headers).content
        with open(f'法律条文\\{title}.{name}', mode='wb') as f:
            f.write(content)

        print(title, down_load, name)

    # 页码递增
    page += 1