import subprocess

def speak(text):
    subprocess.run(["powershell", "-command", f"$speak = New-Object -ComObject SAPI.SpVoice; $speak.Speak('{text}')"])

if __name__ == '__main__':
    print("Welcome to RoboSpeaker")
    while True:


            x = input("Enter what do you want to speak: ")
            if x=="q":
                speak("Bye Bye, see you!")
                break
            speak(x)