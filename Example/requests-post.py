import requests

# GEMINI_API_KEY：輸入 Gemini API Key
API_KEY = "GEMINI_API_KEY"

# Gemini API 不同語言模型的網址
# url = f'https://generativelanguage.googleapis.com/v1/models/gemini-1.0-pro:generateContent?key={API_KEY}'
# url = f'https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}'
# url = f'https://generativelanguage.googleapis.com/v1/models/gemini-1.5-pro:generateContent?key={API_KEY}'
# url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}'
url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key={API_KEY}'


# 要發送 Post 請求的資料
data = {

    # 一般指令：輸入給 Gemini 的文字
    "contents": [
        {
            "parts": [{"text": "你好，我是饅頭～"}]
        }
    ],

    # 對話紀錄與指令：先前的對話紀錄 + 輸入給 Gemini 的文字
    # "contents": [
    #     {
    #       "role": "user", "parts": [{"text": "你好，我是饅頭。"}],
    #     },
    #     {
    #       "role": "model", "parts": [{"text": "日文：こんにちは、饅頭です。"}],
    #     },
    #     {
    #       "role": "user", "parts": [{"text": "下午你在做什麼？"}],
    #     },
    #     {
    #       "role": "model", "parts": [{"text": "日文：午後は何をしていますか？ "}],
    #     },
    #     {
    #       "role": "user", "parts": [{"text": "今天的晚餐吃什麼？"}],
    #     },
    # ],

    # 安全設定
    "safetySettings": [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE"
        }
    ],

    # 模型的相關設定
    "generationConfig": {
        "temperature": 0.9,
        "maxOutputTokens": 2048,
        "topP": 1,
        "topK": 0
    },

    # 系統指令：只支援 v1beta gemini-1.5-flash、gemini-1.5-pro 兩個模型，gemini-1.0-pro 不支援。
    "systemInstruction": {
      "parts": [
        {
          "text": "翻譯成日文"
        }
      ]
    },
}
response = requests.post(url, headers={'Content-Type': 'application/json'}, json=data)


# 印出 Gemini 輸出結果文字
# print(response.json())
print(response.json()["candidates"][0]["content"]["parts"][0]["text"])