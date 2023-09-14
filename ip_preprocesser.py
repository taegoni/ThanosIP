# ip파일을 생성하는 전처리기

# xxx.xxx.xxx.xxx 형식을 정규식으로 찾아서 저장하도록 한다.
# 문자열 사이에 있는것을 뽑아내기... 정규식....
# ? 포트나 서브넷은 어떻게 잡아낼 것인지 생각해보기.
# ? ipv4의 정규화 해보기 필요성은?

# ! 현재 방식
# ! 하나의 string에서 자꾸 못 찾아내서 이런 방법으로 돌림..
# 1. 숫자와 점을 제외한 것들을 모두 제거하여 공백화 한다.
# 2. 공백 기준 split
# 3. 각각이 ipv4인지 체크하기 ipv4 정규식을 돌린다.


import re
from tqdm import tqdm
input_file_name='raw_list.txt' # path = current folder, type it without file type
input_file_path=f'./data/resources/{input_file_name}'
# input_file_name ='laBel_sample0001' # test
alpha_clear='[^0-9\.]'
ip_get=re.compile('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$')
import_file=open(input_file_path,'r',encoding='utf-8')
export_file=open(f'./data/preprocessed/{input_file_name}_ppd.txt','w',encoding='utf-8')
for line in tqdm(import_file.readlines(),desc="진행률 : "):
    noalpha=re.sub(alpha_clear," ",line).split()
    for ip_cand in noalpha:
        matcher=ip_get.match(ip_cand)
        if matcher:
            export_file.write(matcher.group()+'\n')
import_file.close()
export_file.close()