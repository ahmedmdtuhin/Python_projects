import requests
import json
import subprocess


def speak(text):
    subprocess.run(["powershell", "-command", f"$speak = New-Object -ComObject SAPI.SpVoice; $speak.Speak('{text}')"])

while True:
    try:

            city =input("Enter the name of the city: ")
            if city == "q":
                speak("Bye Bye, see you again.")
                break
            url = f"https://api.weatherapi.com/v1/current.json?key=2d873644a871451893072958230412&q={city}"
            r= requests.get(url)
            #print(r.text)
            #print(type(r.text))
            w_dic = json.loads(r.text)


            w1 = w_dic["location"]["name"]
            w2 = w_dic["current"]["temp_c"]
            print(f"City name: {w1} \nTemp is: {w2}")
            speak(f" The current weather in {w1} is {w2} degree celsius")
            speak("If you want to quit ,please press q or to continue type another city name.")
            print("Press q to exit.")



    except:
        print("Error: Entered a wrong city name. \n"
              "Please enter the city name again:")
        speak("Sorry, you have entered a wrong city name, please type the correct city name and if you want to quit, please type q.")
        print("Press q to exit.")












