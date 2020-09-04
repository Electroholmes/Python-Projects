from gtts import gTTS


tts = gTTS(text="hello everyone and welcome to electronic technocrat, your own techie guy", lang='en')
tts.save("ET.mp3")
print("Text Converted Successfully ")
