import requests
import random


# GEMINI_API_KEY：輸入 Gemini API Key
API_KEY = "GEMINI_API_KEY"

# Gemini API 不同語言模型的網址
url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key={API_KEY}'

list = ["大吉","中吉","小吉","吉","末吉","凶","大凶"]

while True:
  # 輸入給 Gemini 的文字
  input_text = input("請輸入文字：")
  # 隨機選擇一個運勢
  result = random.choice(list)
  input_text = result +","+ input_text

  # 要發送 Post 請求的資料
  data = {

    # 對話紀錄與指令：先前的對話紀錄 + 輸入給 Gemini 的文字
    "contents": [
        {
          "role": "user", "parts": [{"text": "大吉：我的戀愛運勢"}],
        },
        {
          "role": "model", "parts": [{"text": "你的戀愛運勢極佳，各方面均將獲得成功和幸福，可能遇到命中注定的愛情，感情更會更穩固，享受這段美好時光！"}],
        },

        {
          "role": "user", "parts": [{"text": "凶：投資股市"}],
        },
        {
          "role": "model", "parts": [{"text": "投資股市方面可能會遇到挑戰和波動，建議謹慎行事，避免冒險，保持穩健的態度，做好風險控制和資金管理。"}],
        },

        {
          "role": "user", "parts": [{"text": "大凶：明天的考試"}],
        },
        {
          "role": "model", "parts": [{"text": "明天的考試可能會遇到困難和挑戰，建議你積極準備，保持冷靜，專注於考試內容，盡力而為。"}],
        },

        {
          "role": "user", "parts": [{"text": "末吉：下周的比賽"}],
        },
        {
          "role": "model", "parts": [{"text": "下周的比賽可能會有些許波折，但也會有一些幸運之處。請確保充分準備，保持冷靜和專注，並尋求幫助或建議以克服任何挑戰。"}],
        },

        {
          "role": "user", "parts": [{"text": "吉：大樂透"}],
        },
        {
          "role": "model", "parts": [{"text": "吉兆預示著一些幸運和機會，儘管中獎並非必然，但你可能會遇到一些好運氣。但仍然要理智地玩，不要投入過多金錢。"}],
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
    print("運勢："+result)
    print(response.json()["candidates"][0]["content"]["parts"][0]["text"])
  except:
    print("錯誤！")