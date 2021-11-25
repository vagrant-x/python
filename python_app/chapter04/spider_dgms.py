import requests
import json
from multiprocessing import Queue
from handle_mongo import mongo_info
from concurrent.futures import ThreadPoolExecutor

# 数据队列
queue_list = Queue()


# 请求数据方法
def handel_request(url, data):
    header = {
        # "Cookie": "duid=69270019",
        "client": "4",
        "version": "7106.2",
        # "channel": "baidu",
        "act-code": "1637324809",
        "act-timestamp": "1637324809",
        "pset": "1",
        # "pseudo-id": "44c57e66cae004c9",
        "device": "SM-N976N",
        "brand": "samsung",
        "sdk": "25,7.1.2",
        "resolution": "1280*720",
        "dpi": "1.5",
        "timezone": "28800",
        "language": "zh",
        "cns": "2",
        "imsi": "460071317077478",
        "uuid": "f4d26323-9b23-403c-9187-e662ba7fc470",
        "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; SM-N976N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36",
        "battery-level": "0.98",
        "battery-state": "3",
        "caid": "44c57e66cae004c9",
        "bssid": "AC:22:0B:07:74:4E",
        "display-resolution": "1280*720",
        "scale": "1.5",
        "reach": "1",
        "rom-version": "d2que-user 7.1.2 QP1A.190711.020 700211101 release-keys",
        "syscmp-time": "1635765679000",
        "countrycode": "CN",
        "sysmemory": "3186032640",
        "sysdisksize": "61.39 GB",
        "terms-accepted": "1",
        "newbie": "1",
        "app-state": "0",
        "bootmark": "822206a5-4ae7-412f-8e85-601e91ff3d10",
        "updatemark": "1635817290.809861000",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "Keep-Alive",
        "session-info": "O0y/dPYTJAm0BbGoew14b/fQctKsmmjzQdUMA09SAmiCS7mYzKaP/73rPRSMQ2uIW+v7/szNkhJjhWHJizw+1luYaLUqgMlU1ieRCbekVZspYwlXLyRowX2oEkhJ0MIj",
        "Host": "api.douguo.net",
        # "Content-Length": "179",
    }
    # 设置代理
    # proxies = {"http": "127.0.0.1:8888"}  # 通用代理
    # response = requests.post(url=url, headers=header, data=data, proxies=proxies)
    response = requests.post(url=url, headers=header, data=data)
    return response


# 请求菜谱分类页面
def handle_index():
    url = "https://api.douguo.net/recipe/flatcatalogs"
    data = {
        "client": "4",
        # "_session": "1637373525108351564145807749",
        # "v": "new1637324615",
        "_vs": "0",
        "sign_ran": "e53fd78533e564209a573d14bd449d83",
        "code": "a8665c30af67ce0c",
    }
    response = handel_request(url, data)
    # 解析数据
    index_response_dict = json.loads(response.text)
    for index_item in index_response_dict["result"]["cs"]:
        # print(index_item["name"])
        for index_item_1 in index_item["cs"]:
            data_2 = {
                "client": "4",
                # "_session": "1637373525108351564145807749",
                "keyword": index_item_1["name"],
                "order": "0",
                "_vs": "400",
                "type": "0",
                "auto_play_mode": "2",
                "sign_ran": "1ce60f6319b32e96194116a84c331275",
                "code": "bf2b7920137d77f9",
            }
            queue_list.put(data_2)
            # print("----->",index_item_1["name"])
    # print(response.text)


# 获取菜谱列表
def handle_caipu_list(data):
    print("当前处理的食材：", data["keyword"])
    caipu_list_url = "https://api.douguo.net/recipe/v2/search/0/20"
    caipu_list_response = handel_request(url=caipu_list_url, data=data)
    # print(caipu_list_response.text)
    caipu_list_response_dict = json.loads(caipu_list_response.text)
    for item in caipu_list_response_dict["result"]["list"]:
        caipu_info = {}
        caipu_info["shicai"] = data["keyword"]
        if item["type"] == 13:
            caipu_info["user_name"] = item["r"]["an"]
            caipu_info["shicai_id"] = item["r"]["id"]
            caipu_info["describe"] = item['r']['cookstory']
            caipu_info["caipu_name"] = item['r']['n']
            caipu_info["zuoliao_list"] = item['r']['major']
            # print(caipu_info)
            # 请求详细做法信息
            detail_url = "https://api.douguo.net/recipe/v2/detail/" + str(caipu_info["shicai_id"])
            detail_data = {
                "client": "4",
                "_session": "1637373525108351564145807749",
                "author_id": "0",
                "_vs": "11102",
                "_ext": '{"query":{"kw":' + caipu_info["shicai"] + ',"src":"11102","idx":"2","type":"13","id":' + str(caipu_info["shicai_id"]) + '"}}"',
                "is_new_user": "1",
                "sign_ran": "f588cc28475995ac6398393f5007e4be",
                "code": "584429579d7b207a",
            }
            detail_response = handel_request(detail_url, detail_data)
            detail_response_dict = json.loads(detail_response.text)
            caipu_info["tips"] = detail_response_dict["result"]["recipe"]["tips"]
            caipu_info["cook_step"] = detail_response_dict["result"]["recipe"]["cookstep"]
            print("当前入库菜谱是： ", caipu_info["caipu_name"])
            mongo_info.insert_item(caipu_info)  # 插入数据到mongodb
            print("插入完成")
        else:
             continue
        # print(item)


if __name__ == '__main__':
    # 插入一个菜谱
    # handle_index()
    # handle_caipu_list(queue_list.get())

    # 多线程抓取数据
    handle_index()
    pool = ThreadPoolExecutor(max_workers = 20)
    while queue_list.qsize() > 0:
        pool.submit(handle_caipu_list, queue_list.get())
