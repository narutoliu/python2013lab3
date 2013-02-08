import re

readlines=open('mystery.in','r')
writefile=open('result.txt','w')
writefile2=open('result.dat','w')
fibo_num=[0,1,1,2,3,5,13,21,34,55,144]
summary=''
for lines in readlines:   
    for i in range(0,len(lines)):
        summary=summary+(chr(ord(str(lines[i]))-5))
writefile.write(summary)

writefile.close()
dummy_list=[]
dummy_list2=[]
readresult=open('result.txt','r')
for lines in readresult:   
    dummy_list=lines.split()


for i in dummy_list:
    inside=False
    for y in dummy_list2:
        if y[0]==i:
            inside=True
            y[1]=y[1]+1
    if inside==False:
        dummy_list2.append([i,1])
first=['',0]
second=['',0]
third=['',0]



for i in dummy_list2:
    if len(i[0])>4:
        if i[1]>first[1]:
            first=i
        elif i[1]>second[1]:
            second=i
        elif i[1]>third[1]:
            third=i
writefile2.write(first[0]+' '+second[0]+' '+third[0])
print (first,second,third)
writefile2.close()


