# импортируем нужные нам библиотеки
import string
import random
# вводим размер матрицы, учитывая, что нужно вввести либо 2, либо 3, либо 4, либо 5
t=0
while t==0:
    M=M=str(input("Введите размер матрицы(2,3,4 или же 5): "))
    if (M=='2' or M=='3' or M=='4' or M=='5'):
        t=1
        print ("Вы выбрали такой размер: ",M,'*',M)
    else:
        print('Похоже, что Вы ввели направильные данные. Повторите ввод снова:')
# создадим двумерный массив (матрицу) для хранения слов
M=int(M)
A=[0]*(M)
for i in range(M):
    A[i]=[0]*M
# выбираем способ ввода 
t=0
while t==0:
    way=str(input("Выберите способ заполнения матрицы: Нажмите 1 (вручную) или  2(автоматически): "))
    if (way=='1' or way=='2'):
        t=1
        print("Вы выбрали: ",way)
    else:
        print ("Похоже, что Вы что-то ввели не так. Нужно ввести 1 или 2, повторите попытку: ")
# осуществляется ввод слов

if (way=='1'):
    alph="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a=''
    t=0
    k=1
    izm="Введите элемент матрицы №"+str(k)+":"
    for i in range(M):
        for j in range(M):
            k+=1
            while t!=4:
                t=0
                a=str(input(izm))
                for x in a:
                    if x in alph:
                        t+=1
                izm="Введите этот элемент повторно\n"
            A[i][j]=a
            izm="Введите элемент матрицы №"+str(k)+":"
            a=''
            t=0
elif (way=='2'):
    for i in range (M):
        for j in range (M):
            A[i][j]=random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+\
            random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
# выводим получившуюся матрицу со словами
print("Исходная матрица имеет вид: ")
for row in A:
    print(' '.join(list(map(str, row))))
# преобразовываем матрицу к нужному виду, опираясь на кодировку ASCII 
for i in range(M):
    for j in range(M):
        A[i][j]=(list(A[i][j]))
for i in range(M):
    for j in range(M):
        for k in range(4):
            A[i][j][k]=str(ord(A[i][j][k]))
for i in range(M):
    for j in range(M):        
        A[i][j]=A[i][j][0]+A[i][j][1]+A[i][j][2]+A[i][j][3]
print("Преобразованная матрица имеет вид: ")
for row in A:
    print(' '.join(list(map(str, row))))
# переведём наш двумерный массив в одномерный, чтобы отсортировать его:
B=[0]*(M*M)
k=0
for i in range(M):
    for j in range(M):
        B[k]=int(A[i][j])
        k+=1
B=sorted(B)
# преобразуем наш одномерный массив B обратнов двумерный массив A:
k=0
for i in range(M):
    for j in range(M):
        A[i][j]=B[k]
        k+=1
# выводим окончательный результат - отсортированную матрицу        
print("Отсортированная матрица имеет вид: ")
for row in A:
    print(' '.join(list(map(str, row))))
        











            













