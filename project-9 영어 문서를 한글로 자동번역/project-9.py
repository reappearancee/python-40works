import googletrans
from os import linesep

#dest에 번역될 문자 입력, src 번역할 문자 입력(생략시 auto)

### 9-1번
# translater = googletrans.Translator()

# str1 = "행복하세요"
# result1 = translater.translate(str1, dest='en', src='auto') 
# print(f"행복하세요 => {result1.text}")

# str2 ="I am happy"
# result2 = translater.translate(str2, dest='ko', src='en')
# print(f"I am happy => {result2.text}")

### 9-2번
# lang = googletrans.LANGUAGES
# print(lang)

### 9-3번
# translater = googletrans.Translator()

# read_file_path = r"project-9 영어 문서를 한글로 자동번역\영어파일.txt"

# with open(read_file_path,'r') as f:
#     readLines = f.readlines()

# for lines in readLines:
#     result1= translater.translate(lines, dest='ko')
#     print(result1.text)

### 9-4번
translater = googletrans.Translator()

read_file_path = r"project-9 영어 문서를 한글로 자동번역\영어파일.txt"
write_file_path = r"project-9 영어 문서를 한글로 자동번역\한글파일.txt"

with open(read_file_path,'r') as f:
    readLines = f.readlines()

for lines in readLines:
    result1= translater.translate(lines, dest='ko')
    print(result1.text)
    with open(write_file_path,'a', encoding='UTF-8') as f:
        f.write(result1.text + '\n')