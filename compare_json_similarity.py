import os
import json
from difflib import SequenceMatcher

def calculate_similarity(json1, json2):
    """
    Calcola la similarità tra due oggetti JSON.
    """
    json1_str = json.dumps(json1, sort_keys=True)
    json2_str = json.dumps(json2, sort_keys=True)
    return SequenceMatcher(None, json1_str, json2_str).ratio()

def find_matching_file(file1, dir2):
    """
    Trova il file corrispondente nella seconda directory.
    """
    base_name = file1.replace("_claims.json", "_claims_groundtruth.json")
    return os.path.join(dir2, base_name) if os.path.exists(os.path.join(dir2, base_name)) else None

def calculate_total_similarity(dir1, dir2):
    """
    Calcola la similarità totale tra i file corrispondenti di due directory.
    """
    total_similarity = 0
    matched_files_count = 0

    # Itera sui file della prima directory
    for file1 in os.listdir(dir1):
        if file1.endswith("_claims.json"):
            file1_path = os.path.join(dir1, file1)
            file2_path = find_matching_file(file1, dir2)

            if file2_path:
                # Leggi i file JSON
                with open(file1_path, "r", encoding="utf-8") as f1, open(file2_path, "r", encoding="utf-8") as f2:
                    json1 = json.load(f1)
                    json2 = json.load(f2)

                # Calcola la similarità
                similarity = calculate_similarity(json1, json2)
                total_similarity += similarity
                matched_files_count += 1

                print(f"Similarità tra {file1} e {os.path.basename(file2_path)}: {similarity:.2f}")

    if matched_files_count == 0:
        print("Nessun file corrispondente trovato.")
        return 0

    # Restituisci la similarità media
    average_similarity = total_similarity / matched_files_count
    print(f"\nSimilarità totale: {total_similarity:.2f}, Similarità media: {average_similarity:.2f}\n")
    return total_similarity

dir1 = "C:/Users/hp/ClaimsProject_4HW/Claims_extraction_project/RIC_CRI_GAB_CLAIMS"
dir2 = "C:/Users/hp/ClaimsProject_4HW/Claims_extraction_project/GROUND_TRUTH" # ground truth
calculate_total_similarity(dir1, dir2)
