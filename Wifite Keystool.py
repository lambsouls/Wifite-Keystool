#!/usr/bin/env python
# coding: utf-8

# In[35]:


#全局引用
import random
#全局变量
x=0


# In[43]:


#函数区域 ↓


# In[24]:


def rounum(a,b):
    '''生成a到b之间的随机数'''
    num=random.randint(a,b)
    return num


def rouxiao():
    '''随机小写字母'''
    num=chr(rounum(97,122))
    return num



def rouda():
    '''随机大写字母'''
    num=chr(rounum(65,91))
    return num    


# In[ ]:


#主体


# In[ ]:


#输出标题
a1=13
while a1>0:
    print(end='—')
    a1-=1
print("")
print("* Wifite Keystool v1.00 *")
a2=13
while a2>0:
    print(end='—')
    a2-=1
print("")


# In[ ]:


#输入区域
#输入最小位数
print("Minimum number of digits:")
minimun=input()
while minimun.isdigit()==0: #判断是否输入的是数字
    print("[Warning] Illegal input,please re-enter:")
    minimun=input()
while int(minimun)<6:#判断是否大于6位
    print("[Warning] Illegal input,please re-enter:")
    minimun=input()
while int(minimun)>20:#判断是否小于20位
    print("[Warning] Illegal input,please re-enter:")
    minimun=input()
print("")


#输入最大位数
print("Maximum number of digits:")
maximun=input()
while maximun.isdigit()==0: #判断是否输入的是数字
    print("[Warning] Illegal input,please re-enter:")
    maximun=input()
while int(minimun)>int(maximun): #判断是否大于最小位数
    print("[Warning] Illegal input,please re-enter:")
    maximun=input()
while int(maximun)>20: #判断是否小于20位
    print("[Warning] Illegal input,please re-enter:")
    maximun=input()
print("")

#是否包含数字
print("Does the keys contain numbers?")
print("[0] NO")
print("[1] YES")
havenumbers=input()
while havenumbers.isdigit()==0: #判断是否输入的是数字
    print("[Warning] Illegal input,please re-enter:")
    print("[0] NO")
    print("[1] YES")
    havenumbers=input()
while int(havenumbers)>1: #判断是否小于等于1
    print("[Warning] Illegal input,please re-enter:")
    print("[0] NO")
    print("[1] YES")
    havenumbers=input()
while int(havenumbers)<0: #判断是否大于等于0
    print("[Warning] Illegal input,please re-enter:")
    print("[0] NO")
    print("[1] YES")
    havenumbers=input()
print("")

#是否包含小写字母
print("Does the keys contain lowercase letters?")
print("[0] NO")
print("[1] YES")
havelowercaseletters=input()
while havelowercaseletters.isdigit()==0: #判断是否输入的是数字
    print("[Warning] Illegal input,please re-enter:")
    print("[0] NO")
    print("[1] YES")
    havelowercaseletters=input()
while int(havelowercaseletters)>1: #判断是否小于等于1
    print("[Warning] Illegal input,please re-enter:")
    print("[0] NO")
    print("[1] YES")
    havelowercaseletters=input()
while int(havelowercaseletters)<0: #判断是否大于等于0
    print("[Warning] Illegal input,please re-enter:")
    print("[0] NO")
    print("[1] YES")
    havelowercaseletters=input()
print("")

#是否包含大写字母
print("Does the keys contain lowercase capital letters?")
print("[0] NO")
print("[1] YES")
havecapitalletters=input()
while havecapitalletters.isdigit()==0: #判断是否输入的是数字
    print("[Warning] Illegal input,please re-enter:")
    print("[0] NO")
    print("[1] YES")
    havecapitalletters=input()
while int(havecapitalletters)>1: #判断是否小于等于1
    print("[Warning] Illegal input,please re-enter:")
    print("[0] NO")
    print("[1] YES")
    havecapitalletters=input()
while int(havecapitalletters)<0: #判断是否大于等于0
    print("[Warning] Illegal input,please re-enter:")
    print("[0] NO")
    print("[1] YES")
    havecapitalletters=input()
print("")

#把参数变成整型
minimun=int(minimun)
maximun=int(maximun)
havenumbers=int(havenumbers)
havelowercaseletters=int(havelowercaseletters)
havecapitalletters=int(havecapitalletters)

#生成随机位数
weishu=rounum(minimun,maximun)

#创建检查字典

#选择数据类型
while x==0:
    n=0
    while n==0:
        n1=rounum(1,3)
        if n==0 and n1==1 and havenumbers==1:
            n=1
        if n==0 and n1==2 and havelowercaseletters==1:
            n=1
        if n==0 and n1==3 and havecapitalletters==1:
            n=1

    if n1==1:
        nx=str(rounum(0,9))
    if n1==2:
        nx=str(rouxiao())
    if n1==3:
        nx=str(rouda()) 
    
    weishu=rounum(minimun,maximun)
    while weishu>1:
        n=0
        while n==0:
            n1=rounum(1,3)
            if n==0 and n1==1 and havenumbers==1:
                n=1
            if n==0 and n1==2 and havelowercaseletters==1:
                n=1
            if n==0 and n1==3 and havecapitalletters==1:
                n=1
        weishu-=1
        if n1==1:
            nx+=str(rounum(0,9))
        if n1==2:
            nx+=str(rouxiao())
        if n1==3:
            nx+=str(rouda()) 
    print(nx)
    f = open('wordlist-probable.txt', 'a')
    f.write(nx)
    f.write('\n')

