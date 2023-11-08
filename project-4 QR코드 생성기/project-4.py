import qrcode 

### 4-1번
# qr_data = 'fow.kr'
# qr_img = qrcode.make(qr_data)

# save_path ='project-4 QR코드\\' + qr_data +'.png'
# qr_img.save(save_path)

### 4-2번 (출력하기)
file_path = r'project-4 QR코드\QR코드 모음.txt'
with open(file_path, 'rt', encoding='UTF8') as f:
    read_lines = f.readlines()

    for line in read_lines:
        line = line.strip() # 줄바꿈 삭제
        print(line)
# 4-3번 (저장 / 4-1과 동일)
        qr_data = line
        qr_img = qrcode.make(qr_data)

        save_path ='project-4 QR코드\\' + qr_data +'.png'
        qr_img.save(save_path)
