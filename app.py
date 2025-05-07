# pipeline.py (Flask backend)
from flask import Flask, request, jsonify
import base64
import io
import os
import tempfile
import requests

app = Flask(__name__)

# Configuration
API_KEY = os.getenv('SARVAM_API_KEY')
STT_URL = 'https://api.sarvam.ai/speech-to-text'
TRANSLATE_URL = 'https://api.sarvam.ai/speech-to-text-translate'
TTS_URL = 'https://api.sarvam.ai/text-to-speech'

@app.route('/translate_play', methods=['POST'])
def translate_play():
    data = request.get_json()
    role = data.get('role')  # 'teacher' or 'student'
    audio_b64 = data.get('audio')
    if not role or not audio_b64:
        return jsonify({'error': 'Missing role or audio'}), 400

    # Decode base64 to bytes
    audio_bytes = base64.b64decode(audio_b64)

    # STT
    files = {'file': ('input.wav', io.BytesIO(audio_bytes), 'audio/wav')}
    headers = {'API-Subscription-Key': API_KEY}
    stt_resp = requests.post(STT_URL, headers=headers, files=files)
    stt_resp.raise_for_status()
    stt_json = stt_resp.json()
    transcript = stt_json['transcript']

    # Translation
    src, tgt = ('hi-IN', 'pa-IN') if role == 'teacher' else ('pa-IN', 'hi-IN')
    tr_payload = {'text': transcript, 'source_language_code': src, 'target_language_code': tgt}
    tr_headers = {'Content-Type': 'application/json', 'API-Subscription-Key': API_KEY}
    tr_resp = requests.post(TRANSLATE_URL, headers=tr_headers, json=tr_payload)
    tr_resp.raise_for_status()
    translated_text = tr_resp.json()['translated_text']

    # TTS
    tts_payload = {
        'text': translated_text,
        'target_language_code': tgt,
        'speaker': 'anushka' if role=='teacher' else 'karun'
    }
    tts_headers = {'Content-Type': 'application/json', 'API-Subscription-Key': API_KEY}
    tts_resp = requests.post(TTS_URL, headers=tts_headers, json=tts_payload)
    tts_resp.raise_for_status()
    audio_b64_list = tts_resp.json().get('audios', [])
    if not audio_b64_list:
        return jsonify({'error': 'No audio returned'}), 500
    audio_out_b64 = audio_b64_list[0]

    # Return original, translated, and audio
    return jsonify({
        'original': transcript,
        'translated': translated_text,
        'audio': audio_out_b64
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
