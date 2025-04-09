dentro = 0
fora = 0
for x in range(1,5):
   n = int(input("digite o valor de 10 a 21"))
   if n>=10 and n <=20:
       dentro = dentro + 1
   else:
       fora = fora +1
print(f"total de valores dentro {dentro}, fora {fora}")

