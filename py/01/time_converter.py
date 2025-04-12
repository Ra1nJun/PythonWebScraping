import math

time_bf = 12345

h = time_bf // 3600
time_af = time_bf % 3600

m = time_af / 60
m = math.floor(m)
time_af %= 60

s = time_af % 60

print(f'{time_bf}초는 {h}시간 {m}분 {s}초입니다.')