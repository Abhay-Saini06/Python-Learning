import pyjokes
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty("voices")

# engine.setProperty("voice", voices[0].id)  # First voice
engine.setProperty("voice", voices[1].id)  # Second voice

joke = pyjokes.get_joke()

print(joke)

engine.say(joke)
engine.runAndWait()