import os
import json
import time
import re
import API_key
import Extraction_methods
from Table_Dictionary import table_types
from Cloud_Gemini import generate_content_with_gemini
from LLM_Extraction_Prompt_Update import prompt_function
from colorama import Fore, Back, Style, init

def parse_claims_to_json(input_string, table_id, paper_id):

    # Separare i claims in base alle righe
    claims = [claim.strip() for claim in input_string.split('\n') if claim.strip()]

    # Costruzione del nome del file JSON basato su paper_id e table_id
    file_name = f"{paper_id}_{table_id}_claims.json"

    output = []  # Lista per contenere i claims

    for i, claim in enumerate(claims):

        # Pulizia del claim da caratteri indesiderati
        claim = claim.strip()

        # Regex per identificare il blocco delle specifications (nuovo formato con | prima della graffa)
        spec_match = re.match(r"\|\{(.*?)\|\},\s*(.*)", claim)

        if not spec_match:
            print(f"Errore: il claim {i} non ha un formato valido per le specifications.")
            continue  # Salta il claim non valido

        specifications_part = spec_match.group(1).strip()
        remaining_part = spec_match.group(2).strip()

        # Parsing delle specifications
        specifications = {}
        valid_idx = 0  # Contatore per mantenere l'enumerazione sequenziale
        spec_items = [spec.strip() for spec in specifications_part.split('|') if spec.strip() and ',' in spec]
        for spec in spec_items:
            key, value = [s.strip() for s in spec.split(',', 1)]
            if key and value:  # Aggiungere solo specifiche con nome e valore non vuoti
                specifications[str(valid_idx)] = {"name": key, "value": value}
                valid_idx += 1  # Incrementare solo per specifiche valide

        # Separare Measure e Outcome dal resto del claim
        remaining_parts = [part.strip() for part in remaining_part.split(',')]
        measure = remaining_parts[0] if len(remaining_parts) > 0 else None
        outcome = remaining_parts[1].rstrip('|') if len(remaining_parts) > 1 else None

        # Creare la struttura del claim
        claim_data = {
            "specifications": specifications,
            "Measure": measure,
            "Outcome": outcome
        }
        claim_data_dictionary = {
            str(i): claim_data
        }

        output.append(claim_data_dictionary)  # Aggiungere il claim alla lista

    # Salvataggio nel file JSON
    try:

        # Verifica se la directory esiste, altrimenti la crea
        directory = "RIC_CRI_GAB_CLAIMS"
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Claims salvati correttamente in {file_name}")

        # Scrivere su file JSON
        with open(os.path.join(directory, file_name), 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=4)
    except Exception as e:
        print(f"Errore durante il salvataggio del file JSON: {e}")

# Per ogni tabella estrae i claims con GEMINI 1.5 (LLM)
def extract_table_data(json_file, paper_id): 

    for table_id, table_details in json_file.items():
        if(table_id in table_types):
            table_type = table_types[table_id]
            print(Fore.BLUE + "Id Tabella: " + table_id + Style.RESET_ALL)
            print(Fore.BLUE + "Tipo Tabella: " + table_type + "\n" + Style.RESET_ALL)
            

            if(table_type == "relational"):
                rows = Extraction_methods.extract_claims_from_relational_table(table_details["table"]) #non sono i claims finali
            elif(table_type == "nested relational"):
                rows = Extraction_methods.extract_claims_from_nested_relational_table(table_details["table"]) #non sono i claims finali
            elif(table_type == "cross-table"):
                # rows= Extraction_methods.extract_claims_from_relational_table(table_details["table"]) #non sono i claims finali
                continue
            elif(table_type == "nested cross-table"):
                rows = Extraction_methods.extract_claims_from_nested_relational_table(table_details["table"]) #non sono i claims finali
    

            # Estrazione dei claims
            prompt = prompt_function("\n".join(map(str, rows)), table_details["caption"], "\n".join(table_details["references"]))
            final_claims = generate_content_with_gemini(API_key.api_key, prompt)
            parse_claims_to_json(final_claims, table_id, paper_id)

            time.sleep(7)
        else:
            print("Tabella non inclusa nel dizionario \n")

# Reitera l'estrazione dei claims su tutti i file nella directory
def process_directory():

    init()

    directory = "C:/Users/hp/ClaimsProject_4HW/Claims_extraction_project/10_samples/arxiv_10_json"
    #directory = "C:/Users/rikyj/Documents/university/Magistrale/Ingegneria dei dati/HW4/10_samples/arxiv_10_json"

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
                    
                    print(Fore.GREEN + "--- Nome del file:" + file_name + " ---\n" + Style.RESET_ALL)
                    
                    # Leggi il contenuto del file
                    json_file = json.load(file)
                    extract_table_data(json_file, file_name.replace(".json", ""))
            except Exception as e:
                print(f"Errore nell'elaborazione di {file_name}: {e} \n")
process_directory()

