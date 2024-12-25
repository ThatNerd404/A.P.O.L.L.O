import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)
    try:
        user_input = recognizer.recognize_google(audio)
        print(f"User said: {user_input}")
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")