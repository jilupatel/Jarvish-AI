import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import subprocess


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return "Sorry, I did not understand that."
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return "Could not request results; check your network connection."


def get_detailed_time():
    now = datetime.datetime.now()
    hours = now.strftime("%I").lstrip("0")  # 12-hour format without leading zero
    minutes = now.strftime("%M").lstrip("0")  # Minutes without leading zero
    seconds = now.strftime("%S").lstrip("0")  # Seconds without leading zero

    time_str = f"{hours} hour" + ("s" if hours != "1" else "")
    if minutes != "0":
        time_str += f" {minutes} minute" + ("s" if minutes != "1" else "")
    if seconds != "0":
        time_str += f" and {seconds} second" + ("s" if seconds != "1" else "")

    return time_str


if __name__ == '__main__':
    print('PyCharm')
    say("Hello, I am Jarvis AI")
    while True:
        print("Listening...")
        query = take_command()
        if query is None:
            continue

        sites = [["youtube", "https://www.youtube.com"],
                 ["wikipedia", "https://www.wikipedia.org"],
                 ["google", "https://www.google.com"]]

        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Jilu...")
                webbrowser.open(site[1])
                break  # Stop checking after the first match

        if "open music" in query.lower():
            music_path = r"C:\Users\jilu_\Downloads\clockwork-by-neeraj-waves-ncs-copyright-free-music-195167.mp3"  # Adjust the path to your music file
            if os.path.exists(music_path):
                os.startfile(music_path)
            else:
                say("Sorry, the music file was not found.")
                print("Sorry, the music file was not found.")

        if "the time" in query.lower():
            detailed_time = get_detailed_time()
            say(f"Jilu, the time is {detailed_time}")

        if "open camera" in query.lower():
            try:
                say("Opening camera...")
                subprocess.run('start microsoft.windows.camera:', shell=True)
            except Exception as e:
                say("Sorry, I couldn't open the camera.")
                print(f"Error: {e}")

        if "open visual studio code" in query.lower() or "open vs code" in query.lower():
            try:
                say("Opening Visual Studio Code...")
                subprocess.run(["code"])
            except Exception as e:
                say("Sorry, I couldn't open Visual Studio Code.")
                print(f"Error: {e}")