def multi(a):
    for i in range(1,10):
        print(a,"*",str(i),"=",a * i)

while True:
    print("=" * 30)
    print("1, n까지 정수의 합")
    print("2, n~m까지 k의 배수의 합")
    print("3, 구구단 출력")
    print("4, 종료")
    menu = int(input("번호를 입력(1~4):"))
    
    if menu == 1:
        n = int(input("정수를 입력:"))
        sum = 0
        for i in range(n+1):
            sum += i
        print(n,"까지의 정수의 합:",sum)
        
    if menu == 2:
        n = int(input("시작 값 입력:"))
        m = int(input("끝 값 입력:"))
        k = int(input("배수 입력:"))
        sum = 0
        for i in range(n,m+1):
            if i % k == 0:
                sum += i
        print("%d와 %d의 %d배수의 합:%d" %(n, m, k, sum))

    if menu == 3:
        a = int(input("정수를 입력:"))
        multi(a)
        
    if menu == 4:
        print("프로그램을 종료합니다.......")
        break
    
            
            
        
        
    
