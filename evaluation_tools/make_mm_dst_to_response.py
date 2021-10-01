import json
import ipdb
from tqdm import tqdm

FIELDNAME_DIALOG = "dialogue"

lines = []
def format_disambiguation_label(dialog):
    for turn_idx, turn in enumerate(dialog[FIELDNAME_DIALOG]):
        if "disambiguation_label" in turn:
            lines.append(turn["disambiguation_label"])
        else:
            lines.append(-100)
import argparse
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_path_text",
        type=str,
        default='../scripts/mm_dst_result.txt'
    )
    parser.add_argument(
        "--dialog_meta_data",
        type=str,
        default='../data_object_special/simmc2_dials_dstc10_devtest_inference_disambiguation.json'
    )
    parser.add_argument(
        "--output_path_json",
        type=str,
        default="response_result.json"    
    )  

    args = parser.parse_args()
    input_path_text = args.input_path_text
    output_path_txt = args.output_path_json
    dialogue_meta_data = json.load(open(args.dialog_meta_data)) # List[Dict]
    
    results = [] 
    with open(input_path_text, 'r') as f:
        for idx, line in f.read().splitlines):
            response = line.split("<EOB>")[1]
            print(response)
            ipdb.set_trace()
            results.append({
                "dialogu_id" : meta[idx]["dialog_id"],
                "predictions" : [{
                    "turn_id" : meta[idx]["turn_id"],
                    "response" : response
                }]
            })