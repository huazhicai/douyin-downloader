import requests
from urllib.parse import urlencode

# 请求 URL 基础地址
url = "https://www-hj.douyin.com/aweme/v1/web/comment/list/"

# 查询参数（query parameters）
params = {
    "device_platform": "webapp",
    "aid": "6383",
    "channel": "channel_pc_web",
    "aweme_id": "7538929120571575612",  # 视频 ID
    "cursor": "10",
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
    "downlink": "1.35",
    "effective_type": "3g",
    "round_trip_time": "350",
    "webid": "7535069073778312738",
    "uifid": "1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee64740d2e774158a5ff949275fa8076e5fe433481a7d836cd9c619a2e1771a732aff0a4915821b3aa427925dd575eea7052e002694eef3ee6632bb357ac752f09e3575b0014027e3698bd41ce9e9a8278b00cfda4a956646bb886b9b325c146163157945297c907374d1a3b098577e9268e6d4ff60b258b63ec19c51087aad2b0ed0e4",
    "msToken": "wo6Yxn16ak_TLpev6vStonfvoYWchMsp_A9mfIZ1Y7pcHo608hFBFQeGn0RazGeXm5lVg3zBOAOkFVloYehd4FMWKLWQFaUdvs1tx_xpAyTrfw7norw5uQu3tLrnco0vzNW6jj0MHQ1SvMLIZ9Oi9ahNzLATT7GB1GwwrCh3Asfe0g==",
    "a_bogus": "OfU5ht6JOZ8jKd%2FGYKsc71Il9Lj%2FNs8yQeiQWwBPyNPdcwtTjRPlirSCbxz7EhmJ3RBwkFMH4nPAadxbT0XkZHckqmpvSgsfv0VIn6vogqiRTzkQLNjmCzuzKwMx0c4ql55Ui1h6gUtqgfVAwrdE%2FBlJt%2FKFQ58BPpxjkMYcT9sg106Ag3c3Ppthxwiq4f%3D%3D",
    "verifyFp": "verify_mdflalvf_lsqPlNtb_3MKY_42Dk_9lO0_xnb1vqXHICKv",
    "fp": "verify_mdflalvf_lsqPlNtb_3MKY_42Dk_9lO0_xnb1vqXHICKv"
}

# 完整 URL
full_url = url + "?" + urlencode(params, safe='=')

