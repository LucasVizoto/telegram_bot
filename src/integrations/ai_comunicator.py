import google.generativeai as genai


from config.env import env_variables

api_key = env_variables['GOOGLE_API_KEY']
google_model = env_variables['GOOGLE_MODEL']

genai.configure(api_key=api_key)

# Escolha o modelo
model = genai.GenerativeModel(google_model)
