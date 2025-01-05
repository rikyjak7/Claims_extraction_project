import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def test_gpt_neox_simple_question():
    """
    Testa GPT-NeoX-20B su un dispositivo configurabile (GPU, MPS o CPU).
    """
    model_name = "EleutherAI/gpt-neox-20b"
    print("Caricamento del tokenizer...")

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Identifica il dispositivo
    if torch.cuda.is_available():
        device = "cuda"  # GPU NVIDIA
        print("CUDA disponibile. Uso GPU.")
    elif torch.backends.mps.is_available():
        device = "mps"  # GPU Apple
        print("MPS disponibile. Uso GPU Apple.")
    else:
        device = "cpu"  # Fallback su CPU
        print("Nessuna GPU disponibile. Uso CPU.")
    
    print(f"Caricamento del modello su: {device}...")
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map=device)

    # Prompt di esempio
    input_text = "What is a dog?"

    # Tokenizza l'input
    inputs = tokenizer(input_text, return_tensors="pt", max_length=2048, truncation=True)

    # Porta i tensori sullo stesso dispositivo del modello
    inputs = {k: v.to(device) for k, v in inputs.items()}

    # Genera la risposta
    print("Generazione della risposta...")
    outputs = model.generate(
        inputs["input_ids"],
        max_length=50,
        num_beams=2,
        early_stopping=True
    )

    # Decodifica la risposta
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("Risultato generato:")
    print(generated_text)

test_gpt_neox_simple_question()
