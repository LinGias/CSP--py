import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=list(map(int,input().split()))
S_list=[]
S_XOR=[]
res=[]
for i in range(m):
    s=list(map(int,input().split()))
    parts=s[1:]
    S_list.append(parts)
    S_XOR_num=0
    for num1 in parts:
        S_XOR_num=S_XOR_num^a[num1-1]
    S_XOR.append(S_XOR_num)
for i in range(m):
    t= list(map(int, input().split()))
    parts=t[1:]
    x=0
    for x1 in parts:
        x=x^a[x1-1]
    rans=1 if parts==S_list[i] else 0
    ans=1 if x==S_XOR[i] else 0
    if rans==ans:
        res.append("correct")
    else:
        res.append("wrong")
for s in res:
    print(s)







# s="10 20 30"
# print(s.split())

# line=list(map(int,"5 1 2 3 4 5".split()))
# print(line)

# text="hello world python"
# print(text.split())

# a="2,4,6,8"
# print(a.split(","))

# #练习5
# import sys,time
# ans=list(map(int,sys.stdin.readline().split()))
# size=ans[0]
# print(ans[1:])

#原做法：遍历了两遍，可能会超时
import sys,time
input=sys.stdin.readline
#map本身就可以解包赋值给n,m,因此不用list会显得多余
start_time=time.time()
n,m=map(int,input().split())
a=list(map(int,input().split()))
S=[[]for _ in range(m)]
T=[[]for _ in range(m)]
for i in range(m):
    parts=list(map(int,input().split()))
    S[i].extend(parts[1:])
for i in range(m):
    parts = list(map(int, input().split()))
    T[i].extend(parts[1:])
for i in range(m):
#rans
    ans=1
    rans=1
    if len(S[i])!=len(T[i]):
        rans=0
    else:
        for j in range(len(S[i])):
            if(S[i][j]!=T[i][j]):
                rans=0

    fs=a[S[i][0]-1]
    ft=a[T[i][0]-1]
    for j in range(1,len(S[i])):
        fs=fs^a[S[i][j]-1]
    for j in range(1,len(T[i])):
        ft=ft^a[T[i][j]-1]
    if fs!=ft:
        ans=0
    if ans==rans:
        print("correct")
    else:
        print("wrong")
end_time=time.time()
print(f"{end_time-start_time}")


