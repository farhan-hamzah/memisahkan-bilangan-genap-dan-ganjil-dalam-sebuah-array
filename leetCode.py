nums = list(map(int, input().split()))
genap = []
ganjil = []
for i in nums:
    if i%2==0:
        genap.append(i)
    else:
        ganjil.append(i)
print("Bilangan genap : ", genap)
print("Bilangan Ganjil: ", ganjil)
