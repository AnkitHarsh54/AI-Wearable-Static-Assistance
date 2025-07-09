# stt.py

import vosk
import sounddevice as sd
import queue
import json
import os

# Download and unzip a Vosk model if you haven't already.
# Example model: https://alphacephei.com/vosk/models

model_path = "model-en"

if not os.path.exists(model_path):
    raise RuntimeError(f"Vosk model not found at {model_path}. Download it and unzip.")

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

