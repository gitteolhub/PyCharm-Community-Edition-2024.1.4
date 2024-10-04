# 만점자가 가장 많은 문제 : Core Banking/Server 직군

# # 출제자의 한마디
# 이 문제는 만점자가 1435명으로 가장 많았는데요. 실제로도 난이도가 가장 낮은 문제로, Server 직군에 지원하는 지원자라면 반드시 맞추어야 하는 문제로 생각하고 출제했어요. 문자열과 반복문을 이용해 프로그래밍할 수 있는지 확인하는 기초적인 문제에요.

# 문제명 : 멋쟁이 숫자

# 숫자로만 이루어진 문자열 s가 있습니다. (0 <=  s.length < 1,000)
# 아래의 조건을 모두 만족하는 숫자를 '멋쟁이 숫자'라고 합니다.

# [조건]
# 1. 길이가 3인 s의 substring을 10진수로 읽은 숫자이다.
# 2. 각 자리의 숫자가 모두 같다.

# 구현사항

# 문자열s를 입력받아 멋쟁이 숫자를 리턴하는 함수를 만들어주세요.

# 만약, 멋쟁이 숫자가 여러 개 존재하는 경우에는 가장 큰 수를 리턴합니다.
# 만약, 가장 큰 멋쟁이 숫자가 000이라면 0을 리턴합니다.
# 만약, 멋쟁이 숫자가 존재하지 않다면 -1을 리턴합니다.

# 예시 문제

# 예시 1

# 입력: s = “12223”
# 출력: 222

# 예시 2

# 입력: s = “111999333”
# 출력: 999
# 설명: 111, 333, 999 3가지가 존재하고 999가 제일 크므로 999를 리턴합니다.

# 예시 3

# 입력: s = “123”
# 출력: -1

# region 모범 답안
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# class Solution {
#     fun solution(s: String): Int {
#         var biggest = -1
#         for (i in 0 until s.length-2) {
#             if (s[i] == s[i+1] && s[i+1] == s[i+2]) {
#                 biggest = Math.max(biggest, s.substring(i, i+3).toInt())
#             }
#         }
#         return biggest
#     }
# }
# endregion
s = input()
cool_number = -1
for i in range(len(s) - 2):
    if s[i] == s[i + 1] == s[i + 2]:
        if s[i] == '0':
            print('0')
        elif int(s[i] * 3) > cool_number:
            cool_number = s[i] * 3
        print(s[i] * 3)
    else:
        print('-1')