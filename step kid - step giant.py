import math
from re import X

key = [1,2,3,5,7,11,13,17,19,23,29,31,37,41,47,53,59,61,67,71,73,79,83,97,101,103,107,109,113,127,131,137,149,151,157,163,167,173,179,181,191,197,199,211,223,227,229,233,239,241,257,263,269,271,277,281,283,293,307,313,317,331,337,347,349,353,359,367,379,383,389,397,401,409,419,421,431,439,443,449,457,461,463,467,479,487,499,503,509,521,523,541,547,557,563,571,577,587,593,599,45989,61861,58109,40459,53101,45817,36973,49207,41959,57901,47501,50867,49559,47381,42467,48017,54841,60899,35149,51361,53653,58679,34763,64109]
alf =list('абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
u = []
v = []
mes = 0
res = 0
sum = 0
p=0
g=0
message = ''
b=0
i_ind = 0
j_ind = 0 

p_true = False
g_true = False

x = 0
def Code():
    p_true = False
    g_true = False
    sum =0
    i_ind = 0
    j_ind = 0
    while True:
            p = int(input('Введите простое число P: '))
            g = int(input('Введите G(1 < G < P-1) : '))
            message = input('Введите сообщение:')


            for i in key:
                 if(p == i):
                    p_true = True
                 if(g<p-1 ):
                    g_true = True
       
            if(p_true == True and g_true == True):
                break

    for sym in message:
        for i in alf:
            if (sym == i):
                sum=sum+alf.index(i)+1
                
    print('Сумма символов равна: ',sum)

    m = round(math.sqrt(p))
    if(m**2<=p):
        m+=1
    print('Число m = k = ',m)
    b = g**sum % p

    print('Число b ',b)
    print()
    print('\t',end='')


    for i in range(m):
        print(i+1,end='\t')
###############################################################
    print()
    print('Ui     ',end='')
    
    for i in range(m):
        print(( g**((1+i)*m)) % p ,end ='\t')
        u.append(( g**((1+i)*m)) % p )
    
    print()
    print('Vj     ',end='')

    
    for i in range(m):
        print((g**(1+i)*sum) % p,end='\t')
        v.append((g**(1+i)*sum) % p )
#################################################################
    for i in u:
        for j in v:
            if(i == j):            
                i_ind = u.index(i)+1
                j_ind = v.index(j)+1
                print('\nОбщее число строк U и V: ',u[i_ind-1])
                print('I = ',i_ind,' \nJ= ',j_ind)
    x = (m*i_ind - j_ind)
    print('Mi - j = ',x)
    x = x % (p-1)
    print('X равен: ',x)

def Decode():
    p_true = False
    g_true = False
    while True:
            p = int(input('Введите простое число P: '))
            g = int(input('Введите G: '))
            mes = int(input('Введите X: '))

            for i in key:
                 if(p == i):
                    p_true = True
                 if(g<p-1 ):
                    g_true = True
       
            if(p_true == True and g_true == True):
                break
    res = (g**mes)
    res = res % p
    print('Изначальная сумма сообщения: ',res)

change = input('Кодирование / Декодирование :')
if (change == 'K'or change =='k'or change =='К' or change =='к'):
    Code()
    
if (change == 'D'or change =='d'or change =='Д'or change =='д'):
    Decode()