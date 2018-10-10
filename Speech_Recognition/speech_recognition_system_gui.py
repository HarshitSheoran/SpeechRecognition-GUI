import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from gtts import gTTS
import speech_recognition as sr
from pygame import mixer
import time
mixer.init()
kivy.require('1.9.1')


class MyWindowApp(App):

    def __init__(self):
        super(MyWindowApp, self).__init__()

        self.btn = Button(text='Ask Something')
        self.lbl = Label(text='Read Me!')

    def build(self):
        self.btn.bind(on_press=self.clk)
        layout = BoxLayout()
        layout.orientation = 'vertical'
        layout.add_widget(self.lbl)
        layout.add_widget(self.btn)

        return layout

    def program(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            speech = gTTS("Hello!, how can I help You")
            speech.save("hello.mp3")
            mixer.music.load('hello.mp3')
            mixer.music.play()
            time.sleep(2)
            print("Say Something")
            self.lbl.text = 'Say Something'
            audio=r.listen(source)
        try:
            print("Here 43")
            text = r.recognize_google(audio)
            print(text)
            self.lbl.text = text
            if "think" in text and "technical partner" in text or "thought" in text and "technical partner" in text:
                speech = gTTS("Technical Partner is a company with many international relationships, with the enthosiasm of the C E O Deepanshu, The company is touching the skies.")
                speech.save("answer.mp3")
                mixer.music.load('answer.mp3')
                mixer.music.play()
            if "who" in text and "Deepanshu" in text:
                speech = gTTS("Deepanshu, the C E O of Technical Partner is a great man with great ideas to power the world, also he is a cyber-security expert.")
                speech.save("answer.mp3")
                mixer.music.load('answer.mp3')
                mixer.music.play()

        except:
            pass

    def clk(self, obj):
        self.program()


window = MyWindowApp()
window.run()
