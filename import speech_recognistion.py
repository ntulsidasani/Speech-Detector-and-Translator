import speech_recognition
from googletrans import Translator
def record():
    microphone=speech_recognition.Recognizer()# recogniser object

    with speech_recognition.Microphone() as live_phone:
        microphone.adjust_for_ambient_noise(live_phone)#adjusts according to the background noise

        print("Listening...")
        audio=microphone.listen(live_phone) #records what u are saying

        try:
            phrase= microphone.recognize_google(audio ,language='en')
            return phrase
        except speech_recognition.UnknownValueError:
            return "cannot understand"
        
def translate_to_diffrent_lang(text):
    translator=Translator()
    result=translator.translate(text ,dest='hi')
    result2=translator.translate(text ,dest='fr')
    result3=translator.translate(text ,dest='mr')
    return result.text,result2.text,result3.text

if __name__=='__main__':
    phrase=record()
    print("we detected you said",phrase)
    a=translate_to_diffrent_lang(phrase)
    for t in a:
        print(t)
