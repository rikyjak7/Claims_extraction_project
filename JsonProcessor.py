import os
import json
from T5_Model import extract_claims_with_flan_t5


def extract_table_data(json_file): 

    for table_id, table_details in json_file.items():
        #"references": table_details.get("references", []),
        claims = extract_claims_with_flan_t5(table_details.get("table", None),table_details.get("caption", None),"")
        



def process_directory():

    directory = "C:/Users/rikyj/Documents/university/Magistrale/Ingegneria_dei_dati/HW4/10_samples/arxiv_10_json"
    # Controlla che il percorso sia una cartella
    if not os.path.isdir(directory):
        print(f"{directory} non è una cartella valida!")
        return
    
    # Itera sui file nella cartella
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        
        # Verifica che sia un file JSON
        if file_name.endswith('.json') and os.path.isfile(file_path):
            try:
                # Apri il file JSON
                with open(file_path, 'r', encoding='utf-8') as file:
                    json_file = json.load(file)  # Leggi il contenuto del file
                    extract_table_data(json_file)
            except Exception as e:
                print(f"Errore nell'elaborazione di {file_name}: {e}")