# -*- coding:utf-8 -*-
# playwright codegen --browser=ff --viewport-size="1920, 1080" --save-storage=auth.json -o script.py https://www.douyin.com
from playwright.sync_api import sync_playwright
from loguru import logger
import yaml
import os
import platform

# 自定义格式
format = "{time:YYYY-MM-DD HH:mm:ss} | {level} | {message} | {file}:{line}"
logger.add("logs/cookies.log", format=format, level="INFO")

# 你想提取的 cookie 名称列表
TARGET_COOKIES = [
    "msToken",
    "ttwid",
    "odin_tt",
    "passport_csrf_token",
    "sid_guard",
    # 可以继续添加其他需要的 cookie
]


def load_yaml(path: str) -> dict:
    """安全加载 YAML 配置"""
    if not os.path.exists(path):
        logger.warning(f"{path} 文件不存在，将新建一个。")
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def save_yaml(path: str, data: dict) -> None:
    """安全写入 YAML 配置"""
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        yaml.dump(
            data,
            f,
            allow_unicode=True,
            indent=2,
            sort_keys=False,
            default_flow_style=False,
        )
    os.replace(tmp_path, path)  # 原子替换，避免写坏文件
    logger.info(f"已更新配置文件: {path}")


def extract_cookies(phone: str, config_path: str = "config.yml"):
    with sync_playwright() as p:
        system = platform.system().lower()
        headless = system == "linux"

        logger.info("启动浏览器...")

        browser = p.firefox.launch(headless=headless)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        try:
            page.goto("https://www.douyin.com/?recommend=1")
            # page.get_by_role("textbox", name="请输入手机号").click()
            page.get_by_role("textbox", name="请输入手机号").fill(phone)
            page.get_by_text("获取验证码").click()

            code = input("输入短信验证码>").strip()
            # page.get_by_role("textbox", name="请输入验证码").click()
            page.get_by_role("textbox", name="请输入验证码").fill(code)
            page.get_by_text("登录/注册").click()

            # 获取所有 Cookies
            page.wait_for_timeout(9000)
            all_cookies = context.cookies()
            cookie_dict = {cookie["name"]: cookie["value"] for cookie in all_cookies}

            # 提取目标 Cookies
            extracted = {}
            for name in TARGET_COOKIES:
                if name in cookie_dict:
                    extracted[name] = cookie_dict[name]
                else:
                    logger.info(f"未找到 Cookie: {name}")

            # 更新 config.yaml
            config = load_yaml(config_path)
            config["cookies"] = extracted
            save_yaml(config_path, config)

            # 保存 Playwright 登录状态
            context.storage_state(path="auth.json")
            logger.info("Cookies 已提取并保存到 config.yaml 与 auth.json")
        except Exception as e:
            logger.exception(e)
        finally:
            browser.close()
            logger.info("浏览器已关闭")


if __name__ == "__main__":
    extract_cookies(phone="187 0194 3997")
