from gtts import gTTS
import os

def text_to_speech(text, output_file="output.mp3", lang="en"):
    try:
        # Create a gTTS object
        tts = gTTS(text=text, lang=lang)

        # Save the generated audio to a file
        tts.save(output_file)

        # Play the generated audio (optional)
        os.system(f"open {output_file}")
        (f"start {output_file}")  # This command works on Mac OS X and above, use different command for other OS

        return output_file
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    text = "Gucci."  # Add your text here
    output_file = text_to_speech(text)
    print(f"Audio saved to {output_file}")
# Press control+R to run TTS