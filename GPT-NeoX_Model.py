from transformers import AutoTokenizer, AutoModelForCausalLM

def extract_claims_with_gpt_neox(table_html, caption, references):
    """
    Estrae i claims da una tabella HTML usando il modello GPT-NeoX-20B.

    Args:
        table_html (str): HTML della tabella.
        caption (str): Caption della tabella.
        references (str): Testo di riferimento associato alla tabella.

    Returns:
        list: Lista di claims estratti nel formato desiderato.
    """
    # Carica il modello GPT-NeoX-20B e il tokenizer
    model_name = "EleutherAI/gpt-neox-20b"  # Modello GPT-NeoX-20B
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Prepara il prompt con esempi espliciti
    input_text = (
        f"Extract claims from the table in this format: "
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
        f"Table HTML: {table_html} \nCaption: {caption} \nReferences: {references}"
    )

    # Tokenizza l'input
    inputs = tokenizer(input_text, return_tensors="pt", max_length=2048, truncation=True)

    # Genera il risultato (usa num_beams per migliore qualità, ma usa un valore moderato per GPT-NeoX)
    outputs = model.generate(
        inputs.input_ids,
        max_length=512,
        num_beams=5,
        early_stopping=True
    )

    # Decodifica i risultati
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Processa il testo generato per convertirlo in una lista di claims
    claims = [claim.strip() for claim in generated_text.split("\n") if claim.strip()]

    return claims


# Esempio di utilizzo
table_html = """<table>
<tr><th>Model</th><th>Difficulty</th><th>Execution Match</th></tr>
<tr><td>ChatGPT-3.5-turbo</td><td>1</td><td>0.760</td></tr>
<tr><td>ChatGPT-3.5-turbo</td><td>2</td><td>0.799</td></tr>
<tr><td>Starcoder</td><td>1</td><td>0.584</td></tr>
</table>"""

caption = "Execution Match for various LLMs on Spider dev dataset"
references = "The metric Execution Match measures the correctness of SQL query outputs."

# Esegue la funzione e stampa i claims estratti
claims = extract_claims_with_gpt_neox(table_html, caption, references)
for claim in claims:
    print(claim)
