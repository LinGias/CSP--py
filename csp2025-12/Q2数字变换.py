import sys
input=sys.stdin.readline
n,m=map(int,input().split())
K=list(map(int,input().split()))
Res=list(map(int,input().split()))
Match=[0]*512#题目中说了2^9，那么就是512以内喽，变换后的数字也只能在这个范围内
#range函数，左闭右开哈
for i in range(512):
    #这个顺序别搞反了，刚开始就是xa放在前面然后结果就是答案是353
    xc=i%8
    xb=(i>>3)%8
    xa=(i>>6)%8
    #进行k次变换
    for j in range(m):
        ga=xb
        gb=(((xb**2+K[j]**2)%8)^K[j])^xc
        gc=(((xc**2+K[j]**2)%8)^K[j])^ xa
        xa=ga
        xb=gb
        xc=gc
    #一定要打括号，因为py中+的优先级大于位移符
    g=(xa<<6)+(xb<<3)+xc
    #还有这个很重要，用结果值存为索引下标，这样就可以直接利用结果的数值集合作为下标来输出了
    Match[g]=i
for e in Res:
    #
    print(Match[e])


