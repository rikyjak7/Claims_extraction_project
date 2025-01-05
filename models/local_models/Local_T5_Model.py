from transformers import T5Tokenizer, T5ForConditionalGeneration

def extract_claims_with_flan_t5(table_html, caption, references):
    """
    Estrae i claims da una tabella HTML usando il modello Flan-T5.

    Args:
        table_html (str): HTML della tabella.
        caption (str): Caption della tabella.
        references (str): Testo di riferimento associato alla tabella.

    Returns:
        list: Lista di claims estratti nel formato desiderato.
    """
    # Carica il modello Flan-T5 e il tokenizer
    model_name = "google/flan-t5-large"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    # Prepara il prompt in modo più diretto, limitando la struttura.
    input_text = (
        "what is a dog?. Talk a lot"
    )

    # Tokenizza l'input
    inputs = tokenizer(input_text, return_tensors="pt")

    # Genera il risultato
    outputs = model.generate(
        inputs.input_ids,
        max_length=512,
        num_beams=5,
        early_stopping=False
    )

    # Decodifica il risultato
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Il testo risultante dovrebbe contenere una lista di claims che può essere post-processata.
    claims = [claim.strip() for claim in generated_text.split("|") if claim.strip()]

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
claims = extract_claims_with_flan_t5(table_html, caption, references)
for claim in claims:
    print(claim)
