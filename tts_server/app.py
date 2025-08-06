from gradio_client import Client
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import tempfile
import os

app = Flask(__name__)
CORS(app)
client = Client("NihalGazi/Text-To-Speech-Unlimited")

def synthesize_tts(prompt, voice="alloy", emotion="neutral", use_random_seed=True, specific_seed=12345):
    result = client.predict(
        prompt=prompt,
        voice=voice,
        emotion=emotion,
        use_random_seed=use_random_seed,
        specific_seed=specific_seed,
        api_name="/text_to_speech_app"
    )
    audio_path = result[0]
    return audio_path

@app.route('/tts', methods=['POST'])
def tts():
    data = request.json
    prompt = data.get('prompt', 'Hello!')
    voice = data.get('voice', 'alloy')
    emotion = data.get('emotion', 'neutral')
    use_random_seed = data.get('use_random_seed', True)
    specific_seed = data.get('specific_seed', 12345)
    import time
    start_time = time.time()
    audio_path = synthesize_tts(prompt, voice, emotion, use_random_seed, specific_seed)
    duration = time.time() - start_time
    response = send_file(audio_path, mimetype='audio/wav')
    response.headers['X-TTS-Generation-Time'] = str(duration)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
