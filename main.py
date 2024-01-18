import speech_recognition as sr


r = sr.Recognizer()

def speech_to_text(audio_file):
  """
  Opens and listens to an audio file and translates it to text
  Args: audio file
  Returns: text of transcribed audio file
  """
  text=""
  print('Converting audio transcripts into text. Please wait ...')
  with sr.AudioFile(audio_file) as source:
    audio_text = r.listen(source)
    try:
        text = r.recognize_google(audio_text)
    except:
         print('Sorry.. run again...')

    return text

male_path = "./audio/male.wav"
female_path = "./audio/female.wav"
male = speech_to_text(male_path)
print (male)
print("\n")
female = speech_to_text(female_path)
print (female)


