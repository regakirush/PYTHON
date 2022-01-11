import time
print ("Hello word!")


a = 1
b = 15
c = a + b
print (type(c), c)

d = 'Regina'
print (type(d), d)

v = 1.5
print (type(v), v)

q = False
print (type(q), q)

l = [a, b, c, d, v, q, 'Regina', ['Andrew', 28, True]]
print (type (l), l)

if a < 5:
    print('a > 5')
else:
    print ('Else')

count = 0
while count < 10:

    time.sleep (.500)
    count +=1
    print ('count =', count)