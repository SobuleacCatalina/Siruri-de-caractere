S=str(input('Introduceti sirul: '))
print(S)
k=0
for i in S:
    if i=='A':
        k+=1
print('Numarul de aparitii a lui "A"= ',k)
S2=S.replace('A','*')
print('Sirul obtinut prin substituirea caracterului "A" prin caracterul "*"= ',S2)
S3=S.replace('B','')
print('Sirul obtinut prin radierea caracterului "B" = ',S3)
aparitiima=0
for i in range(0,len(S)):
    if (S[i]=='M')and(S[i+1]=='A'):
        aparitiima+=1
print('Numarul de aparitii a silabei "MA"= ',aparitiima)
S4=S.replace('MA','TA')
print('Sirul obtinut prin substituirea silabei "MA" prin silaba "TA"= ',S4)
S5=S.replace('TO','')   
print('Sirul obtinut prin radierea silabei "TO" = ',S5)
print('Sirul scris invers= ',S[::-1])