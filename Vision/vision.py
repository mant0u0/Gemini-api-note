import json
import requests
import base64

# 讀取圖片檔案，並轉換成 Base64 編碼的字串
with open("image_test.jpg", "rb") as image_file:
    image_base64_string = base64.b64encode(image_file.read()).decode('utf-8')
    # print(image_base64_string)

# GEMINI_API_KEY：輸入 Gemini API Key
API_KEY = "GEMINI_API_KEY"

# Gemini API 網址
url = f'https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}'


# 要發送 Post 請求的資料
data = {
    "contents": [
        {
            "parts": [
                {"text": "圖片中的是什麼？"},
                {
                    "inline_data": {
                        "mime_type": "image/jpeg",
                        "data": image_base64_string
                    }
                }
            ]
        },
    ]
}


response = requests.post(url, headers={'Content-Type': 'application/json'}, json=data)


# 印出 Gemini 輸出結果文字
# print(response.json())
print(response.json()["candidates"][0]["content"]["parts"][0]["text"])