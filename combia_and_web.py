import os
from flask import Flask, render_template_string

app = Flask(__name__)

def combine_txt_files(folder):
    files = sorted([f for f in os.listdir(folder) if f.endswith('.txt')])
    content = ""
    for fname in files:
        with open(os.path.join(folder, fname), encoding="utf-8") as f:
            content += f.read() + "\n\n"
    return content

@app.route("/")
def index():
    content = combine_txt_files("page")
    # 用簡單的 HTML 顯示內容
    return render_template_string("""
    <html>
    <head>
        <meta charset="utf-8">
        <title>小說合併展示</title>
        <style>
            body { font-family: "Noto Sans TC", "微軟正黑體", sans-serif; white-space: pre-wrap; }
        </style>
    </head>
    <body>
        <h1>小說內容</h1>
        <div>{{ content }}</div>
    </body>
    </html>
    """, content=content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)