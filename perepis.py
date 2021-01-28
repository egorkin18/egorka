s=str(input())
s1=str()
max=int()
while s.find('0')>-1:
    s=s[s.find('0')::]
    s1=s[:s.find('1'):]
    if len(s1)>max: max=len(s1)
    s=s[len(s1)::]
print(max)