from gtts import gTTS

def speak(text, language="en", voice="en-US_Standard-B"):
  """
  Converts text to speech audio using Google Text-to-Speech API.

  Args:
      text: The text to be converted to speech.
      language: The language code (e.g., "en" for English, "es" for Spanish).
      voice: The voice name (e.g., "en-US_Standard-B" for US English female).
  """
  tts = gTTS(text=text, lang=language, slow=False)
  tts.save("output.mp3")
  print("Audio generated. Playing...")
  # You can use an external library to play the audio here

def main():
  text = input("Enter text to convert: ")
  # Present language and voice selection options (not implemented here)
  language = "en"  # Replace with user selection
  voice = "en-US_Standard-B"  # Replace with user selection
  speak(text, language, voice)

if __name__ == "__main__":
  main()
