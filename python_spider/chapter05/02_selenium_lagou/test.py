import requests

def get_page():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
        "referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
        "cookie": "RECOMMEND_TIP=true; user_trace_token=20210601203538-e427f31d-b9f1-4789-890e-3ec28256b015; LGUID=20210601203538-4dc03a6b-d8ac-44b3-ab4f-7a028f1820f4; _ga=GA1.2.550597581.1622550938; index_location_city=%E5%B9%BF%E5%B7%9E; JSESSIONID=ABAAAECABFAACEA08BE869362F4FC22BB367C9A6254D681; WEBTJ-ID=2021067%E4%B8%8B%E5%8D%886:43:47184347-179e61242e716b-0e8563ac5f425d-f7f1939-1049088-179e61242e8657; PRE_UTM=; PRE_HOST=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGSID=20210607184347-2ca9f203-3696-4a71-82a0-c18f6afb8748; PRE_SITE=https%3A%2F%2Fwww.lagou.com; privacyPolicyPopup=false; _gat=1; sensorsdata2015session=%7B%7D; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1622550938,1623062628; _gid=GA1.2.1673162386.1623062628; __lg_stoken__=fe729dd5651834f184e55f7e9fa924ad7eff25ad241ad31693d514d7431fa05da6ff2fbb2d319233bbff0ccf689b1eb6944fad126bc5cf36aafcebf1bf80632b65baa98cd29b; X_MIDDLE_TOKEN=4a41e51a64463984e7e964141a9fad0e; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1622550946,1623062642; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1623062663; TG-TRACK-CODE=search_code; X_HTTP_TOKEN=0c0ca74129bd7f36649260326124f204c78ab13708; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22179c79281ab2d4-0850daa7d5129f-1333062-1049088-179c79281ac160%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2291.0.4472.77%22%7D%2C%22%24device_id%22%3A%22179c79281ab2d4-0850daa7d5129f-1333062-1049088-179c79281ac160%22%7D; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1623062946; LGRID=20210607184907-ce26d3dd-fbae-4a43-9fdd-90a6d593edd9; SEARCH_ID=f9d09408c2bd433f9f691322086ad449",
        "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
    }

    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
        "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
        "Cookie": "RECOMMEND_TIP=true; user_trace_token=20210601203538-e427f31d-b9f1-4789-890e-3ec28256b015; LGUID=20210601203538-4dc03a6b-d8ac-44b3-ab4f-7a028f1820f4; _ga=GA1.2.550597581.1622550938; index_location_city=%E5%B9%BF%E5%B7%9E; JSESSIONID=ABAAAECABFAACEA08BE869362F4FC22BB367C9A6254D681; WEBTJ-ID=2021067%E4%B8%8B%E5%8D%886:43:47184347-179e61242e716b-0e8563ac5f425d-f7f1939-1049088-179e61242e8657; LGSID=20210607184347-2ca9f203-3696-4a71-82a0-c18f6afb8748; privacyPolicyPopup=false; sensorsdata2015session=%7B%7D; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1622550938,1623062628; _gid=GA1.2.1673162386.1623062628; __lg_stoken__=fe729dd5651834f184e55f7e9fa924ad7eff25ad241ad31693d514d7431fa05da6ff2fbb2d319233bbff0ccf689b1eb6944fad126bc5cf36aafcebf1bf80632b65baa98cd29b; X_MIDDLE_TOKEN=4a41e51a64463984e7e964141a9fad0e; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1622550946,1623062642; TG-TRACK-CODE=search_code; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1623067732; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22179c79281ab2d4-0850daa7d5129f-1333062-1049088-179c79281ac160%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2291.0.4472.77%22%7D%2C%22%24device_id%22%3A%22179c79281ab2d4-0850daa7d5129f-1333062-1049088-179c79281ac160%22%7D; LGRID=20210607200853-d885e04f-1673-44c9-9a9a-4f6877a29ced; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1623067739; X_HTTP_TOKEN=0c0ca74129bd7f36350860326124f204c78ab13708; SEARCH_ID=5a0edb8650ed4288a9be50960d665404",
        "Origin": "https://www.lagou.com",
        "x-anit-forge-code": "0",
        "x-anit-forge-token": "None",
        "x-requested-with": "XMLHttpRequest",
    }
    url = "https://www.lagou.com/jobs/8361719.html?show=9b1ec987ecac47ad8e478436fc5ce6b3"
    response = requests.get(url, headers=headers)
    print(response.content.decode("utf-8"))

def get_page2():
    pass


if __name__ == '__main__':
    get_page()