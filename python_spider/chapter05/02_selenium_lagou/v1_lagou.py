import requests, time, re
from lxml import etree

# Cookie 的过期时间比较短，需要重新复制后放进去
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
    "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
    "Origin": "https://www.lagou.com",
    "x-anit-forge-code": "0",
    "x-anit-forge-token": "None",
    "x-requested-with": "XMLHttpRequest",
    "Cookie": "RECOMMEND_TIP=true; user_trace_token=20210601203538-e427f31d-b9f1-4789-890e-3ec28256b015; LGUID=20210601203538-4dc03a6b-d8ac-44b3-ab4f-7a028f1820f4; _ga=GA1.2.550597581.1622550938; index_location_city=%E5%B9%BF%E5%B7%9E; JSESSIONID=ABAAAECABFAACEA08BE869362F4FC22BB367C9A6254D681; WEBTJ-ID=2021067%E4%B8%8B%E5%8D%886:43:47184347-179e61242e716b-0e8563ac5f425d-f7f1939-1049088-179e61242e8657; LGSID=20210607184347-2ca9f203-3696-4a71-82a0-c18f6afb8748; privacyPolicyPopup=false; sensorsdata2015session=%7B%7D; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1622550938,1623062628; _gid=GA1.2.1673162386.1623062628; __lg_stoken__=fe729dd5651834f184e55f7e9fa924ad7eff25ad241ad31693d514d7431fa05da6ff2fbb2d319233bbff0ccf689b1eb6944fad126bc5cf36aafcebf1bf80632b65baa98cd29b; X_MIDDLE_TOKEN=4a41e51a64463984e7e964141a9fad0e; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1622550946,1623062642; TG-TRACK-CODE=search_code; _gat=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22179c79281ab2d4-0850daa7d5129f-1333062-1049088-179c79281ac160%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2291.0.4472.77%22%7D%2C%22%24device_id%22%3A%22179c79281ab2d4-0850daa7d5129f-1333062-1049088-179c79281ac160%22%7D; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1623070021; LGRID=20210607204701-1dea870e-f70e-4338-ace7-0ad717d92356; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1623070027; X_HTTP_TOKEN=0c0ca74129bd7f36651070326124f204c78ab13708; SEARCH_ID=f78e0045512c4e6f99eba1f525aef4f2"
}

def parse_detail_page(url, cookies):
    # 获取职位详细信息页面数据
    response = requests.get(url=url, headers=headers, cookies=cookies)
    text = response.content.decode("utf-8")
    html = etree.HTML(text)
    p_name = html.xpath("//span[@class='position-head-wrap-name']/text()")[0]
    job_request_spans = html.xpath("//dd[@class='job_request']//span")
    p_salary = job_request_spans[0].xpath(".//text()")[0]
    p_city = job_request_spans[1].xpath(".//text()")[0]
    p_city = re.sub(r"[\s/]", "", p_city)
    p_years = job_request_spans[2].xpath(".//text()")[0]
    p_years = re.sub(r"[\s/]", "", p_years)
    p_education = job_request_spans[3].xpath(".//text()")[0]
    p_education = re.sub(r"[\s/]", "", p_education)
    p_detail = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()
    p_info = {
        "p_name": p_name,
        "p_salary": p_salary,
        "p_city": p_city,
        "p_years": p_years,
        "p_education": p_education,
        "p_detail": p_detail,
    }
    print(p_info)
    print("* " * 20)
    return p_info

def main():
    all_position = []
    url = "https://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false"
    # 这个例子只爬取前五页内容
    for i in range(5):
        print("* " * 10 + "开始获取第 {} 页面".format(i))
        # 拼接请求的数据
        data = {
            "first": "false",
            "pn": "{}".format(i),
            "kd": "python"
        }
        # 获取职位信息
        response = requests.post(url=url, headers= headers, data=data)
        # 获取职位信息
        positions = response.json()["content"]["positionResult"]["result"]
        time.sleep(1)
        # 获取职位id,id是请求数据url的构成部分
        for position in positions:
            positionId = position["positionId"]
            position_url = "https://www.lagou.com/jobs/{}.html".format(positionId)
            cookies = response.cookies
            p = parse_detail_page(position_url, cookies)
            time.sleep(1)
            all_position.append(p)
    print(all_position)


if __name__ == '__main__':
    main()
"""
遇到问题
    请求第一页的第一条连接之后，后面被识别出来是爬虫，第二条详情就请求不到了        
"""