import requests
from datetime import datetime


# GEMINI_API_KEY：輸入 Gemini API Key
API_KEY = "GEMINI_API_KEY"

# Gemini API 不同語言模型的網址
url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key={API_KEY}'

# 現在時間
now = str(datetime.now().strftime("%Y-%m-%d %A %H:%M:%S"))
print(now)

while True:
  # 輸入給 Gemini 的文字
  input_text = input("請輸入文字：")
  input_text = now +","+ input_text

  # 要發送 Post 請求的資料
  data = {

    # 對話紀錄與指令：先前的對話紀錄 + 輸入給 Gemini 的文字
    "contents": [
        {
          "role": "user", "parts": [{"text": "2024-06-20 Thursday 15:17:28, 明天下我兩點要去看電影。"}],
        },
        {
          "role": "model", "parts": [{"text": "行程：看電影\n時間：2024-06-21 14:00\n地點：未知\n"}],
        },
        {
          "role": "user", "parts": [{"text": "2024-06-20 Thursday 15:17:28, 星期六我要去上課"}],
        },
        {
          "role": "model", "parts": [{"text": "行程：上課\n時間：2024-06-22 整天\n地點：未知\n"}],
        },
        {
          "role": "user", "parts": [{"text": input_text}],
        },
    ],

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

  }
  response = requests.post(url, headers={'Content-Type': 'application/json'}, json=data)

  # 印出 Gemini 輸出結果文字
  try:
    print(response.json()["candidates"][0]["content"]["parts"][0]["text"])
  except:
    print("錯誤！")