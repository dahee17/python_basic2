# 문제 1) 입력된 단수를 출력하는 코드
# dan = int(input("단수")
# for i in range(1, 10):
#   print(f"{dan}x{i}={dan*i}")

# 문제 2) 2단~ 9단까지 출력하기(2~9) => 해당 단 출력, 중첩 for 문
# 구구단 2단 출력
# 2x1=2
# 2x2=4
# ...
# 2x9=18
for i in range(2, 10):
    for j in range(1,10):
        print(f"{i}x{j}={i*j}")

# 문제 3) list a의 평균값을 계산하세요.
print("=" * 200)
a = {1, 2, 3, 4, 5, 99, 87, 54, 2, 5, 4}
total = 0
for i in a:
    total += i
length = len(a)
result = total / length
# round(값, 소수점숫자) : 반올림
print(round(result,2)) # 평균값

# 문제 4) list b에서 최소값 찾기!
print("=" * 200)
b = [22, 1, 4, 7, 98]
num_min = b[0]
for x in b :
    if x < num_min:
        num_min = x
print(num_min)  # 1 출력

# 문제 5) list c의 최솟값, 최대값 찾기
print("=" * 200)
c = [2, 5, 7, 1, 8]
num_min = num_max = c[0]
for i in c:
    if i < num_min:
        num_min = i
    if j > num_max:
        num_max = i

print(num_min)
print(num_max)

print("=" * 200)
# 사용자가 입력한 값 1, 2, 3
# 아닌 경우 다시 입력하도록.
num = int(input("값 : "))
# if 4 > num >0 :
while True :
    if num in [1, 2, 3]:
      print(f"{num}을 입력하셨습니다.")
      break
    else:
      print("1, 2, 3의 값만 입력해주세요.")
      break

# 문제 7> 1부터 100까지 총합을 출력하는 코드
print("=" * 200)
sum = 0
for X in range(1, 101) :
    sum += X
print(sum)

tot = 0
j = 0
while True:
    j += 1
    if j == 101:
        break
    tot += j
print(tot)