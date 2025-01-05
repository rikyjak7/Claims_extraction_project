import requests

def query_huggingface_api(prompt):
    # URL dell'API di inferenza
    API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
    
    # Token Hugging Face
    headers = {
        "Authorization": "Bearer token"
    }
    
    # Payload
    payload = {"inputs": prompt}
    
    # Richiesta API
    response = requests.post(API_URL, headers=headers, json=payload)
    
    # Risultato
    if response.status_code == 200:
        return response.json()[0]['generated_text']
    else:
        print(f"Errore: {response.status_code}, {response.text}")
        return None


table_html = """<table>
<tr><th>Model</th><th>Difficulty</th><th>Execution Match</th></tr>
<tr><td>ChatGPT-3.5-turbo</td><td>1</td><td>0.760</td></tr>
<tr><td>ChatGPT-3.5-turbo</td><td>2</td><td>0.799</td></tr>
<tr><td>Starcoder</td><td>1</td><td>0.584</td></tr>
</table>"""
caption = "Execution Match for various LLMs on Spider dev dataset"
references = "The metric Execution Match measures the correctness of SQL query outputs."

# Testa la funzione
prompt =(f"Extract claims from the table in this format: "
        f"{{{{|Specification1, Value1|, |Specification2, Value2|, ...}}, Measure, Outcome|}}. "
        f"Example:\n"
        f"Input: <table><tr><th>Model</th><th>Difficulty</th><th>Execution Match</th></tr>"
        f"<tr><td>ChatGPT-3.5-turbo</td><td>1</td><td>0.760</td></tr>"
        f"<tr><td>ChatGPT-3.5-turbo</td><td>2</td><td>0.799</td></tr>"
        f"<tr><td>Starcoder</td><td>1</td><td>0.584</td></tr>"
        f"</table>, Caption: Execution Match for various LLMs on Spider dev dataset, "
        f"References: The metric Execution Match measures the correctness of SQL query outputs.\n"
        f"Output: {{|Model, ChatGPT-3.5-turbo|, |Difficulty Level, 1|, |Execution Match, 0.760|}}.\n"
        f"Now extract claims for the following input:\n"
        f"Table HTML: {table_html} \nCaption: {caption} \nReferences: {references}")
response = query_huggingface_api(prompt)
print("Risposta:", response)
