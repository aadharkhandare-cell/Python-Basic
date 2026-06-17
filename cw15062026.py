#15/06/2026
#1
t=(1,2,3,4,4)
a=set(t)
l=len(t)
l1=len(a)
if l==l1:
	print("elements are same")
else:
	print("elements are not same")
#2
list=[]
n=int(input("Enter no fo elements to enter : "))
for i in range(n):
	a=input("Enter element: ")
	list.append(a)
	
b=set(list)
print(b)

#3
d={'Name':"Adhar",'ID No.':12,'Address':"satara"}
print(d)
print(type(d))
d['Name']="Apoorv"
print(d)
for i in d:
	print(i)
print()

for i,j in enumerate (d):
	print(i,j)
print()

for (k,v) in d.items():
	print(k,v,sep=":-")
print()

del(d['Name'])
print(d)
print()

d1=dict(a=192829, b=19)
print(d1)
print()

print(d.keys())
print(d.values())
print(d.items())
print(d.get('Address'))
print(d['Address'])
print()

d.popitem()
print(d)
print(d.pop('ID No.'))
print(d)
d['Address']='kada'
print(d)
d['Address']='satara'
print(d)
d.clear()
print(d)

#4
s="Python is very easy.Python is programming language"
d={}
L=s.split()
for i in L:
	d[i]=L.count(i)
print(d)
