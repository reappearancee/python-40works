import itertools
import zipfile

### 6-1번
# passwd_string ="0123456789abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVWXYZ"

# for len in range(1, 4):
#     to_attempt = itertools.product(passwd_string, repeat=len)
#     for attempt in to_attempt:
#         passwd = ''.join(attempt)
#         print(passwd)

### 6-2번 (실행안돼는 코드)
# passwd_string ="0123456789abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVWXYZ"

# zFile = zipfile.ZipFile(r'project-6 압축파일 암호 푸는 프로그램\암호.zip')

# for len in range(1, 6):
#     to_attempt = itertools.product(passwd_string, repeat=len)
#     for attempt in to_attempt:
#         passwd = ''.join(attempt)
#         print(passwd)
#         try:
#             zFile.extractall(pwd = passwd.encode())
#             print(f"비밀번호는 {passwd}입니다.")
#             break
#         except:
#             pass

### 6-3번

def un_zip(passwd_string, min_len, max_len, zFile):
    for len in range(min_len, max_len):
        to_attempt = itertools.product(passwd_string, repeat= len)
        for attempt in to_attempt:
            passwd = ''.join(attempt)
            print(passwd)
            try:
                zFile.extractall(pwd = passwd.encode())
                print(f"비밀번호는 {passwd}입니다.")
                return 1
            except:
                pass

passwd_string ="0123456789abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVWXYZ"

zFile = zipfile.ZipFile(r'project-6 압축파일 암호 푸는 프로그램\암호.zip')

min_len =1
max_len =5

unzip_result = un_zip(passwd_string, min_len, max_len, zFile)

if unzip_result ==1:
    print("암호 찾기에 성공했습니다.")
else:
    print("암호 찾기에 실패했습니다.")
