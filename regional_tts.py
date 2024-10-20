from gtts import gTTS
import os

# Path to the dataset file
dataset_path = "dataset/regional_data.txt"

# Read the dataset using UTF-8 encoding
with open(dataset_path, "r", encoding="utf-8") as file:
    sentences = file.readlines()

# Loop through each sentence in the dataset
for i, sentence in enumerate(sentences):
    sentence = sentence.strip()  # Remove any extra whitespace
    if not sentence:  # Skip empty lines
        continue

    # Generate TTS for the sentence in regional language
    tts = gTTS(text=sentence, lang='hi', slow=False)  # 'hi' is for Hindi, change if needed

    # Save the output audio
    output_path = f"recordings/regional_{i+1}.mp3"
    tts.save(output_path)
    print(f"Saved: {output_path}")

# Optionally play the last generated audio file
os.system(f"start {output_path}")
