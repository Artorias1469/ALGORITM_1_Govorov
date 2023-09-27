def F(n):
   if n < 1:
     return n
   else:
     return n + F(n -1)
print(F(2024)-F(2021))