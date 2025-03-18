from gtts import gTTS
import os

def generate_tts(text_list, filename="output.mp3"):
    """
    Generate Hindi speech from a list of headlines.
    """
    try:
        if not text_list:
            print("No headlines provided for TTS.")
            return None

        text_to_speak = " | ".join(text_list)  # Join headlines with a pause
        tts = gTTS(text_to_speak, lang="hi")  # Convert to Hindi speech
        filepath = f"static/{filename}"  # Save inside 'static' folder
        tts.save(filepath)
        
        print(f"Audio saved at: {filepath}")
        return filepath  # Return the file path for Streamlit

    except Exception as e:
        print(f"Error in TTS: {e}")
        return None