# 请求头（Headers）
headers = {
    "Host": "www-hj.douyin.com",
    "Connection": "keep-alive",
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua": '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    "bd-ticket-guard-web-version": "2",
    "sec-ch-ua-mobile": "?0",
    "bd-ticket-guard-client-data": "eyJ0c19zaWduIjoidHMuMi41MzkwZTg4Zjk1ZDlmZDU4ZmY2MjZjMjEyMTVkMzUzZDAzNjZjMmYxMGNlMDA5MzcyMTQ2NzM3ZDgzZDQwM2I5YzRmYmU4N2QyMzE5Y2YwNTMxODYyNGNlZGExNDkxMWNhNDA2ZGVkYmViZWRkYjJlMzBmY2U4ZDRmYTAyNTc1ZCIsInJlcV9jb250ZW50IjoidGlja2V0LHBhdGgsdGltZXN0YW1wIiwicmVxX3NpZ24iOiIxYi9uWTYyU3I1SFNRczNMeTdaRGFndjlBb1hRVUcyTzRXVXBxNEQrL3pJPSIsInRpbWVzdGFtcCI6MTc1NTQxODQwMn0=",
    "uifid": "1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee64740d2e774158a5ff949275fa8076e5fe433481a7d836cd9c619a2e1771a732aff0a4915821b3aa427925dd575eea7052e002694eef3ee6632bb357ac752f09e3575b0014027e3698bd41ce9e9a8278b00cfda4a956646bb886b9b325c146163157945297c907374d1a3b098577e9268e6d4ff60b258b63ec19c51087aad2b0ed0e4",
    "bd-ticket-guard-web-sign-type": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "bd-ticket-guard-iteration-version": "1",
    "bd-ticket-guard-ree-public-key": "BLjA8Aqkmt1JBGlAI/lrs8qw91YQng3nAC6jAFzyaDpFM2HbmlniwHwpscUA7Tvtd/1Jc+VE8EYDuSdyMr5n7RA=",
    "bd-ticket-guard-version": "2",
    "Origin": "https://www.douyin.com",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.douyin.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cookie": "store-region=cn-zj; store-region-src=uid; live_use_vvc=%22false%22; hevc_supported=true; SelfTabRedDotControl=%5B%5D; enter_pc_once=1; is_dash_user=1; bd_ticket_guard_client_web_domain=2; passport_csrf_token=2415cd8689ad08b962e7899a534e0e6b; passport_csrf_token_default=2415cd8689ad08b962e7899a534e0e6b; n_mh=DMjMIGF989zvuX5IlA7I0mQfqKTprkKmSKCD5WVhBc8; __security_server_data_status=1; my_rd=2; UIFID_TEMP=1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee64740d2e774158a5ff949275fa8076e5fe433c99902203737572e48caef12c790285484b7fc23a7a076d997cc0e5c8ac57343; UIFID=1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee64740d2e774158a5ff949275fa8076e5fe433481a7d836cd9c619a2e1771a732aff0a4915821b3aa427925dd575eea7052e002694eef3ee6632bb357ac752f09e3575b0014027e3698bd41ce9e9a8278b00cfda4a956646bb886b9b325c14616315790660e89cdca7af68b56b5ace2d372a07490b63066d9e52eeaa6c254f5c5144ba; SEARCH_RESULT_LIST_TYPE=%22single%22; __security_mc_1_s_sdk_crypt_sdk=f93ad827-439f-8733; h265ErrorNum=-1; d_ticket=80ab3dc01b97e933a205e1e1369201b64ed19; passport_auth_status=1e49e71e08907180ae52996c113bc919%2C65b4eedbf6adf684de6a5819d57968bf; passport_auth_status_ss=1e49e71e08907180ae52996c113bc919%2C65b4eedbf6adf684de6a5819d57968bf; __security_mc_1_s_sdk_cert_key=3c13c0f5-413b-afc0; passport_mfa_token=CjGT8qMsZ1QC%2BptGqZhlMlsP%2FPst8liDQ7yO1DPfdN93WYcZvtlyybWe12nhcbvVwOt0GkoKPAAAAAAAAAAAAABPVnjfMC0PRuiQFcIoKotjXdRycWHrj4r5Qj0E2uibC3nUVLV9jHP%2FlPLC2Iduj5R8CxDvh%2FkNGPax0WwgAiIBA0UcdoU%3D; passport_assist_user=CkECexkikJthd2LU1BfybBM0V6ol2trHMzlMRrQL2-Prs99gc3V5xRaHA4DkPoHtc0beDhEUcmaVSMIoBI-b3yHwABpKCjwAAAAAAAAAAAAAT1btf7q77WDofFNo22ImTPQunYt3PG7cnOBHJc37uy2S3MvzhbCXkB9rZTOPaF21RSsQ74f5DRiJr9ZUIAEiAQPU3c2m; sid_guard=02a23c42fbac82350863df18eeb7fdbe%7C1754794784%7C5184000%7CThu%2C+09-Oct-2025+02%3A59%3A44+GMT; uid_tt=e0251e33445e7cec6fb091493aba3591; uid_tt_ss=e0251e33445e7cec6fb091493aba3591; sid_tt=02a23c42fbac82350863df18eeb7fdbe; sessionid=02a23c42fbac82350863df18eeb7fdbe; sessionid_ss=02a23c42fbac82350863df18eeb7fdbe; session_tlb_tag=sttt%7C18%7CAqI8QvusgjUIY98Y7rf9vv_________AjQ0UkllDh7vKka22PeUk6H7u15WMPERcPooqTnsq3W4%3D; is_staff_user=false; sid_ucp_v1=1.0.0-KDY0ZWU2ZGQ5ODM3NzZiM2Y3YzdjMzNlY2FlMjEyMjg1NWE2ZjIxN2UKIQjNy7D6xfT1BBCgluDEBhjvMSAMMNjrl_IFOAJA7wdIBBoCbGYiIDAyYTIzYzQyZmJhYzgyMzUwODYzZGYxOGVlYjdmZGJl; ssid_ucp_v1=1.0.0-KDY0ZWU2ZGQ5ODM3NzZiM2Y3YzdjMzNlY2FlMjEyMjg1NWE2ZjIxN2UKIQjNy7D6xfT1BBCgluDEBhjvMSAMMNjrl_IFOAJA7wdIBBoCbGYiIDAyYTIzYzQyZmJhYzgyMzUwODYzZGYxOGVlYjdmZGJl; login_time=1754794785003; _bd_ticket_crypt_cookie=8fff76a002244c58e22a2c5e5793eb8d; __security_mc_1_s_sdk_sign_data_key_web_protect=ff8a008c-45db-b274; publish_badge_show_info=%220%2C0%2C0%2C1755090748472%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.167%7D; EnhanceDownloadGuide=%220_0_1_1755313143_0_0%22; __druidClientInfo=JTdCJTIyY2xpZW50V2lkdGglMjIlM0EzMDQlMkMlMjJjbGllbnRIZWlnaHQlMjIlM0E2NTElMkMlMjJ3aWR0aCUyMiUzQTMwNCUyQyUyMmhlaWdodCUyMiUzQTY1MSUyQyUyMmRldmljZVBpeGVsUmF0aW8lMjIlM0ExJTJDJTIydXNlckFnZW50JTIyJTNBJTIyTW96aWxsYSUyRjUuMCUyMChXaW5kb3dzJTIwTlQlMjAxMC4wJTNCJTIwV2luNjQlM0IlMjB4NjQpJTIwQXBwbGVXZWJLaXQlMkY1MzcuMzYlMjAoS0hUTUwlMkMlMjBsaWtlJTIwR2Vja28pJTIwQ2hyb21lJTJGMTM5LjAuMC4wJTIwU2FmYXJpJTJGNTM3LjM2JTIyJTdE; __live_version__=%221.1.3.7384%22; live_can_add_dy_2_desktop=%221%22; strategyABtestKey=%221755391719.166%22; download_guide=%223%2F20250807%2F1%22; WallpaperGuide=%7B%22showTime%22%3A1755175539720%2C%22closeTime%22%3A0%2C%22showCount%22%3A3%2C%22cursor1%22%3A73%2C%22cursor2%22%3A22%2C%22hoverTime%22%3A1754401932686%7D; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAHtvwPBwaUaA1k0mgpOId5oSi2N8sl6XtWdeHDKucwZS1oMqVGlfse5w42nkvVbTZ%2F1755446400000%2F0%2F0%2F1755410537733%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A1%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A6%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A1.35%2C%5C%22effective_type%5C%22%3A%5C%223g%5C%22%2C%5C%22round_trip_time%5C%22%3A350%7D%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAHtvwPBwaUaA1k0mgpOId5oSi2N8sl6XtWdeHDKucwZS1oMqVGlfse5w42nkvVbTZ%2F1755446400000%2F0%2F1755418348630%2F0%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCTGpBOEFxa210MUpCR2xBSS9scnM4cXc5MVlRbmczbkFDNmpBRnp5YURwRk0ySGJtbG5pd0h3cHNjVUE3VHZ0ZC8xSmMrVkU4RVlEdVNkeU1yNW43UkE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; home_can_add_dy_2_desktop=%221%22; biz_trace_id=ca7ad1a7; ttwid=1%7CsPz3sM0YQUk-pqINPee_1HjLvjPmeZnm4efh-Zu6unI%7C1755418357%7C592c5e731509415ad9c9b4b2cb177d2332224eaa1169d5eea3122bdd663f1e87; odin_tt=f705eb4969bfa1cc00e3cf932483205a4b5e86a13087654bf8b9f404d3c037aab098e6c633ba725269f504b5ce7e5c8b0d1ce91002291f0408524ef7a6336bad; IsDouyinActive=true; sdk_source_info=7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e5927666d776a686028607d71606b766c6a6b3f2a2a6f6975666b6a6a6d66756362756764696d696262616d6f6a66626b696264636b2a6476766071762a68646c6b28726a7769612b7176283160613c3c3666322b6f76592758272927666a6b766a69605a696c6061273f27636469766027292762696c64695a7364776c6467696076273f275e582729277672715a646971273f2763646976602729277f6b5a666475273f2763646976602729276d6a6e5a6b6f6c273f2763646976602729276c6b6f5a7f6367273f27636469766027292771273f2733333230353c37373130303234272927676c715a75776a716a666a69273f2763646976602778; bit_env=eZh4WVAYUWPqzFM0m5mbmouNC2R93rfroDexPWW2FuBWZKk2ZeWxnJCZ1rBh0Qp3Jxu3ybiQfJi7U_BFvxNBpyzAVrJ5SPXu_OGoesjuc28H5OMbd6SbwB9GONeN1nwmF_aAr1nMy5CtNlmJrZlmuPkwXM_20HLpjNUWIffeSheHHDVGwf3G7Lskv932bmY2p--cRyIEk9g-nUsKU8q6dKsXekkvAaz6pQmRe0-M7OUOuAiY9OAwJFyV1G9TtH7Fj6sBvGGwq5GWpiCBG5aj9qoNDbq-n1DP7ihl-bq1CNIsy6kNqRGvccstUZOgvn5XNyk6mtBNfahWBfOpgOoGu6IzvwWiVrvPY3yg3Rh0WUyxciPhMQydTDqEUTJuUWjRKmfREjib52SWbaCRsgDd0knvDolFVpPDfd5NchEel3gSQKZYavas-loo-D6H0CkfnSXcyCONLrYJGrCklZx7mDnfv40Hc8PU8s-pJFjkpLw71w-LUR2N7L0F0YFLph6L; gulu_source_res=eyJwX2luIjoiZTBiNzA1NzgwZDUxMGU2MDhlNzEyM2YxMDgyMGE2YjEzOWU3OGMwMzkwY2NlMDQ2MDZlZWNmZjI5ZTBkNTJhYiJ9; passport_auth_mix_state=0kf6ckbpry36q9pzipufb58zm1ud4erw13b18fgp1ygg4ao1"
}


