count = 0
m = - 20001
f = open('17.txt')
l = [int(i) for i in f]
for i in range(len(l) - 1):
       if (l[i] % 3 == 0) or (l[i + 1] % 3 == 0):
         count += 1
         m = max(m, l[i] + l[i + 1])
print(count, m)