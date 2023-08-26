import os
import random
import wikipedia
import time
from datetime import datetime
import webbrowser
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from driver import driver
import webdriver_assistant


wikipedia.set_lang("TR")
r = sr.Recognizer()


def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio, language="tr-TR")
            voice = voice.lower()
        except sr.UnknownValueError:
            print("Asistan: Anlayamadım")
        except sr.RequestError:
            print("Asistan: Sistem Çalışmıyor")
        return voice


def response(voice):
    global search
    if "jarvis" in voice or "açıl susam açıl" in voice:
        playsound("jarvistart.mp3")
    if "merhaba" in voice:
        selection = ["merhaba, nasılsınız? gayet iyi görünüyorsunuz. yapmamı istediğiniz birşey var mı ?: ", "Bugün yapılacak işler çok sanırım ?: ", "Ben Jarvis efendim, benden ne istersiniz? :"]
        selection = random.choice(selection)
        speak(selection)
    if "teşekkür ederim" in voice or "teşekkürler" in voice or "güzel yardım" in voice:
        speak("her zaman")
    if "sistemi kapat" in voice or "biraz dinlen" in voice or "görüşürüz ama bir yere kaybolma" in voice:
        speak("tabiiki, dikkatli olun")
        exit()
    if "hangi gündeyiz" in voice:
        today = time.strftime("%A")
        today.capitalize()
        if today == "Monday":
            today = "Pazartesi"
        elif today == "Tuesday":
            today = "Salı"
        elif today == "Wednesday":
            today = "Çarşamba"
        elif today == "Thursday":
            today = "Perşembe"
        elif today == "Friday":
            today = "Cuma"
        elif today == "Saturday":
            today = "Cumartesi"
        elif today == "Sunday":
            today = "Pazar"
        speak(today)
    if "saat kaç" in voice or "saati söyle" in voice or "saat" in voice:
        selection = ["saat şu an: ", "hemen bakıyorum: "]
        clock = datetime.now().strftime("%H:%M")
        selection = random.choice(selection)
        speak(selection + clock)
    if "arama yap" in voice or "araştır" in voice:
        speak("ne aramamı istersiniz?")
        search = record()
        url = "https://www.google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        speak("{} için bunları buldum.".format(search))
    if "detaylı ara" in voice or "detaylı söyle" in voice:
        speak("evet, neyi öğrenmek istiyorsunuz ?")
        search = record()
        url = "https://www.google.com/search?q={}".format(search)
        speak("{} için bunları buldum.".format(search))
        wikikelime = wikipedia.summary(search, sentences=1)
        webbrowser.get().open(url)
        print(wikikelime)
        speak(wikikelime)
    if "müzik listemi aç" in voice:
        speak("ne çalsın ? ")
        search = record()
        os.startfile("C:\Kullanıcılar\Akova\Music\negan").format(search)
        speak("iyi eğlenceler efendim")
    if "uygulamaya gir" in voice:
        speak("hangi uygulamaya girmek istiyorsunuz")
        runApp = record()
        runApp = runApp.lower()

        if "spotify" in voice:
            os.startfile(r"C:\Users\Akova\AppData\Local\Microsoft\WindowsApps\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\Spotify.exe")
            speak("iyi dinlemeler efendim")
        if "oyun zamanı" in runApp:
            os.startfile("D:\Steam\Steam.exe")
            speak("açıyorum")
    if "not et" in voice:
        speak("dosya ismi ne olsun ?")
        txtFile = record()
        speak("ne yazmamı istersiniz?")
        theText = record()
        f = open(txtFile, "w", encoding="utf-8")
        f.writelines(theText)
        f.close()
    if "nerede" in voice:
        search = voice.split("nerede", maxsplit=1)
        search = search[0]
        url = "https://www.google.com/maps/place/" + search
        webbrowser.get().open(url)
    if "kimdir" in voice or "kim" in voice:
        search = voice.split("nerede", maxsplit=1)
        search = search[0]
        url = "https://www.google.com/search?q=" + search
        webbrowser.get().open(url)


def speak(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)


playsound("jarvisfirst.mp3")
while True:
    voice = record()
    if voice != '':
        voice = voice.lower()
        print(voice)
        response(voice)
