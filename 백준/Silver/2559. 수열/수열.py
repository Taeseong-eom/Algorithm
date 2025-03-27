import sys

data = sys.stdin.readlines()

num_line = list(map(int, data[0].strip().split()))

N = num_line[0]

K = num_line[1]

line = list(map(int, data[1].strip().split()))

누적합 = []

sum = 0

for i in line:
    sum = sum + i
    누적합.append(sum)

max_mean_temp_list = []


max_mean_temp_list.append(누적합[K - 1])


for i in range(K, N):
    daily_mean_temp = 누적합[i] - 누적합[i - K]
    max_mean_temp_list.append(daily_mean_temp)


max_mean_temp = max(max_mean_temp_list)
print(max_mean_temp)

