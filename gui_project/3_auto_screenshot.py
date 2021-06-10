from PIL import ImageGrab
import time

time.sleep(5) # 5초 대기 : 사용자가 준비하는 시간

for i in range(1, 11): # 2초 간격으로 10개 이미지 저장
    img = ImageGrab.grab()
    img.save("image{}.png".format(i))
    time.sleep(2) # 2초 단위