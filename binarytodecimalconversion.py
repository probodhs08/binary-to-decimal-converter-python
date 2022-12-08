'''from tarfile import LENGTH_NAME


a="1001101"
len1=len(a)
count=0
ans=0
for i in range(len1):
    if a[len1-1-i]=='1':
        ans+=2**count
    count+=1
print(ans)'''
'''a="11001101"
b="10010010"
len1=len(a)
ans=""
for i in range(len1):
    if ((a[len1-1-i]=='1' and b[len1-1-i]=='0') or (a[len1-1-i]=='0' and b[len1-1-i]=='1')):
        ans="1"+ans
    else:
        ans="0"+ans
print(ans)
'''
a="11001101"
b="10010010"
len1=len(a)
ans=""
for i in range(len1):
    if ((a[len1-1-i]=='1' and b[len1-1-i]=='0') or(a[len1-1-i]=='1' and b[len1-1-i]=='1') or (a[len1-1-i]=='0' and b[len1-1-i]=='1')):
        ans="1"+ans
    else:
        ans="0"+ans
print(ans)
