import sys

data = sys.stdin.readline()

number = int(data)
count = 0

택희, 영훈, 남규 = 0, 0, 0
candy_count = 0
for 택희 in range(2, number+1, 2):
    for 영훈 in range(1, number+1):
        for 남규 in range(1, number+1):
            candy_count = 택희 + 영훈 + 남규
            if (number == candy_count):
                if 남규 >= 영훈 + 2:
                    count += 1

sys.stdout.write(str(count)+ '\n')