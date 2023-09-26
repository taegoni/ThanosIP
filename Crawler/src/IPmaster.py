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

class ip_shredder:
    
    def __init__(self):
        self.all='^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\/?([0-9]|[1-2][0-9]|3[0-2])$'
        self.alpha_clear='[^0-9\./]'
        self.ip_only='^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$'
        self.subnet_only='^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\/([0-9]|[1-2][0-9]|3[0-2])$'
    
    def ip_extractor(self,text,mode): # 텍스트에서 ip만 뽑아오기. 0 -> 서브넷 전부 1 -> 서브넷 제외. 2 -> 서브넷만
        self.mode=[self.all,self.ip_only,self.subnet_only][mode]
        self.noalpha=re.sub(self.alpha_clear," ",text).split()
        self.get_ip=re.compile(self.mode)
        self.response=[]
        for candi in noalpha:
            matcher=self.get_ip.match(candi)
            if matcher:
                self.response.append(matcher.group())
        return self.response
    
    def ip_spreader(self,subnet): # 서브넷 펼쳐보기. 리스트로 반환?
        ip,sub=subnet.split('/');sub=int(sub)
        ids=ip.split(".")
        spread_list=[]
        host_id, network_id = ids[sub // 8 :], ids[: (sub // 8)]
        start=self.sub_border[(7-(sub % 8))]
        single=".".join(network_id)
        i=len(host_id)
        if i == 4:
            print('NOT accepted')
        elif i ==3:
            for x in range(start,256):
                for y in range(0,256):
                    for z in range(0,256):
                        spread_list.append(single+"."+str(x)+"."+str(y)+"."+str(z))
        elif i ==2:
            for x in range(start,256):
                for y in range(0,256):
                    spread_list.append(single+"."+str(x)+"."+str(y))
        elif i ==1:
            for x in range(start,256):
                spread_list.append(single+"."+str(x))
        return spread_list
    
    # def ip_zipper(self,ips): #가능한 것들 subnet으로 묶어주기
    #     pass
    
    def in_subnet(self,ip,subnet): #서브넷 포함 확인하기.
        self.ip_spreader
        self.s=''


# input_file_name='raw_list.txt' # path = current folder, type it without file type
# input_file_name='firehol_level1.netset'
input_file_name='raw_list.txt'
input_file_path=f'./data/resources/{input_file_name}'
alpha_clear='[^0-9\./]'
ip_get=re.compile('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\/?([0-9]|[1-2][0-9]|3[0-2])$')
import_file=open(input_file_path,'r',encoding='utf-8')
export_file=open(f'./data/preprocessed/{input_file_name.split()[0]}_ppd.txt','w',encoding='utf-8')
for line in tqdm(import_file.readlines(),desc="진행률 : "):
    noalpha=re.sub(alpha_clear," ",line).split()
    for ip_cand in noalpha:
        matcher=ip_get.match(ip_cand)
        if matcher:
            export_file.write(matcher.group()+'\n')
import_file.close()
export_file.close()