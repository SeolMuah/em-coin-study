#-----------------------------------------------------------
#1. 동전 데이터 생성
import random
k = int(input('동전의 갯수를 입력하세요 : '))
head_probs = [float(s) for s in input('동전의 각각의 앞면이 나올 확률을 입력하세요 : ').split()]
N = int(input('데이터의 갯수를 입력하세요 : '))
M = int(input('데이터의 길이를 입력하세요 : '))

out = ' '.join([str(s) for s in head_probs])
for _ in range(N) :
    i = random.randrange(k)
    ch = ''
    for _ in range(M) : 
        ch += 'H' if random.random() < head_probs[i] else 'T'
    
    ch += f' {i}'
    out += '\n' + ch

with open('coin_data.txt', 'w') as f :
    f.write(out)

#---------------------------------------------------------






