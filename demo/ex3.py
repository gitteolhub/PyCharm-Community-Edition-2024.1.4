print(int(3/2))  # Java랑 다르게 변환할 연산자 종류에는 소괄호 없이 적어도 됨
print(int('2'))  # 문자열도 숫자라면 변환 가능
print(type(2))
n = int(2)
n = n + 1
print(type(n))  # n의 tpye이 <class 'int'>라고 출력됨
print(type('글자'))
print('-' * 10)  # 구분줄 사용할 때 앞에서 배운 문자 곱하기 응용
print(divmod(5, 2))  # 몫과 나머지 계산
print('a' + str(1+2))  # 문자열과 합쳐서 출력하면 계산한 값이 자동으로 문자열이 되는 Java랑 다르게 수동으로 형변환을 해줘야한다.