#----------------------------------------------------------
#EM알고리즘을 통한 각 시행의 동전의 확률 추정
import numpy as np
with open('coin_data.txt', 'r') as f :
    data = f.readlines()
data = [s.split() for s in data]
coin_num = len(data[0])

#초기값 설정
e_head_probs = np.random.random(coin_num)
print(e_head_probs)

import pandas as pd
df = pd.DataFrame(data[1:], columns=['sequence', 'label'])
df['label_prob'] = df['label'].apply(lambda x : data[0][int(x)])

diff = 1
while diff > 0.001 :
    pre_prob = e_head_probs.copy()
    #E-Step : Hidden variable의 Responsibility(전체 클러스터에 대한 입력데이터의 클러스터 확률) 계산
    for i in range(coin_num) :
        df[f'coin_prob_{i}'] = df['sequence'].apply(lambda seq : e_head_probs[i]**seq.count('H')*(1-e_head_probs[i])**seq.count('T'))

    for i in range(coin_num) :
        df[f'coin_resp_{i}'] = df[f'coin_prob_{i}'] / df.iloc[:, 3:3+len(e_head_probs)].sum(axis=1)
    
    #M-Step : 추정값 업데이트
    for i in range(coin_num) :
        df[f'coin_H_num_{i}'] = df.apply(lambda x : x['sequence'].count('H') * x[f'coin_resp_{i}'], axis=1)
        df[f'coin_T_num_{i}'] = df.apply(lambda x : x['sequence'].count('T') * x[f'coin_resp_{i}'], axis=1)
        h_sum, t_sum = df[f'coin_H_num_{i}'].sum(), df[f'coin_T_num_{i}'].sum()
        e_head_probs[i] = h_sum / (h_sum + t_sum)
    diff = abs(e_head_probs.sum() - pre_prob.sum())
 

#정확도 계산
label_probs = np.array([float(d) for d in data[0]])
df['coin_infer_prob'] = df.iloc[:, 5:5+len(e_head_probs)].idxmax(axis=1).apply(lambda x : e_head_probs[int(x.split('_')[-1])])
df['coin_infer'] = df['coin_infer_prob'].apply(lambda x : str(np.abs(label_probs-x).argmin()))
df['correct'] = (df['coin_infer']==df['label']).apply(lambda x : 'S' if x else 'F')
acc = df['correct'][df['correct']=='S'].count() / df['correct'].count()

print('코인별 확률 : ', e_head_probs)
print('정확도 : ', acc)



#결과 저장
save_data = data.copy()
save_data[0] += [f'{p:.3f}' for p in e_head_probs.tolist()]
for i, (c, a) in enumerate(zip(df['coin_infer'], df['correct'])):
   save_data[i+1] += [c, a]
save_data.append([str(acc)])

with open('data_result.txt', 'w') as f :
    for d in save_data :
        f.write(' '.join(d) + '\n')

print('결과 저장 완료')
