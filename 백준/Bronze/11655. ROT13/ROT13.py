word = list(input())
result = []  

for i in range(len(word)):
    if word[i].isupper():  # 대문자일 경우
        if ord(word[i]) + 13 > 90:  
            result.append(chr(ord(word[i]) - 13))  
        else:
            result.append(chr(ord(word[i]) + 13)) 
    elif word[i].islower():  # 소문자일 경우
        if ord(word[i]) + 13 > 122: 
            result.append(chr(ord(word[i]) - 13))  
        else:
            result.append(chr(ord(word[i]) + 13)) 
    else:  
        result.append(word[i])

print(''.join(result))
