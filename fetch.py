import requests
from bs4 import BeautifulSoup
import os
import shutil

base_url = "https://ixdzs.tw/read/393055/p{}.html"
headers = {
    "User-Agent": "Mozilla/5.0"
}

# 建立並清空 page 資料夾
folder = "page"
if os.path.exists(folder):
    shutil.rmtree(folder)
os.makedirs(folder)

start_num = int(input("請輸入起始頁碼（如1272）："))
count = int(input("請輸入要抓取的頁數（如5）："))

for num in range(start_num, start_num + count):
    url = base_url.format(num)
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, "html.parser")
    section = soup.find("section")
    if section:
        ps = section.find_all("p")
        lines = []
        for p in ps:
            # 過濾掉 class="abg" 的廣告段落
            if p.get("class") == ["abg"]:
                continue
            text = p.get_text(strip=True)
            if text:
                lines.append(text)
        content = "\n".join(lines)
        with open(os.path.join(folder, f"page_{num}.txt"), "w", encoding="utf-8") as f:
            f.write(content)
        print(f"已儲存至 {folder}/page_{num}.txt")
    else:
        print(f"找不到 <section> 內容：{url}")