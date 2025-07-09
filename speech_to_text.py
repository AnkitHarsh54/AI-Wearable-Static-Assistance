# stt.py

import vosk
import sounddevice as sd
import queue
import json
import os
import zipfile
import gdown

# Your Google Drive file ID for the zipped model
# Replace this with the correct file ID of your ZIP
file_id = "10iMmI354TbSGwwMubWn1yt2jB27OPG4G"

# Path to unzip the model
model_path = "model-en"

# If model folder does not exist, download and extract
if not os.path.exists(model_path):
    print("Model folder not found. Downloading from Google Drive...")

    url = f"https://drive.google.com/uc?id={file_id}"
    output_zip = "vosk_model.zip"

    # Download the zip file
    gdown.download(url, output_zip, quiet=False)

    # Extract the zip
    with zipfile.ZipFile(output_zip, 'r') as zip_ref:
        zip_ref.extractall(model_path)

    # Delete the zip file
    os.remove(output_zip)

    print(f"Model downloaded and extracted to {model_path}")

# Initialize Vosk model
model = vosk.Model(model_path)
q = queue.Queue()

def listen_once():
    rec = vosk.KaldiRecognizer(model, 16000)

    def callback(indata, frames, time, status):
        q.put(bytes(indata))

    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("Listening... Speak now.")
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                return text
