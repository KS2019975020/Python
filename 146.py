import random
time = random.randint(1,24)
sunny = random.choice([True, False])
print("좋은 아침입니다. 지금 시각은 " ,time,"시 입니다.")
if sunny:
    print("지금 날씨는 화창힙니다.")
else:
    print("지금 날씨는 화창하지 않습니다.")


if time>=6 and time <=9 and sunny:
    print("종달새 노래 ")
else :
    print("종달새 노래 안함")
