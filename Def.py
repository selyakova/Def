from math import *

def arithmetic (a1:float,a2:float,sym:str)->any:
    """Lihtne kalkulaator
    +, сложить их; если —, то вычесть; * — умножить; / — разделить
    :param float a1: Esimene arv
    :param float a2: Teine arv
    :param str sym: Tehe
    :rtype: var Määramata tüüp
    """
    if sym in ["+","-", "/", "*"]:
        if sym=="/" and a2==0:
            vas="Div/0"
        else:
            vas=eval(str(a1)+sym+str(a2))
    else:
        vas="Tundmatu tehe!"
    return vas 

def is_year_leap(year:int)->bool:
    """AAsta kalkulaator
    :param int year: Aasta
    :rtype:bool
    """
    if year % 4 == 0:
        t= True
    else:
        t= False
    return t


def square(a:float)->float:
    """Ruudu tehed
    :param float a: Külg
    :rtype:float
    """
    P=4*a
    S=a*a
    d=(a**2) / 2
    k=(P,S,d)
    return k

def season(num:int)->str:
    """Aastaaeg
    :param int num: Kuu järjenumber
    :rtype:str
    """
    if num == 12 or 1 <= num <= 2:
       vas="talv"
    elif  3 <= num <= 5:
       vas="kevad"
    elif 6 <= num <= 8:
       vas="suvi "
    elif 9 <= num <= 11:
       vas="sügis"
    else:
      vas="Неверно введён номер месяца!"
    return vas


def bank (a:int,years:int)->int:
    """Банковский вклад 
    :param int a:вклад 
    :param int years: cроком на years лет
    :rtype:int
    """
    vas=a*0.1*years
    summa=a+vas
    return summa

def is_prime(n:int)->bool:
    """Простые числа 
    :param n int: Arv
    :rtype:int
    """
    i= 2
    while i < n:
        if n%i!=0:
            i +=1
            continue 
        else:        
            return False 
    return True

def date(Year:int,month:int,day:int)->bool:
    """Правильная дата 
    :param int day: Day
    :param int month: Month
    :param int year: Year'
    :rtype:bool
    """
    import datetime
    try:
        datetime.date(Year,month,day)
        return True
    except:
        return False

def XOR_cipher(string,key):
    encrypt_string= ""
    for char in string:
        encrypt_sting += chr(ord(char)^key)
    return encrypt_string
