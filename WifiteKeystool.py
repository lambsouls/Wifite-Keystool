#!/usr/bin/env python
# coding: utf-8

# In[2]:


#全局引用
import random
#全局变量
x=0


# In[3]:


#函数区域 ↓


# In[4]:


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


# In[5]:


#主体


# In[6]:


#输出标题
a1=13
while a1>0:
    print(end='—')
    a1-=1
print("")
print("* Wifite Keystool v1.02 *")
a2=13
while a2>0:
    print(end='—')
    a2-=1
print("")


# In[ ]:


keys = []
print("正在读取预备处理文件...")
f = open('wordlist-probable.txt',encoding='utf-8')
line = f.readline() # 读取第一行
while line:
    line=line.strip('\n')
    txt_data = str(line) # 可将字符串变为元组
    keys.append(txt_data) # 列表增加
    line = f.readline() # 读取下一行
print("读取完毕")
print('')

#输入区域
#输入最小位数
print(end="输入最小位数(不小于6位):")
minimun=input()
p=0
while p==0:
    if minimun.isdigit(): #判断是否输入的是数字
        p+=1
        if int(minimun)>=6:#判断是否大于6位
            p+=1
            if int(minimun)<=20:#判断是否小于20位
                p+=1
    if p!=3:
        p=0
        print(end="[Warning] 非法输入，请重新输入最小位数(不小于6位):")
        minimun=input()
print("")

#输入最大位数
print(end="输入最大位数(不大于20位):")
maximun=input()
p=0
while p==0:
    if maximun.isdigit(): #判断是否输入的是数字
        p+=1
        if int(minimun)<=int(maximun): #判断是否大于最小位数
            p+=1
            if int(maximun)<=20: #判断是否小于20位
                p+=1
    if p!=3:
        p=0
        print(end="[Warning] 非法输入，请重新输入最大位数(不大于20位):")
        maximun=input()
print("")

#是否包含数字
print(end="是否包含数字([0]NO [1]YES):")
havenumbers=input()
p=0
while p==0:
    if havenumbers.isdigit(): #判断是否输入的是数字
        p+=1
        if int(havenumbers)<=1: #判断是否小于等于1
            p+=1
            if int(havenumbers)>=0: #判断是否大于等于0
                p+=1
    if p!=3:
        p=0
        print(end="[Warning] 非法输入，请重新输入是否包含数字([0]NO [1]YES):")
        havenumbers=input()
print("")

#是否包含小写字母
print(end="是否包含小写字母([0]NO [1]YES):")
havelowercaseletters=input()
p=0
while p==0:
    if havelowercaseletters.isdigit(): #判断是否输入的是数字
        p+=1
        if int(havelowercaseletters)<=1: #判断是否小于等于1
            p+=1
            if int(havelowercaseletters)>=0: #判断是否大于等于0
                p+=1
    if p!=3:
        p=0
        print(end="[Warning] 非法输入，请重新输入是否包含小写字母([0]NO [1]YES):")
        havelowercaseletters=input()
print("")

#是否包含大写字母
print(end="是否包含大小字母([0]NO [1]YES):")
havecapitalletters=input()
p=0
while p==0:
    if havecapitalletters.isdigit(): #判断是否输入的是数字
        p+=1
        if int(havecapitalletters)<=1: #判断是否小于等于1
            p+=1
            if int(havecapitalletters)>=0: #判断是否大于等于0
                p+=1
    if p!=3:
        p=0
        print(end="[Warning] 非法输入，请重新输入是否包含大小字母([0]NO [1]YES):")
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
    if nx not in keys:
        keys.append(nx)
        print(nx)
        f = open('wordlist-probable.txt', 'a')
        f.write(nx)
        f.write('\n')

