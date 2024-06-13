import google.generativeai as genai

# "GEMINI_API_KEY"：輸入 Gemini API Key
genai.configure(api_key="GEMINI_API_KEY")

# 選擇模型與相關模型設定
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 0,
  "max_output_tokens": 2048,
  "response_mime_type": "text/plain",
}

# 安全設定
safety_settings = [{
  "category": "HARM_CATEGORY_HARASSMENT",
  "threshold": "BLOCK_NONE"
}, {
  "category": "HARM_CATEGORY_HATE_SPEECH",
  "threshold": "BLOCK_NONE"
}, {
  "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
  "threshold": "BLOCK_NONE"
}, {
  "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
  "threshold": "BLOCK_NONE"
}]

# model：語言模型設定
model = genai.GenerativeModel(
  model_name="gemini-1.0-pro",
  # model_name="gemini-1.5-flash",
  # model_name="gemini-1.5-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

# chat_session：對話紀錄
chat_session = model.start_chat(
  history=[
  ]
)

# INSERT_INPUT_HERE：輸入給 Gemini 的文字
response = chat_session.send_message("INSERT_INPUT_HERE")
# response = chat_session.send_message("你好啊～")

# response.text：印出 Gemini 輸出結果文字
print(response.text)

