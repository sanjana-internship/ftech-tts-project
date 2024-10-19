from gtts import gTTS
import os

# Path to the dataset file
dataset_path = "dataset/english_data.txt"

# Read the dataset
with open(dataset_path, "r") as file:
    sentences = file.readlines()

# Loop through each sentence in the dataset
for i, sentence in enumerate(sentences):
    sentence = sentence.strip()  # Remove any extra whitespace
    if not sentence:  # Skip empty lines
        continue

    # Generate TTS for the sentence
    tts = gTTS(text=sentence, lang='en', slow=False)

    # Save the output audio
    output_path = f"recordings/english_tech_{i+1}.mp3"
    tts.save(output_path)
    print(f"Saved: {output_path}")

# Optionally play the last generated audio file
os.system(f"start {output_path}")
