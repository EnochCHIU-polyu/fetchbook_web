import os

folder = "page"
files = sorted([f for f in os.listdir(folder) if f.endswith('.txt')])
content = ""
for fname in files:
    with open(os.path.join(folder, fname), encoding="utf-8") as f:
        content += f.read() + "\n\n"

html = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <title>小說合併展示</title>
    <style>
        body {{ font-family: "Noto Sans TC", "微軟正黑體", sans-serif; white-space: pre-wrap; }}
    </style>
</head>
<body>
    <h1>小說內容</h1>
    <div>{content.replace('\n', '<br>')}</div>
</body>
</html>
"""

with open("web.html", "w", encoding="utf-8") as f:
    f.write(html)

print("已產生 web.html")