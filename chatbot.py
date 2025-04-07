import requests
API_KEY = "AIzaSyC1PaZr12k8UsBUL05t_nD2iEIXdqpyO74"
URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"

def get_gemini_response(prompt):
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"maxOutputTokens": 50}
    }
    response = requests.post(f"{URL}?key={API_KEY}", json=data, headers=headers)
    if response.status_code == 200:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return "Error: Couldn’t get a response from Gemini."

print("Welcome to the Gemini Chatbot! Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    reply = get_gemini_response(user_input)
    print("Bot:", reply)