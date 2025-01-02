import os
import json
from Table_Dictionary import table_types
import Extraction_methods

#Per ogni tabella estrae i claims con un LLM e li scrive su un file Json
def extract_table_data(json_file): 

    for table_id, table_details in json_file.items():
        if(table_id in table_types):
            table_type= table_types[table_id]
            print("Id Tabella:" + table_id)
            print("Tipo Tabella:" + table_type)
            if(table_type == "relational"):
                rows= Extraction_methods.extract_claims_from_relational_table(table_details["table"]) #non sono i claims finali
                for row in rows:
                    print(row)
            elif(table_type == "nested relational"):
                rows= Extraction_methods.extract_claims_from_nested_relational_table(table_details["table"]) #non sono i claims finali
                for row in rows:
                    print(row)
            elif(table_type == "cross-table"):
                rows= Extraction_methods.extract_claims_from_relational_table(table_details["table"]) #non sono i claims finali
                for row in rows:
                    print(row)
            elif(table_type == "nested cross-table"):
                rows= Extraction_methods.extract_claims_from_nested_relational_table(table_details["table"]) #non sono i claims finali
                for row in rows:
                    print(row)
            print("\n")
        else:
            print("tabella non inclusa nel dizionario \n")
        

            #codice per LLM per estrarre i claims a partire dalle rows


#reitera l'estrazione dei claims su tutti i file nella directory
def process_directory():

    directory = "C:/Users/rikyj/Documents/university/Magistrale/Ingegneria dei dati/HW4/10_samples/arxiv_10_json"
    #directory = "C:/Users/rikyj/Documents/university/Magistrale/Ingegneria_dei_dati/HW4/Test_1json"

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
                    print("nome del file:" + file_name + "\n")
                    json_file = json.load(file)  # Leggi il contenuto del file
                    extract_table_data(json_file)
            except Exception as e:
                print(f"Errore nell'elaborazione di {file_name}: {e}")


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

process_directory()