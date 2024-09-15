'''
lst=[11,12,13,14]

lst.append(50)
lst.append(60)

print(lst)

'''

'''
lst=[11,12,13,14]
lst.pop(2)
lst.pop(0)

print(lst)
'''


lst=[11,14,13,12]

lst.sort()

print(lst)

'''
lst=[11,12,13,14]

lst.sort(reverse=True)

print(lst)
'''

'''
lst=[11,12,13,14]

i=13

if i in lst:
    print("exist")
else:
    print("not exist")
'''

''''
lst=[11,12,13,14]
print(len(lst))
'''

'''
s=0
n=int(input("enter the number"))
lst=[]
for i in range(n):
    ele=int(input("enter"))
    lst.append(ele)

print(lst)

for i in range(n):
    s=s+lst[i]
print(s)
'''

'''
s=0
n=int(input("enter the number"))
lst=[]
for i in range(n):
    ele=int(input("enter"))
    lst.append(ele)

print(lst)

for i in range(n):
    if(lst[i]%2==1):
        s=s+lst[i]
print(s)
            
'''

'''
s=0
n=int(input("enter the number"))
lst=[]
for i in range(n):
    ele=int(input("enter"))
    lst.append(ele)

print(lst)

for i in range(n):
    if(lst[i]%2==0):
        s=s+lst[i]
print(s)
'''












'''
pending ***************
s=0
n=int(input("enter the number"))
lst=[]
for i in range(n):
    ele=int(input("enter"))
    lst.append(ele)

print(lst)

for i in range(n):
    if(lst[i]%==0):
        s=s+lst[i]
print(s)
'''

'''
s=0
n=int(input("enter the number"))
lst=[]
for i in range(n):
    ele=int(input("enter"))
    lst.append(ele)

print(lst.clear())
'''

'''
deleting a whole list
s=0
n=int(input("enter the number"))
lst=[]
for i in range(n):
    ele=int(input("enter"))
    lst.append(ele)
'''
'''
s=0
n=int(input("enter the number"))
lst=[]
for i in range(n):
    ele=int(input("enter"))
    lst.append(ele)

print(lst)

for i in range(n):
    s=s+lst[i]
print(s)
'''

'''
s=1
n=int(input("enter the number"))
lst=[]
for i in range(n):
    ele=int(input("enter"))
    lst.append(ele)

print(lst)

for i in range(n):
    s=s*lst[i]
print(s)
'''

'''
d= {1:5.6,
    2:7.8,
    3:6.6,
    4:8.7,
    5:7.7}

d[8]=8.8
print(d)
'''

'''
d= {1:5.6,
    2:7.8,
    3:6.6,
    4:8.7,
    5:7.7}


del d[2]

print(d)
'''

'''
d= {1:5.6,
    2:7.8,
    3:6.6,
    4:8.7,
    5:7.7}


if (d.get(6)==None):
    print("not exist")
else:
    print("exist")
'''
'''
d= {1:5.6,
    2:7.8,
    3:6.6,
    4:8.7,
    5:7.7}

print(len(d))
'''

'''
d= {1:5.6,
    2:7.8,
    3:6.6,
    4:8.7,
    5:7.7}

d1={3:7.1}

d.update(d1)


print(d)
'''

'''
d= {1:5.6,
    2:7.8,
    3:6.6,
    4:8.7,
    5:7.7}

print(d.clear())
'''

'''

s1= {10, 20, 30, 40, 50, 60}
s2= {40, 50, 60, 70, 80, 90}


s1.add(55)
s1.add(66)

print(s1)
'''

'''
s1= {10, 20, 30, 40, 50, 60}
s2= {40, 50, 60, 70, 80, 90}


s1.remove(10)
s1.remove(30)

print(s1)
'''

'''
s1= {10, 20, 30, 40, 50, 60}
s2= {40, 50, 60, 70, 80, 90}

if 40 in s1:
    print("exist")

else:
    print("not exist")
'''

'''
s1= {10, 20, 30, 40, 50, 60}
s2= {40, 50, 60, 70, 80, 90}

s1.union(s2)

print(s1.union(s2))
print(s1.intersection(s2))
'''
'''
n=int(input("enter the number"))

for i in range(n):
    a=input("enter the string")
    if(len(a)==6 or len(a)==8):
        print(a)
    else:
        continue
'''

'''
for i in range(100,1000):
    if((i%7==0) and (i%9==0)):
        print(i)
    else:
        continue
'''
'''
lst=[]

n=int(input("enter the value of n"))

for i in range(n):
    ele=int(input("enter"))
    lst.append(ele)

for i in range(n):
    if(lst[i]%5==0):
        print(lst[i])
'''
'''
n=int(input("enter the number"))

if(n%2==0):
    print("number is even",n)
else:
    print("number is odd",n)

'''

'''
n=input("enter the string")

x=n.count("emma")
print(x)
'''

'''
lst=[]
lst1=[]
lst2=[]
n=int(input("enter the value of n"))

for i in range(n):
    ele=int(input("enter"))
    lst.append(ele)

for i in range(n):
    ele=int(input("enter"))
    lst1.append(ele)

print(lst)
print(lst1)


for i in range(n):
    if(lst[i]%2==1):
        lst2.append(lst[i])
print(lst2)

for i in range(n):
    if(lst1[i]%2==0):
        lst2.append(lst1[i])

        
print(lst2)
'''












































    



























































































































































































































































