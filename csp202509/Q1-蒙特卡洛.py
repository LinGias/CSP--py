import sys
input=sys.stdin.readline
n,a=map(int,input().split())
count=0
for i in range(n):
    x,y=map(float,input().split())
    d=x**2+y**2
    #浮点数会吃精度，尽量在a*a上加一点误差范围值
    if d<=a*a+1e-9:
        count=count+1
print(f"{(4*count/n):.6f}")