import os
import torch
import json

device = torch.device('cpu')
torch.set_num_threads(4)
local_file = 'model.pt'

if not os.path.isfile(local_file):
    torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v4_ru.pt',
                                   local_file)
def making_audio(files_name):
    with open(files_name, "r", encoding='utf-8') as json_file:
        dict = json.load(json_file)
    json_file.close()
    example_text = dict.get('comment')

    model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
    model.to(device)

    sample_rate = 48000
    speaker = 'baya'

    for i in range(len(example_text)):
        audio_paths = model.save_wav(text=example_text[i],
                                     speaker=speaker,
                                     sample_rate=sample_rate,
                                     audio_path=rf'C:\Users\stud\PycharmProjects\pythonProject\Text-to-speech\comment_for_frag{i+1}.wav')

making_audio(r"C:\Users\stud\PycharmProjects\pythonProject\combined_output.json")