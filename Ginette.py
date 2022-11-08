Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@JDecelles1990 
Learn Git and GitHub without any code!
Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.


bradtraversy

alexis_speech_assistant
17
178148
Code
Issues
14
Pull requests
9
Actions
Projects
Wiki
Security
Insights
alexis_speech_assistantmain.py 
@rezan21
rezan21 extended features
…
Latest commit 7db778f on Dec 24, 2019
 History
 3 contributors
@bradtraversy@rayavarapuvikram1@rezan21
128 lines (110 sloc)  4.4 KB
  
import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import yfinance as yf # to fetch financial data
import ssl
import certifi
import time
import os # to remove created audio files

class person
    name = ''
    def setName(self, name)
        self.name = name

def there_exists(terms)
    for term in terms
        if term in voice_data
            return True

r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text
def record_audio(ask=False)
    with sr.Microphone() as source # microphone as source
        if ask
            speak(ask)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError # error recognizer does not understand
            speak('I did not get that')
        except sr.RequestError
            speak('Sorry, the service is down') # error recognizer is not connected
        print(f {voice_data.lower()}) # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def speak(audio_string)
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(fkiri {audio_string}) # print what app said
    os.remove(audio_file) # remove audio file

def respond(voice_data)
    # 1 greeting
    if there_exists(['hey','hi','hello'])
        greetings = [fhey, how can I help you {person_obj.name}, fhey, what's up {person_obj.name}, fI'm listening {person_obj.name}, fhow can I help you {person_obj.name}, fhello {person_obj.name}]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)

    # 2 name
    if there_exists([what is your name,what's your name,tell me your name])
        if person_obj.name
            speak(my name is Alexis)
        else
            speak(my name is Alexis. what's your name)

    if there_exists([my name is])
        person_name = voice_data.split(is)[-1].strip()
        speak(fokay, i will remember that {person_name})
        person_obj.setName(person_name) # remember name in person object

    # 3 greeting
    if there_exists([how are you,how are you doing])
        speak(fI'm very well, thanks for asking {person_obj.name})

    # 4 time
    if there_exists([what's the time,tell me the time,what time is it])
        time = ctime().split( )[3].split()[02]
        if time[0] == 00
            hours = '12'
        else
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        speak(time)

    # 5 search google
    if there_exists([search for]) and 'youtube' not in voice_data
        search_term = voice_data.split(for)[-1]
        url = fhttpsgoogle.comsearchq={search_term}
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google')

    # 6 search youtube
    if there_exists([youtube])
        search_term = voice_data.split(for)[-1]
        url = fhttpswww.youtube.comresultssearch_query={search_term}
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on youtube')

    # 7 get stock price
    if there_exists([price of])
        search_term = voice_data.lower().split( of )[-1].strip() #strip removes whitespace afterbefore a term in string
        stocks = {
            appleAAPL,
            microsoftMSFT,
            facebookFB,
            teslaTSLA,
            bitcoinBTC-USD
        }
        try
            stock = stocks[search_term]
            stock = yf.Ticker(stock)
            price = stock.info[regularMarketPrice]

            speak(f'price of {search_term} is {price} {stock.info[currency]} {person_obj.name}')
        except
            speak('oops, something went wrong')
    if there_exists([exit, quit, goodbye])
        speak(going offline)
        exit()


time.sleep(1)

person_obj = person()
while(1)
    voice_data = record_audio() # get the voice input
    respond(voice_data) # respond

© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
