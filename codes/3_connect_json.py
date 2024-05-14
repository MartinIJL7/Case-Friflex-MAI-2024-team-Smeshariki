import json


with open('output.json', 'r') as file:
    output_data = json.load(file)

with open('gpt.json', 'r') as file:
    gpt_data = json.load(file)


output_ts = output_data["ts"]
output_timeline = output_data["timeline"]


combined_data = {
    "comment": gpt_data["comment"],
    "moves": gpt_data["moves"],
    "ts": [],
    "timeline": []
}

for ts_group in gpt_data["ts"]:
    timelines = [output_timeline[output_ts.index(int(ts))] for ts in ts_group]
    combined_data["ts"].append(ts_group)
    combined_data["timeline"].append(timelines)


with open('combined_output.json', 'w') as file:
    json.dump(combined_data, file, ensure_ascii=False, indent=4)

print("Combined data has been saved to combined_output.json")
