a = [1,2,3,4,1]
x = []
print(a)
print(a.count(1))
#a.reverse()
print(len(a))
print(type(a))
if 2 in a:
    print('true')
b = [1,True,None,'aa',8.00]
print(b)
a.insert(4,5)
print(a)
a.remove(5)
print(a)
a.pop(4)
print(a)
a.append(5)
print(a)
z =[3,5,1,7,0,2]
z.sort()
print(z)
c =a.copy()
print(c)
aa = ['a','b','c','d']
#print(aa[5])
print(aa[-4])
print(aa[3:])
print(a)
print(a[:4])
print(a[-3:])

aa[1:2] = 'divya','pogo','mini','ssss'
print(aa)
print(a)
a[1:2] = 'divya','pogo','mini'
#del(a[1])
print(a)

l =  ['a','b']
m = ['c','d']
l.extend(m)
print(l)

v =('e','f')
l.extend(v)
print(l)

q =[1,2,3,4,5]
print('q=',q)
#q.clear()
print('q=',q)
print(min(q))
print(max(q))