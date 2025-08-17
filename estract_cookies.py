# -*- coding:utf-8 -*-
# playwright codegen --browser=ff --viewport-size="1920, 1080" --save-storage=auth.json -o script.py https://www.douyin.com
from playwright.sync_api import sync_playwright
from loguru import logger
import yaml

# 自定义格式
format = "{time:YYYY-MM-DD HH:mm:ss} | {level} | {message} | {file}:{line}"
logger.add("logs/cookie.log", format=format, level="INFO")

# 你想提取的 cookie 名称列表
TARGET_COOKIES = [
    "msToken",
    "ttwid",
    "odin_tt",
    "passport_csrf_token",
    "sid_guard",
    # 可以继续添加其他需要的 cookie
]


def extract_cookies():
    with sync_playwright() as p:
        logger.info("启动浏览器...")
        browser = p.firefox.launch(headless=False)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        try:
            page.goto("https://www.douyin.com/?recommend=1", wait_until="networkidle")
            page.get_by_role("textbox", name="请输入手机号").click()
            page.get_by_role("textbox", name="请输入手机号").fill("187 0194 3997")
            page.get_by_text("获取验证码").click()

            code = input("输入验证码后，请按回车键继续...")
            page.get_by_role("textbox", name="请输入验证码").click()
            page.get_by_role("textbox", name="请输入验证码").fill(code)
            page.get_by_text("登录/注册").click()

            # 获取所有 Cookies
            page.wait_for_timeout(10000)
            all_cookies = context.cookies()
            cookie_dict = {cookie["name"]: cookie["value"] for cookie in all_cookies}

            # 提取目标 Cookies
            extracted = {}
            for name in TARGET_COOKIES:
                if name in cookie_dict:
                    extracted[name] = cookie_dict[name]
                else:
                    logger.info(f"未找到 Cookie: {name}")

            # 保存到 YAML 配置文件
            config = {"cookies": extracted}
            with open("cookies.yaml", "w", encoding="utf-8") as f:
                yaml.dump(config, f, allow_unicode=True, indent=2, sort_keys=False)

            logger.info("Cookies 已成功提取并保存到 cookies.yaml")
            context.storage_state(path="auth.json")
        except Exception as e:
            logger.exception(e)

        browser.close()


if __name__ == "__main__":
    extract_cookies()
