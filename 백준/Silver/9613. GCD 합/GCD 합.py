import sys
import math

def gcd_sum_all():
    input = sys.stdin.read
    input_data = input().strip().split('\n') 
    
    t = int(input_data[0])
    test_cases = []

    for i in range(1, t + 1):# 테스트 개수만큼 줄 나누기
        case = list(map(int, input_data[i].split()))
        test_cases.append(case) 

    def gcd_sum(test_cases):
        results = []

        for case in test_cases:
            # n = case[0] 뒤에 나올 숫자 개수  
            numbers = case[1:] 
            total_gcd_sum = 0 

            for i in range(len(numbers)):
                for j in range(i + 1, len(numbers)):
                    gcd_value = math.gcd(numbers[i], numbers[j])
                    total_gcd_sum += gcd_value

            results.append(total_gcd_sum)

        return results

    results = gcd_sum(test_cases)
    return results


results = gcd_sum_all()
for result in results:
    print(result)
