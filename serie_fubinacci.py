#SERIE FIBONACCI
#Sin usar DEF, es decir, sin funciones
#fn = f-1 + f-2
#f-1 = a
#f-2 = b
#fn = resultado final 
a,b = 0,1
c = a + b
for i in range(10):
    print(a)
    a,b = b,a+b
    #a = b y b = a + b
# 1 a,b=b,a+b a=0 b=0+1=1
# 2 a,b=b,a+b a=1 b=1+0=1
# 3 a,b=b,a+b a=1 b=1+1=2
# 4 a,b=b,a+b a=2 b=2+1=3
# 5 a,b=b,a+b a=3 b=3+2=5
# 6 a,b=b,a+b a=5 b=5+3=8
# 7 a,b=b,a+b a=8 b=8+5=13
# 8 a,b=b,a+b a=13 b=13+8=21
# 9 a,b=b,a+b a=21 b=21+13=34
# 10 a,b=b,a+b a=34 b=34+21=55

a,b = 0,1
c = a + b
nums = int(input("Ingrese la cantidad de números de la serie Fibonacci: "))
for i in range(nums):
    print(a)
    a,b = b,a+b