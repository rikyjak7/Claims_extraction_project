import os
import json
from collections import Counter

def count_json_fields():
    """
    Conta le occorrenze di ciascun 'name', 'value' e 'Measure' in tutti i file JSON in una directory.

    :param directory_path: Percorso alla directory contenente i file JSON.
    :return: Tuple di tre dizionari: ({name: occorrenze}, {value: occorrenze}, {Measure: occorrenze}).
    """
    name_counter = Counter()
    value_counter = Counter()
    measure_counter = Counter()

    directory_path = "C:/Users/hp/ClaimsProject_4HW/Claims_extraction_project/RIC_CRI_GAB_CLAIMS"

    # Itera attraverso tutti i file nella directory
    for filename in os.listdir(directory_path):

        if filename.endswith(".json"):  # Considera solo i file con estensione .json
            file_path = os.path.join(directory_path, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    data = json.load(file)  # Carica il contenuto del file JSON

                    # Itera sui claims all'interno del file
                    for claim in data:
                        for key, value in claim.items():

                            # Conta i 'name' nelle specifiche
                            specifications = value.get("specifications", {})
                            for spec in specifications.values():
                                name = spec.get("name")
                                if name:
                                    name_counter[name] += 1

                                value_field = spec.get("value")
                                if value_field:
                                    value_counter[value_field] += 1  # Incrementa il valore

                            # Conta le 'Measure'
                            measure = value.get("Measure")
                            if measure:
                                measure_counter[measure] += 1
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Errore nel file {filename}: {e}")

    print("Debug - Contatore dei name:", dict(name_counter))
    print("\n")
    print("Debug - Contatore dei value:", dict(value_counter))  # Log per verificare i conteggi
    print("\n")
    print("Debug - Contatore delle measure:", dict(measure_counter))


    return dict(name_counter), dict(value_counter), dict(measure_counter)

count_json_fields()