y = 'Hello world'
print(y)
a = 1
a = 'abcd'
a = "I'm \"Python\""  # Java랑 똑같이 문자열안에 "를 넣고 싶으면 \"를 사용하면 된다.
a = "abcd \
     Java \
     Python"
print(a)
print(type(a))

# Java에서 지원하지 않는 편리한 선언 및 초기화가 가능
x, y, z = 10, 20, 30
x = y = z = 10
'''
문단 주석 작성법
'''
print(x, y, z)

# 변수 값 치환도 temp 변수 없이 바로 가능
x, y = 10, 20
x, y = y, x
print(x, y)

print("-" * 26)

# 변수 삭제도 가능. x를 다시 정의하지 않고 print시 error가 나는데 Python에선 error와 exception을 구분하지 않음
del x
x = None  # Java와 Javascript의 null과 동일한 역할
print(x)
print(type(x))

print("-" * 26)

d = 1
d += 10  # Python에서도 d를 미리 정의해야 연산 가능. d += 10은 d = d + 10의 줄임말이기 때문.
print(d)

##################################################################### 출력할 필요없는 구분선은 이렇게 사용

x = input("입력 : ")
print("x :", x)

######################

# 기본 입력받는 형식은 str(Java의 String)이며 입력 형식을 바꾸고 싶으면 자료형 변환 하듯이 하면 된다.
a = int(input("입력 1 :"))
b = int(input("입력 2 :"))
print(a + b)

# 하나 입력 후 공백(space 혹은 tab)입력 후 나머지 입력. 한 개만 입력하면 error난다.
a, b = input("문자열 두 개를 입력하세요 :").split()  # split의 소괄호 안에 ""를 적고 사이에 원하는 구분자를 적으면 된다. 공백을 넣을 경우 기본값과 다르게 너비가 정확히 일치해야 한다.
print(a, b)
a, b = map(int, input("숫자 두 개를 입력하세요 :").split())  # split 함수는 문자열을 두 개로 나눠서 리스트로 return하므로 int형변환 직접 사용 불가. map을 써야한다.
print(a + b)

#sep은 출력값 사이에 무엇을 넣을지 정하는 함수, end는 출력후 무엇을 넣을지 정하는 함수. 기본값은 각각 공백, 줄바꿈(/n)이다.
print(1, 2, sep="", end="")
print(3, 4)