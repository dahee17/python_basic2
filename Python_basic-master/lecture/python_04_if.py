#조건문(Condition) : if~elif~else

# - 특정 조건을 만족하는 경우에만 수행할 작업이 있는 경우
# - 모든 조건은 boolean으로 표현됨
# - 조건문의 겨우 if, elif, else 블록 내 종속된 코드 들여쓰기
# - 모든 블록문의 시작점은 마지막에 :(콜론, colon) 추가
# - 들여쓰기 필수

# 제어문 기본 문법
# if 조건1:
#   code
# elif 조건2:
#   code
# elif 조건3:
#   code
# else:
#   code

# 조건문 4가지 조합
# 1. if
# 2. if~elif~elif
# 3. if~else
# 4. if~elif~else

# 점수 계산기
# - 91 ~ 100 : A
# - 81 ~ 90 : B
# - 71 ~ 80 : C
# - 61 ~ 70 : D
# - 60이하 : F
score =  95  # 0~100점
if  91<=score :
    print("A")
elif  81<=score :
    print("B")
elif 71<= score:
    print("C")
elif  61<=score :
    print("D")
else:
    print("F")

# 논리 연산자 : AND, OR, NOT

# 1. AND
# 조건1   조건2   결과
#   F and  F      F
#   T and  F      F
#   F and  T      F
#   T and  T      T

# 2. OR
# 조건1   조건2   결과
#   F  or  F      F
#   T  or  F      T
#   F  or  T      T
#   T  or  T      T

# 3.NOT
# T -> F
# F -> T

# 문제1. 어떤 종류의 학생인지 맞히기?
# (초등, 중등, 고등, 대학생, 학생X)

from datetime import datetime

born = input("당신이 태어난 년도를 입력하세요: ")
print(born)
today = datetime.today().year
age = today - int(born)+1
print(age)

if age <= 26 and age >= 20:
    print("대학생")
elif age < 20 and age >=17 :
    print("고등학생")
elif age < 17 and age >= 14 :
    print("중학생")
elif age < 14 and age >= 8 :
    print("초등학생")
else :
    print("학생이 아닙니다.")