import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

# Khởi tạo trợ lý ảo với giọng nữ
friday = pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[1].id)

# Nói một đoạn văn bản
def speak(audio):
    print('AI:', audio)
    friday.say(audio)
    friday.runAndWait()

# Trả về thời gian hiện tại
def tell_time():
    Time = datetime.datetime.now().strftime("%I:%M %p")
    speak("It is")
    speak(Time)

# Chào hỏi tùy theo thời gian
def welcome():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good Morning, Sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon, Sir!")
    elif 18 <= hour <= 23:
        speak("Good Evening, Sir!")
    else:
        speak("Hello Sir!")
    speak("How can I help you, boss?")

# Nghe và nhận diện lệnh thoại
def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        c.pause_threshold = 2
        audio = c.listen(source)

    try:
        query = c.recognize_google(audio, language='en-US')
        print("Hiep_Pro:", query)
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please try again or type.")
        query = input("Your order is: ")
    except sr.RequestError:
        speak("Sorry, the speech service is unavailable.")
        query = input("Your order is: ")
    return query

# Hàm chính
def main():
    welcome()

    while True:
        query = command().lower()

        if "google" in query:
            speak("What should I search, boss?")
            search = command().lower()
            url = f"https://google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on Google")

        elif "youtube" in query:
            speak("What should I search, boss?")
            search = command().lower()
            url = f"https://youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on YouTube")

        elif "time" in query:
            tell_time()

        elif "quit" in query or "exit" in query:
            speak("Friday is off. Goodbye boss.")
            break

if __name__ == "__main__":
    main()
