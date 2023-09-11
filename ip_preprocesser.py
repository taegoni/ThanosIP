# ip파일을 생성하는 전처리기
# xxx.xxx.xxx.xxx 형식을 정규식으로 찾아서 저장하도록 한다.
# 문자열 사이에 있는것을 뽑아내기... 정규식....
import re
ip_get=re.compile('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$/g')

test_file=open('./test_list.txt','r',encoding='utf-8')
# export_file=open('./regex_test.txt','w',encoding='utf-8')
answer1=[]
answer2=[]
for line in test_file.readlines():
    # print(line)
    if ip_get.match(line):
        # export_file.write(ip_get.match(line).group()+'\n')
        answer1.append(ip_get.findall(line))
        answer2.append(ip_get.match(line).group())
print(answer1)
print(answer2)
test_file.close()
# export_file.close()