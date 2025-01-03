import requests
import json

def generate_content_with_gemini(api_key, prompt):
   
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=" + api_key
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Lancia un eccezione per 'bad status codes' (4xx o 5xx)
        response_json = response.json()

        # Estrae il testo generato
        if "candidates" in response_json and response_json["candidates"]:
            generated_text = response_json["candidates"][0]["content"]["parts"][0]["text"]
            return generated_text
        else:
           print("Error: No generated text found in the response.")
           return None

    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return None