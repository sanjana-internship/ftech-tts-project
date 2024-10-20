from flask import Flask, request, jsonify
from gtts import gTTS
import os

app = Flask(__name__)

# Endpoint for English TTS
@app.route('/tts/english', methods=['POST'])
def english_tts():
    text = request.json.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    tts = gTTS(text=text, lang='en')
    output_path = "recordings/english_tts.mp3"
    tts.save(output_path)
    return jsonify({"message": "TTS generated", "file": output_path})

# Endpoint for Regional TTS
@app.route('/tts/regional', methods=['POST'])
def regional_tts():
    text = request.json.get("text", "")
    lang = request.json.get("lang", "hi")  # Default to Hindi
    if not text:
        return jsonify({"error": "No text provided"}), 400
    tts = gTTS(text=text, lang=lang)
    output_path = "recordings/regional_tts.mp3"
    tts.save(output_path)
    return jsonify({"message": "TTS generated", "file": output_path})

if __name__ == '__main__':
    app.run(debug=True)
 
