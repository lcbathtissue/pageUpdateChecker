import time
import requests
from playsound import playsound

URL = "https://registrar.ontariotechu.ca/winter-2022.php"
delaySeconds = 10
hitDetection = 0.001  # 1 is 100% , 0.001 is 0.1%

response = requests.get(URL)
counter = 1
length = len(response.content)
MAX = length * (1 + hitDetection)
MIN = length * (1 - hitDetection)
print(f"{URL}")
while True:
    response = requests.get(URL)
    length = len(response.content)
    if length <= MIN or length >= MAX:
        print(f"CHECK PAGE! {URL}")
        playsound('sound.mp3')
        break
    else:
        print(f"[{counter}] No Change..")
    time.sleep(60)
    counter += 1
