import asyncio
import re
from playwright.async_api import async_playwright

# 正则：只允许昵称是纯英文（大写或小写字母），不含中文、数字、符号
english_name_pattern = re.compile(r'^[A-Za-z]+$')

async def check_uid(suffix):
    result = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        for prefix in range(500, 600):
            uid = f"{prefix}{suffix:04d}"
            url = f"https://space.bilibili.com/{uid}"
            try:
                await page.goto(url, timeout=10000)
                await page.wait_for_timeout(1000)  # 等待 JS 渲染

                html = await page.content()

                # 判断是否为等级 0 用户
                if "sic-BDC_svg-user_level_0" not in html:
                    print(f"✘ {uid}：非零级")
                    continue

                # 提取昵称
                match = re.search(r'<div[^>]*class="nickname"[^>]*>(.*?)</div>', html)
                if not match:
                    print(f"✘ {uid}：找不到昵称")
                    continue

                nickname = match.group(1).strip()

                # 判断昵称是否纯英文字母
                if not english_name_pattern.fullmatch(nickname):
                    print(f"✘ {uid}：昵称不合规：{nickname}")
                    continue

                # 符合条件，保存 UID
                print(f"✔ {uid}：昵称 {nickname}")
                result.append(uid)
                result.append(nickname)

            except Exception as e:
                print(f"⚠ {uid} 错误：{e}")

        await browser.close()

    # 写入 UID 到文件
    with open("uid.txt", "w", encoding="utf-8") as f:
        for uid in result:
            f.write(uid + "\n" + nickname)

if __name__ == "__main__":
    suffix_input = input("请输入四位数后缀（如1234）：")
    if not suffix_input.isdigit() or len(suffix_input) != 4:
        print("输入有误，必须是4位数字！")
    else:
        asyncio.run(check_uid(int(suffix_input)))