url = "https://www-hj.douyin.com/aweme/v1/web/comment/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id=7538929120571575612&cursor=10&count=10&item_type=0&insert_ids=&whale_cut_token=&cut_version=1&rcFT=&update_version_code=170400&pc_client_type=1&pc_libra_divert=Windows&support_h265=1&support_dash=1&cpu_core_num=6&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=139.0.0.0&browser_online=true&engine_name=Blink&engine_version=139.0.0.0&os_name=Windows&os_version=10&device_memory=8&platform=PC&downlink=1.35&effective_type=3g&round_trip_time=350&webid=7535069073778312738&uifid=1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee64740d2e774158a5ff949275fa8076e5fe433481a7d836cd9c619a2e1771a732aff0a4915821b3aa427925dd575eea7052e002694eef3ee6632bb357ac752f09e3575b0014027e3698bd41ce9e9a8278b00cfda4a956646bb886b9b325c146163157945297c907374d1a3b098577e9268e6d4ff60b258b63ec19c51087aad2b0ed0e4&msToken=wo6Yxn16ak_TLpev6vStonfvoYWchMsp_A9mfIZ1Y7pcHo608hFBFQeGn0RazGeXm5lVg3zBOAOkFVloYehd4FMWKLWQFaUdvs1tx_xpAyTrfw7norw5uQu3tLrnco0vzNW6jj0MHQ1SvMLIZ9Oi9ahNzLATT7GB1GwwrCh3Asfe0g%3D%3D&a_bogus=OfU5ht6JOZ8jKd%2FGYKsc71Il9Lj%2FNs8yQeiQWwBPyNPdcwtTjRPlirSCbxz7EhmJ3RBwkFMH4nPAadxbT0XkZHckqmpvSgsfv0VIn6vogqiRTzkQLNjmCzuzKwMx0c4ql55Ui1h6gUtqgfVAwrdE%2FBlJt%2FKFQ58BPpxjkMYcT9sg106Ag3c3Ppthxwiq4f%3D%3D&verifyFp=verify_mdflalvf_lsqPlNtb_3MKY_42Dk_9lO0_xnb1vqXHICKv&fp=verify_mdflalvf_lsqPlNtb_3MKY_42Dk_9lO0_xnb1vqXHICKv"
response = requests.get(url, headers=headers, timeout=10)

# 检查状态码
if response.status_code == 200:
    data = response.text
    print("请求成功！")
    print("返回数据示例：")
    print(data)
#     print(data.get("comments", [])[:2])  # 打印前两条评论
# else:
#     print(f"请求失败，状态码：{response.status_code}")
#     print(response.text)

