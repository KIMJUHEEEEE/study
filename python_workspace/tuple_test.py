tuple_test=(10,20,30)
tuple_test2=10,20,30
print(type(tuple_test2))
print(type(tuple_test[0]))

# tuple은 값 변경 불가능
#tuple_test[0]=20

#swapping
a,b=10,20
temp=a
a=b
b=temp
print(a,b)


c,d=30,40
c,d=d,c
print(c,d)