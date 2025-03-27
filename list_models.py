import google.generativeai as genai

# ✅ Replace this with your actual Gemini API key
GEMINI_API_KEY = "AIzaSyDwPHN1Gb0Qph2eBEynNkVwFX29mh6wzFA"

# Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Fetch and print available models
models = genai.list_models()
print("Available Gemini Models:\n")
for model in models:
    print(f"🔹 Model ID: {model.name}")
    print(f"   ➡️ Description: {model.description}")
    print(f"   🚀 Input Token Limit: {model.input_token_limit}")
    print(f"   📝 Output Token Limit: {model.output_token_limit}")
    print("-" * 50)
