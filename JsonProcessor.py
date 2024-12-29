import os
import json
from Local_T5_Model import extract_claims_with_flan_t5

#Per ogni tabella estrae i claims con un LLM e li scrive su un file Json
def extract_table_data(json_file): 

    for table_id, table_details in json_file.items():
        #"references": table_details.get("references", []),
        claims = extract_claims_with_flan_t5(table_details.get("table", None),table_details.get("caption", None),"")
        parse_claims_to_json(claims)

#Scrive i claims sul json
def parse_claims_to_json(claims):
    output = {}

    for i, claim in enumerate(claims):
        parts = claim.split('|')
        specifications = {}

        for idx, part in enumerate(parts):
            if ',' in part:  # Extract specifications
                key_value = part.strip('{}').split(',', 1)
                if len(key_value) == 2:
                    key, value = key_value[0].strip(), key_value[1].strip()
                    specifications[str(len(specifications))] = {"name": key, "value": value}

        # Build the claim structure
        output[str(i)] = {
            "specifications": specifications,
            "Measure": None,  #Da modificare
            "Outcome": None   #Da modificare
        }

    # Convert to JSON format
    return json.dumps(output, indent=4)

# Example claims list
claims = [
    "|{|Dataset, LUBM-8000|, |RL-GRAPH partitions, 500 subgraphs|, |# cutting edges, 23,624,351|, |replication factor alpha, 1.23|}|",
    "|{|Dataset, LUBM-20480|, |RL-GRAPH partitions, 500 subgraphs|, |# cutting edges, 61,518,672|, |replication factor alpha, 1.21|}|",
    "|{|Dataset, SNIB-15000|, |RL-GRAPH partitions, 500 subgraphs|, |# cutting edges, 58,823,356|, |replication factor alpha, 1.52|}|"
]

# Generate the JSON
json_output = parse_claims_to_json(claims)
print(json_output)


#reitera l'estrazione dei claims su tutti i file nella directory
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