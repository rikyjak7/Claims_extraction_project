import os
import json
from collections import defaultdict

def align_claims(input_dir, mapping_dict, output_file):
    # Initialize the output dictionary
    alignment_dict = defaultdict(list)

    # Iterate through each JSON file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".json"):
            # Extract PaperID and TableID from the filename
            try:
                paper_id, table_id = filename.rsplit(".", 1)[0].rsplit("_", maxsplit=2)[:2]
            except ValueError:
                print(f"Skipping file with unexpected format: {filename}")
                continue

            # Load the JSON content
            file_path = os.path.join(input_dir, filename)
            with open(file_path, "r") as f:
                claims_data = json.load(f)

            # Handle JSON structure
            if isinstance(claims_data, dict):  # JSON is a dictionary
                claim_items = claims_data.items()
            elif isinstance(claims_data, list):  # JSON is a list
                claim_items = ((claim_id, claim) for claim in claims_data for claim_id in claim.keys())
            else:
                print(f"Unexpected JSON structure in file: {filename}")
                continue

            # Process each claim
            for claim_id, claim in claim_items:
                #specifications = claim.get("specifications", {})
                id=int(claim_id)
                specifications = claim[claim_id]['specifications']
                for spec_id, spec in specifications.items():
                    for key, value in mapping_dict.items():
                        # Check if the 'name' field matches any mapping key
                        if any(mapped_key.lower() == spec.get("value", "").lower() for mapped_key in value):
                            # Construct the identifier and append to the alignment dict
                            identifier = f"{paper_id}_{table_id}_{claim_id}_{spec_id}"
                            alignment_dict[key.lower()].append(identifier)

    # Save the populated alignment dictionary to the output JSON file
    with open(output_file, "w") as f:
        json.dump(alignment_dict, f, indent=4)




def align_claims_measures(input_dir, mapping_dict, output_file):
    # Initialize the output dictionary
    alignment_dict = defaultdict(list)

    # Iterate through each JSON file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".json"):
            # Extract PaperID and TableID from the filename
            try:
                paper_id, table_id = filename.rsplit(".", 1)[0].rsplit("_", maxsplit=2)[:2]
            except ValueError:
                print(f"Skipping file with unexpected format: {filename}")
                continue

            # Load the JSON content
            file_path = os.path.join(input_dir, filename)
            with open(file_path, "r") as f:
                claims_data = json.load(f)

            # Handle JSON structure
            if isinstance(claims_data, dict):  # JSON is a dictionary
                claim_items = claims_data.items()
            elif isinstance(claims_data, list):  # JSON is a list
                claim_items = ((claim_id, claim) for claim in claims_data for claim_id in claim.keys())
            else:
                print(f"Unexpected JSON structure in file: {filename}")
                continue

            # Process each claim
            for claim_id, claim in claim_items:
                id=int(claim_id)
                measure = claim[claim_id]['Measure']
                for key, value in mapping_dict.items():
                    # Check if the 'name' field matches any mapping key
                    if any(mapped_key == measure for mapped_key in value): #tolto .lower() a mapped_key
                        # Construct the identifier and append to the alignment dict
                        identifier = f"{paper_id}_{table_id}_{claim_id}"
                        alignment_dict[key.lower()].append(identifier)

    # Save the populated alignment dictionary to the output JSON file
    with open(output_file, "w") as f:
        json.dump(alignment_dict, f, indent=4)



input_directory="C:/Users/hp/ClaimsProject_4HW/Claims_extraction_project/RIC_CRI_GAB_CLAIMS"
mapping={
    "Accuracy": ["Accuracy", "Acc", "Top-1 Acc", "Top-1 Accuracy", "Top 1 Accuracy", "rAcc", "Classification Accuracy (%)", "pix. acc."],
    "OA(%)": ["OA(%)"],
    "A": ["A"],
    "mIoU": ["mIoU", "mIoU(%)", "IoU", "IoU(%)"],
    "IoU": ["IoU", "IoU(%)"],
    "F1": ["F1", "F1-Score"],
    "mF1(%)": ["mF1(%)"],
    "Average Dice Score": ["Average Dice Score", "Averaged Dice Score", "DSC", "DC"],
    "Se": ["Se", "SE"],
    "rSe": ["rSe"],
    "Sp": ["Sp", "SP"],
    "rSp": ["rSp"],
    "AUROC": ["AUROC"],
    "Params (Mb)": ["Params (M)", "Params(Mb)"],
    "Model Size": ["Model Size"],
    "Image Encoder Size": ["Image Encoder Size"],
    "FLOPs(Gbps)": ["FLOPs(Gbps)", "Flops (G)"],
    "Latency-CPU (ms)": ["Latency-CPU (ms)"],
    "Latency-GPU (ms)": ["Latency-GPU (ms)"],
    "Inference Latency": ["Inference Latency"],
     "Throughput (img/s)": ["Throughput (img/s)"],
    "Few-Shot Accuracy (%)": ["Few-Shot Accuracy (%)"],
    "AVG": ["AVG", "Average"],
    "Mcc": ["Mcc"],
    "$D_{OD}$": ["$D_{OD}$"],
    "$D_{OC}$": ["$D_{OC}$"],
    "CD": ["CD"],
    "NSD": ["NSD"],
    "CD_top": ["CD_top"],
    "CD_bottom": ["CD_bottom"],
    "Image-to-Text Retrieval Accuracy": ["Image-to-Text Retrieval Accuracy"],
    "Text-to-Image Retrieval Accuracy": ["Text-to-Image Retrieval Accuracy"],
    "EER (%)": ["EER (%)"],
    "AP": ["AP"],
    "AP": ["APS"],
    "AP": ["APM"],
    "AP": ["APL"],
     "EMD": ["EMD"],
     "SNR": ["SNR"],
     "JA": ["JA"],
     "Imp.surf.": ["Imp.surf."],
    "Building": ["Building"],
    "Lowveg.": ["Lowveg."],
    "Tree": ["Tree"],
    "Car": ["Car"],
    "C": ["C"],
     "L": ["L"],
     "B": ["B"],
    "D": ["D"],
    "E": ["E"],
    "-none-": ["-none-"]
}

output_filename = "Measure_alignement.json"

align_claims_measures(input_directory, mapping, output_filename)
