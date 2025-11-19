print("hello world")
#nomor 4
def bilangan (angka):
    for i in range(1,angka):
        if i % 2 !=0:
            print(i, end=",  ")
bilangan (20)

#nomor 3
print()
def nilai(n = 0):
    if n <=60:
        print("tidak lulus")
    elif n > 60 and n <= 100:
        print("lulus")
    else:
        print("tidak idketahui")
nilai(80)

#nomor 2
print()
def is_genap(n):
    return n % 2 == 0
print(is_genap(2))

#nomor 1
print()
def celcius_ke_fahrenheit (n):
    f = (n * 9/5) + 32
    return f
print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))



    