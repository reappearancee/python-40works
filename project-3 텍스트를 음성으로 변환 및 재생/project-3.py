from gtts import gTTS
from playsound import playsound
import os

### 3-1번
# text = "안녕하세요, 파이썬과 40개 작품들입니다."
# tts = gTTS(text=text, lang='ko')
# tts.save(r"hi.mp3")

### 3-2번
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# text = "안녕하세요, 파이썬과 40개 작품들입니다."

# tts = gTTS(text=text, lang='ko')
# tts.save("hi.mp3")

# playsound("hi.mp3")

### 3-3번
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path ='나의텍스트.txt'
with open(file_path, 'rt', encoding='UTF-8') as f:
    read_file = f.read()

tts = gTTS(text=read_file, lang='ko')
tts.save("myText.mp3")

playsound("myText.mp3")
