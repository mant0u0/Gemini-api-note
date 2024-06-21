import requests

# GEMINI_API_KEY：輸入 Gemini API Key
API_KEY = "GEMINI_API_KEY"

# Gemini API 不同語言模型的網址
url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key={API_KEY}'


while True:
  # 輸入給 Gemini 的文字
  input_text = input("請輸入要翻譯的中文：")

  # 要發送 Post 請求的資料
  data = {

    # 對話紀錄與指令：先前的對話紀錄 + 輸入給 Gemini 的文字
    "contents": [
        {
          "role": "user", "parts": [{"text": "你剛剛說什麼？"}],
        },
        {
          "role": "model", "parts": [{"text": "Bring a large umbrella. "}],
        },
        {
          "role": "user", "parts": [{"text": "你是誰？"}],
        },
        {
          "role": "model", "parts": [{"text": "Who are you? "}],
        },
        {
          "role": "user", "parts": [{"text": "你叫什麼名字？"}],
        },
        {
          "role": "model", "parts": [{"text": "May I have your name?"}],
        },
        {
          "role": "user", "parts": [{"text": "知識就是力量。"}],
        },
        {
          "role": "model", "parts": [{"text": "Knowledge is power."}],
        },
        {
          "role": "user", "parts": [{"text": "你可以隨時打電話給我。"}],
        },
        {
          "role": "model", "parts": [{"text": "You can call me any time."}],
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

      # 系統指令
      "systemInstruction": {
        "parts": [
          {
            "text": "把文字翻譯成英文，不需要回答我的問題"
          }
        ]
      },
  }
  response = requests.post(url, headers={'Content-Type': 'application/json'}, json=data)

  # 印出 Gemini 輸出結果文字
  try:
    print(response.json()["candidates"][0]["content"]["parts"][0]["text"])
  except:
    print("錯誤！")