
import sys

N = int(sys.stdin.readline()) # 입력 단어 수 N 
sum = 0

for i in range(N):
    group_word = []
    group_bool = True
    word = sys.stdin.readline().strip()    
    group_word.append(word[0])
    
    for j in word[1:]:
        if group_word[-1] == j:  
            continue
        elif j in group_word:    
            group_bool = False
            break
        else:                  
            group_word.append(j)
    
    if group_bool:  
        sum += 1

print(sum)