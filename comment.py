# -*- coding:utf-8 -*-
import requests

# 请求 URL（已包含完整参数）
url = "https://www.douyin.com/aweme/v1/web/comment/list/"

# 请求头（Headers）：模拟浏览器环境，提高请求成功率
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "Referer": "https://www.douyin.com/",
    "Accept": "application/json",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
}

# 请求参数（从 URL 中提取的查询参数）
params = {
    "device_platform": "webapp",
    "aid": "6383",
    "channel": "channel_pc_web",
    "aweme_id": "7537866571764174137",
    "cursor": "0",
    "count": "10",
    "item_type": "0",
    "insert_ids": "",
    "whale_cut_token": "",
    "cut_version": "1",
    "rcFT": "",
    "update_version_code": "170400",
    "pc_client_type": "1",
    "pc_libra_divert": "Windows",
    "support_h265": "1",
    "support_dash": "1",
    "cpu_core_num": "6",
    "version_code": "170400",
    "version_name": "17.4.0",
    "cookie_enabled": "true",
    "screen_width": "1920",
    "screen_height": "1080",
    "browser_language": "zh-CN",
    "browser_platform": "Win32",
    "browser_name": "Chrome",
    "browser_version": "139.0.0.0",
    "browser_online": "true",
    "engine_name": "Blink",
    "engine_version": "139.0.0.0",
    "os_name": "Windows",
    "os_version": "10",
    "device_memory": "8",
    "platform": "PC",
    "downlink": "1.3",
    "effective_type": "3g",
    "round_trip_time": "450",
    "webid": "7535069073778312738",
    "uifid": "1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee64740d2e774158a5ff949275fa8076e5fe433481a7d836cd9c619a2e1771a732aff0a4915821b3aa427925dd575eea7052e002694eef3ee6632bb357ac752f09e3575b0014027e3698bd41ce9e9a8278b00cfda4a956646bb886b9b325c146163157945297c907374d1a3b098577e9268e6d4ff60b258b63ec19c51087aad2b0ed0e4",
    "msToken": "xi7F6-JKf42ofd6u3lR2wfLwZbSkv76woozuSvs5UEkP0rIxq0olPsoQI6xorwKB9VGI1qdvBkmlcJOJ5IaP8YoHko8Ik9gCKSSOppeolaNCNfd56No90iLZYmDWnDU1kDZ5p7zu-jWMFHgM2MY0P9FBdT1cgzIwGBAZH17Tybgeq3venBQiEx8=",
    "a_bogus": "Ej4VDe6wYx%2FjadFSuOEUeR1UngIMNP8yPrTdWHeU7Ow4OhMTuRP-iPcWrxKNptmknmpwkeIHsfGAbnxcT0tiZ9npKmkfShiR64Vcnh6ohqNmG0JQEN6DS8WzFwMx0cGqeA5vi1kIhUeqgfdAkNQD%2FQAre%2FKK55uBFpxfk2TbT9sXZMgALZn3PQbgNwJqnj%3D%3D"
}

# 发送 GET 请求
try:
    response = requests.get(url, headers=headers, params=params, timeout=10)

    # 检查响应状态码
    if response.status_code == 200:
        # 打印返回的 JSON 数据
        data = response.json()
        print(data)
    else:
        print(f"请求失败，状态码：{response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"请求异常：{e}")